# EVO-X2 First Boot Runbook

## Purpose

Bring the EVO-X2 online as a stable local AI services host.

## Hardware

- GMKtec Mini AI — AMD Ryzen AI Max+ 395 (Strix Halo, gfx1151, RDNA 3.5, 40 CUs)
- 128GB unified memory (GPU and CPU share the same pool — no discrete VRAM ceiling)
- 2TB NVMe storage
- Ubuntu 24.04 LTS

## Reference

Configuration validated against real-world EVO-X2 deployment:
https://github.com/pablo-ross/strix-halo-gmktec-evo-x2

---

## Step 0 — BIOS Configuration (Before OS Install)

Access BIOS at startup via **ESC** or **DEL**. Apply these settings before installing the OS.

### Secure Boot
- **Disable Secure Boot** — required for third-party AMD drivers and stability.

### GPU Memory
- Navigate to **Integrated Graphics** or **AMD CBS**
- Set **UMA Frame Buffer Size** to **96GB** (or highest available)
- This pre-allocates unified memory to the GPU pool for inference

### IOMMU
- Set **IOMMU** to **Disabled** — provides ~6% memory read improvement
- Exception: leave enabled only if you plan to use GPU passthrough via VM

### Power Mode
- Set **Power Mode** to **85W** — optimal balance between performance and thermals

### Boot Order
- Prioritize **USB** for OS installation

---

## Step 1 — OS Installation

**Required:** Ubuntu 24.04 LTS

> Do NOT use Ubuntu 25.04 or 25.10 — Wi-Fi issues require a Windows BIOS update first.
> Stick with 24.04 LTS.

During installation:
- Select **Install OpenSSH server** for remote access from MacBook
- Standard partitioning is fine

After first boot into the OS:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget git htop tuned tmux
```

**Critical — expand LVM to use the full drive immediately after first boot.** Ubuntu's installer defaults to ~100GB root partition and leaves the rest unallocated. You will run out of space pulling models.

```bash
sudo lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
df -h  # confirm / shows ~2TB
```

Set hostname and confirm network:

```bash
sudo hostnamectl set-hostname evo-x2
ip a  # confirm IP, note it for static/reserved DHCP lease
```

### Performance Profile

Enable the accelerator performance tuning profile for a free 5-8% improvement:

> `tuned` is included in the apt install above. If you skipped that step or hit an error,
> `systemctl enable --now tuned` will fail with "Unit file tuned.service does not exist".
> Run `sudo apt install -y tuned` first, then continue.

```bash
sudo systemctl enable --now tuned
sudo tuned-adm profile accelerator-performance
tuned-adm active  # confirm profile is set
```

---

## Step 2 — Kernel Version

Kernel **6.16.9 specifically** is required for full Strix Halo memory access.

> Do NOT use kernel 6.17 — it has a known ABI incompatibility with ROCm that causes
> llama-server to segfault on startup. Stay on 6.16.9 until ROCm confirms 6.17 support.

Check current kernel:
```bash
uname -r
```

If not on 6.16.9, install via the `mainline` tool:
```bash
sudo add-apt-repository ppa:cappelikan/ppa
sudo apt update
sudo apt install mainline
mainline install 6.16.9
```

**Before rebooting**, verify the kernel was added to grub:
```bash
grep "menuentry" /boot/grub/grub.cfg | grep "6.16.9"
```

If the 6.16.9 entry is missing, the install completed but grub wasn't updated. Fix:
```bash
mainline install 6.16.9  # re-run — the reinstall triggers update-grub
# OR manually:
sudo update-grub
```

Confirm the entry appears, then reboot:
```bash
sudo reboot
```

Confirm after reboot:
```bash
uname -r  # should show 6.16.9-061609-generic
```

---

## Step 3 — GPU Memory Configuration

This is the most critical step for inference performance. Without it, the GPU can only
access a small slice of the 128GB unified pool.

### GRUB Parameters

```bash
sudo nano /etc/default/grub
```

Find `GRUB_CMDLINE_LINUX_DEFAULT` and set it to:

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amd_iommu=off amdgpu.gttsize=131072 ttm.pages_limit=33554432"
```

> `gttsize=131072` = full 128GB pool exposed to GPU
> `ttm.pages_limit=33554432` = 128GB page limit (up from default 120GB)

Apply:
```bash
sudo update-grub
```

### Modprobe Config (Belt and Suspenders)

Also set via modprobe so it persists across kernel updates:

```bash
sudo nano /etc/modprobe.d/amdgpu_llm_optimized.conf
```

Add:
```
options amdgpu gttsize=131072
options ttm pages_limit=33554432
options ttm page_pool_size=33554432
```

Apply and reboot:
```bash
sudo update-initramfs -u -k all
sudo reboot
```

---

## Step 4 — ROCm Drivers

Install AMD's unified Linux drivers and ROCm for GPU-accelerated inference.

> `amdgpu-dkms` and `rocm` are **not** in the default Ubuntu repos. Running
> `apt install rocm` will fail with "Unable to locate package". The AMD repo
> must be added first via the `amdgpu-install` script.

Download and install the AMD repo configurator (check current version at
https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html):

```bash
wget https://repo.radeon.com/amdgpu-install/6.4/ubuntu/noble/amdgpu-install_6.4.60400-1_all.deb
sudo apt install -y ./amdgpu-install_6.4.60400-1_all.deb
sudo apt update
```

Then install the drivers and ROCm stack:

> **Critical:** After ROCm install, Ollama will default to CPU inference. The HSA
> override and ROCm library path must be added to the Ollama service. See Step 6.

```bash
sudo amdgpu-install -y --usecase=rocm
```

This pulls several GB — let it run.

### GPU Device Permissions

Create a udev rule so your user can access the GPU without sudo:

```bash
sudo nano /etc/udev/rules.d/99-amd-kfd.rules
```

Add:
```
SUBSYSTEM=="kfd", GROUP="render", MODE="0666"
SUBSYSTEM=="drm", KERNEL=="card[0-9]*", GROUP="render", MODE="0666"
SUBSYSTEM=="drm", KERNEL=="renderD[0-9]*", GROUP="render", MODE="0666"
```

This prevents `HSA_STATUS_ERROR_OUT_OF_RESOURCES` errors during inference.

### User Groups

```bash
sudo usermod -aG render,video $USER
newgrp render
```

**Before rebooting**, check if `amdgpu-dkms` left a blacklist that will block the in-tree driver:

```bash
grep -r "amdgpu" /etc/modprobe.d/
```

If you see `blacklist amdgpu` in any file, remove it:

```bash
sudo rm /etc/modprobe.d/blacklist-amdgpu.conf
sudo update-initramfs -u
```

> This blacklist is created automatically when `amdgpu-dkms` fails to build. Without
> removing it, the in-tree amdgpu driver will not load on boot and the GPU disappears.

Reboot to apply all driver and permission changes:

```bash
sudo reboot
```

---

## Step 5 — Verification

Confirm everything is working before installing Ollama.

```bash
# Kernel version — must be 6.16.9
uname -r

# GPU memory — should show ~128GB (131072 MB)
cat /sys/class/drm/card*/device/mem_info_gtt_total

# All memory stats
for file in /sys/class/drm/card*/device/mem_info*; do echo "$file: $(cat $file)"; done

# ROCm — GPU should be detected as gfx1151
rocminfo | grep -A50 'Agent 2'

# Live GPU stats
rocm-smi
```

**Pass criteria:**
- Kernel shows 6.16.9
- `mem_info_gtt_total` shows ~128GB
- `rocminfo` shows GPU agent with gfx1151
- `rocm-smi` shows GPU accessible

If verification passes, proceed. If not, do not continue — diagnose first.

---

## Step 6 — Ollama (Native, Not Docker)

Ollama runs natively on the host for best AMD GPU performance. Docker adds unnecessary
complexity for ROCm passthrough.

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

Confirm Ollama is running:

```bash
systemctl status ollama
curl http://localhost:11434/api/tags
```

Enable on boot:

```bash
sudo systemctl enable ollama
```

### Context Window Configuration

Ollama's default context window is conservative. Agent chains pass accumulated state
between nodes — scripts, logs, prior outputs. Set a larger default so benchmark results
reflect real agent workload conditions:

```bash
sudo systemctl edit ollama
```

Add:
```ini
[Service]
Environment="OLLAMA_NUM_CTX=32768"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/rocm/bin"
Environment="LD_LIBRARY_PATH=/opt/rocm/lib"
Environment="HSA_OVERRIDE_GFX_VERSION=11.5.1"
```

> `HSA_OVERRIDE_GFX_VERSION=11.5.1` is required for gfx1151 (Strix Halo). Without it,
> Ollama cannot detect the GPU and falls back to CPU inference (~5 t/s vs ~40-70 t/s).
> `11.0.0` does NOT work — must be `11.5.1`.

Apply:
```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

Verify GPU is being used:
```bash
ollama run qwen3:8b "hi" &
sleep 3 && ollama ps  # PROCESSOR column must show GPU, not CPU
```

---

## Step 7 — Docker (For Everything Else)

```bash
sudo apt install -y docker.io docker-compose-plugin
sudo usermod -aG docker $USER
newgrp docker
```

Verify:

```bash
docker run hello-world
```

---

## Step 8 — Pull Models

Pull smallest to largest so you're productive immediately while larger models download.

```bash
# Embeddings — required for RAG and memory
ollama pull nomic-embed-text

# Chat and reasoning — comparison set
ollama pull qwen3:8b
ollama pull deepseek-r1:8b
ollama pull qwen3:14b
ollama pull deepseek-r1:14b

# Vision — required for Teams screenshot parsing workflow
ollama pull llama3.2-vision:11b

# Coding and scripting — primary PowerShell/Graph generation models
ollama pull qwen2.5-coder:7b
ollama pull qwen2.5-coder:14b
ollama pull qwen2.5-coder:32b

# Qwen3.6 — coding-focused, 256K context, vision support, thinking preservation
# Benchmark against qwen2.5-coder:32b to determine best coding daily driver
ollama pull qwen3.6:35b
```

Confirm all models loaded:

```bash
ollama list
```

---

## Step 9 — First Model Test

```bash
ollama run qwen3:14b
```

Ask it something simple. Confirm response is coherent and GPU is being used:

```bash
# In a second terminal while model is running
rocm-smi  # GPU% should show >0% during inference; VRAM% will always show 0% on unified memory — this is expected
```

**Expected performance baseline (validated on same hardware):**
- qwen3:30B — ~71 tok/sec
- qwen3:8b — ~55 tok/sec

If numbers are significantly lower, check that GRUB parameters applied correctly.

---

## Step 10 — Confirm Reachable from MacBook

From the MacBook terminal:

```bash
curl http://evo-x2.local:11434/api/tags
```

If mDNS doesn't resolve, use the IP directly:

```bash
curl http://<evo-ip>:11434/api/tags
```

---

## Step 11 — Run Benchmark

Once models are pulled, run the full benchmark suite:

```bash
cd /opt/ai-runtime
python3 scripts/ollama_model_benchmark.py \
  qwen3:8b qwen3:14b deepseek-r1:8b deepseek-r1:14b \
  qwen2.5-coder:7b qwen2.5-coder:14b qwen2.5-coder:32b qwen3.6:35b \
  --host http://localhost:11434 \
  --prompt-set all \
  --runs 3
```

Then score the outputs:

```bash
python3 scripts/opus_scorer.py \
  projects/homelab/outputs/model-benchmarks/ollama-benchmark-*.json
```

Results saved to `AI/projects/homelab/outputs/model-benchmarks/`.

---

## Step 12 — Claude Code (Remote Dev) and Claude API Access

### Claude API Key

The Opus scorer and any agent that calls Claude needs the API key available as an
environment variable. Add it to your shell profile so it persists across sessions:

```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
source ~/.bashrc
```

Verify:
```bash
echo $ANTHROPIC_API_KEY  # should print the key
```

> Never commit this value to git. The `.gitignore` already excludes `.env` files —
> if you prefer storing it there, use a `.env` file and load it via `source .env`.

### Claude Code Installation

Claude Code lets you SSH into the EVO and run an AI-assisted dev session remotely
from your MacBook terminal — same experience as local, running on EVO hardware.

Install Node.js first (Claude Code requires it):
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
node --version  # confirm 22.x
```

Install Claude Code globally:
```bash
npm install -g @anthropic-ai/claude-code
```

Confirm it's working:
```bash
claude --version
```

### Remote Dev Workflow

Claude Code has a built-in remote control feature — no manual SSH session required.

**Option 1 — Claude Code UI (recommended):**
In the Claude Code sidebar, click the host selector → **Set up Remote Control** →
**Add SSH host** → enter `charles@evo-x2.local`. Claude Code handles the connection
natively. All file access and commands run on the EVO, MacBook is just the UI.

**Option 2 — Terminal:**
```bash
claude rc
```
Follow the prompts to register the EVO as a remote host.

Claude Code will use the `ANTHROPIC_API_KEY` from the EVO's environment. All file
access, bash commands, and context are on the EVO — your MacBook is just the interface.

### SSH Key for MacBook → EVO

Add your MacBook's public key to the EVO so you can SSH without a password:

On MacBook:
```bash
ssh-copy-id charles@evo-x2.local
```

Or manually — on MacBook, copy the public key:
```bash
cat ~/.ssh/id_ed25519.pub
```

On EVO, append it:
```bash
mkdir -p ~/.ssh
echo "ssh-ed25519 AAAA..." >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

Test passwordless login:
```bash
ssh charles@evo-x2.local  # should connect without password prompt
```

> MCP server integration (exposing EVO tools to Claude Code on MacBook) is a
> future phase — see build-roadmap.md Phase 6+.

---

## Known Issues

| Issue | Cause | Fix |
|---|---|---|
| `Unable to locate package rocm` | AMD repo not added | Use `amdgpu-install` script first — see Step 4 |
| `Unit file tuned.service does not exist` | tuned not installed | `sudo apt install -y tuned` then retry |
| Kernel installed but not in grub after reboot | mainline didn't trigger update-grub | Re-run `mainline install 6.16.9` or `sudo update-grub` before rebooting |
| Ollama runs on CPU despite GPU being present | `HSA_OVERRIDE_GFX_VERSION` not set or wrong value | Add `HSA_OVERRIDE_GFX_VERSION=11.5.1` to ollama systemd override — `11.0.0` does not work for gfx1151 |
| amdgpu missing after reboot, `lsmod` shows nothing | `amdgpu-dkms` build failure creates `/etc/modprobe.d/blacklist-amdgpu.conf` which blocks the in-tree driver | `sudo rm /etc/modprobe.d/blacklist-amdgpu.conf && sudo update-initramfs -u && sudo reboot` |
| llama-server segfaults on startup | Kernel 6.17 + ROCm ABI mismatch | Stay on kernel 6.16.9 |
| `HSA_STATUS_ERROR_OUT_OF_RESOURCES` | Missing udev rules or wrong groups | Add 99-amd-kfd.rules, re-add user to render/video |
| GPU only sees small memory slice | GRUB gttsize not applied | Verify `/etc/default/grub` and rerun `update-grub` |
| Slow inference despite GPU | Flash attention disabled | Add `-fa 1` flag if using llama.cpp directly |
| Wi-Fi not working | Ubuntu 25.x kernel issue | Use Ubuntu 24.04 LTS only |

---

## Session Notes — 2026-06-25 Boot/OOM Fixes

### What Was Broken

- Ollama loading models on CPU after reboots — race condition where Ollama started before the amdgpu driver was fully initialized
- OOM kills — CPU RAM is only ~31GB (96GB is reserved as GPU UMA); a model falling back to CPU + 32K KV cache would exhaust system RAM instantly
- Multiple models loading simultaneously from Open WebUI compounding the OOM risk

### Fixes Applied

`/etc/systemd/system/ollama.service.d/override.conf`:

```ini
[Unit]
After=dev-dri-renderD128.device
Wants=dev-dri-renderD128.device

[Service]
Environment="OLLAMA_NUM_CTX=32768"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/rocm/bin"
Environment="LD_LIBRARY_PATH=/opt/rocm/lib"
Environment="HSA_OVERRIDE_GFX_VERSION=11.5.1"
Environment="OLLAMA_MAX_LOADED_MODELS=1"
ExecStartPre=/bin/bash -c 'until [ -c /dev/dri/renderD128 ]; do sleep 1; done'
```

- `After=` / `Wants=` — systemd waits for the DRM device node before starting Ollama
- `ExecStartPre` — belt-and-suspenders poll in case driver init lags behind the device node
- `OLLAMA_MAX_LOADED_MODELS=1` — prevents Open WebUI from silently holding multiple models in VRAM

### Memory Architecture (Important)

128GB unified memory is split at BIOS level:
- **GPU UMA (VRAM):** 96GB
- **CPU system RAM:** ~31GB

A model on CPU only has 31GB. A 35GB model + 32K KV cache cannot fit. This is why OOM happens — not because the machine is small, but because the BIOS UMA split means CPU fallback = instant OOM.

**Rule:** never load more than one large model. Stop the current model before switching.

### Models Removed

- `llama3.2-vision:11b` — ROCm does not support mllama architecture
- `hf.co/SandLogicTechnologies/Mistral-NeMo-12B-Instruct-GGUF:Q4_K_M` — removed from stack
- `hf.co/OBLITERATUS/Qwen3.6-27B-OBLITERATED:latest` — 0.54 t/s due to 262K context default, removed
- `hf.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Aggressive:latest` — Q2 quant, garbage output

### Confirmed Working

- `qwen3:8b` — ~40 t/s, 100% GPU
- `qwen3:14b` — ~59 t/s, 100% GPU
- `qwen3.6:35b` — MoE, ~50 t/s, 100% GPU, vision capable, 262K context
- `hf.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive:Q4_K_M` — ~55 t/s, 100% GPU, 262K context

### If CPU Fallback Happens Again

```bash
ollama stop <model>
sudo systemctl restart ollama
sleep 3
ollama run <model> "hi"
ollama ps  # PROCESSOR must show GPU
```

Check for driver instability (different problem from boot ordering):

```bash
journalctl -k | grep -E "amdgpu.*reset|ring.*timeout"
```

---

## Done Criteria

- [ ] BIOS configured — Secure Boot off, UMA 96GB+, IOMMU off, 85W power mode
- [ ] Kernel 6.16.9 confirmed via `uname -r`
- [ ] GPU memory 128GB confirmed via `mem_info_gtt_total`
- [ ] `rocminfo` shows gfx1151 GPU agent
- [ ] `tuned` profile set to `accelerator-performance`
- [ ] EVO reachable from MacBook by hostname
- [ ] Ollama API responding on port 11434
- [ ] ROCm GPU visible during model inference
- [ ] All models pulled and listed in `ollama list`
- [ ] Benchmark run completed, scored, results saved
- [ ] Docker running and verified
- [ ] `ANTHROPIC_API_KEY` set in `~/.bashrc`, persists across sessions
- [ ] Claude Code installed, `claude --version` responds
- [ ] SSH passwordless login from MacBook confirmed
- [ ] Claude Code session launched remotely over SSH from MacBook
- [ ] Notes saved under this homelab project
