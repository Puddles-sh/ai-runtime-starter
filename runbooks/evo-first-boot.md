# EVO-X2 First Boot Runbook

## Purpose

Bring the GMKtec EVO-X2 online as a stable local AI services host. This runbook reflects a
validated real-world deployment — every step has been run on this exact hardware.

## Hardware

- GMKtec EVO-X2 — AMD Ryzen AI Max+ 395 (Strix Halo, gfx1151, RDNA 3.5, 40 CUs)
- 128GB unified memory (GPU and CPU share the same physical pool — no discrete VRAM)
- 2TB NVMe storage
- Ubuntu 24.04 LTS

### Memory Architecture (Read This First)

The 128GB pool is split at the BIOS level:
- **GPU UMA (VRAM):** 96GB (set in BIOS)
- **CPU system RAM:** ~31GB (remainder)

This means if a model falls back to CPU, it only has 31GB. A 35B model alone is 21GB —
add a 32K KV cache and you OOM instantly. **GPU inference is not optional on this machine.**

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
- Standard partitioning is fine — the LVM will be expanded in the next step

After first boot into the OS:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget git htop tuned tmux
```

### Expand LVM to Full Drive

**Critical — do this immediately.** Ubuntu's installer defaults to ~100GB root partition
and leaves the rest of the 2TB drive unallocated. You will run out of space pulling models.

```bash
sudo lvextend -l +100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
df -h  # confirm / shows ~2TB
```

### Hostname and Network

```bash
sudo hostnamectl set-hostname evo-x2
ip a  # confirm IP, note it for static/reserved DHCP lease
```

### Performance Profile

```bash
sudo systemctl enable --now tuned
sudo tuned-adm profile accelerator-performance
tuned-adm active  # confirm profile is set
```

---

## Step 2 — Kernel Version

Kernel **6.16.9 specifically** is required for full Strix Halo memory access.

> Do NOT use kernel 6.17 — known ABI incompatibility with ROCm causes llama-server to
> segfault on startup. Stay on 6.16.9 until ROCm confirms 6.17 support.

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

If the 6.16.9 entry is missing, grub wasn't updated. Fix:
```bash
mainline install 6.16.9  # re-run — the reinstall triggers update-grub
# OR:
sudo update-grub
```

Confirm the entry appears, then reboot:
```bash
sudo reboot
uname -r  # should show 6.16.9-061609-generic
```

---

## Step 3 — GPU Memory Configuration

Without this step the GPU can only access a small slice of the 128GB unified pool.

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

### Modprobe Config

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

> `amdgpu-dkms` and `rocm` are **not** in the default Ubuntu repos. Do not run
> `apt install rocm` — it will fail. The AMD repo must be added first via the
> `amdgpu-install` script.

Download and install the AMD repo configurator (check current version at
https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html):

```bash
wget https://repo.radeon.com/amdgpu-install/6.4/ubuntu/noble/amdgpu-install_6.4.60400-1_all.deb
sudo apt install -y ./amdgpu-install_6.4.60400-1_all.deb
sudo apt update
sudo amdgpu-install -y --usecase=rocm
```

This pulls several GB — let it run.

### GPU Device Permissions

```bash
sudo nano /etc/udev/rules.d/99-amd-kfd.rules
```

Add:
```
SUBSYSTEM=="kfd", GROUP="render", MODE="0666"
SUBSYSTEM=="drm", KERNEL=="card[0-9]*", GROUP="render", MODE="0666"
SUBSYSTEM=="drm", KERNEL=="renderD[0-9]*", GROUP="render", MODE="0666"
```

### User Groups

```bash
sudo usermod -aG render,video $USER
newgrp render
```

### Check for amdgpu Blacklist

`amdgpu-dkms` sometimes fails to build and leaves a blacklist that blocks the in-tree
driver. Check for it before rebooting:

```bash
grep -r "amdgpu" /etc/modprobe.d/
```

If you see `blacklist amdgpu` in any file:
```bash
sudo dpkg --purge amdgpu-dkms
sudo rm -f /etc/modprobe.d/blacklist-amdgpu.conf
sudo update-initramfs -u
```

> Use `--purge` not `--remove` — `--remove` leaves the config files behind and the
> blacklist comes back on next boot.

### Blacklist the NPU Driver

The `amdxdna` NPU driver conflicts with amdgpu for shared virtual memory and will
flood the kernel log with errors and destabilize the system at idle. Ollama does not
use the NPU — blacklist it:

```bash
echo "blacklist amdxdna" | sudo tee /etc/modprobe.d/blacklist-amdxdna.conf
sudo update-initramfs -u
```

Reboot to apply all driver changes:

```bash
sudo reboot
```

---

## Step 5 — Verification

Confirm everything is working before installing Ollama.

```bash
# Kernel version — must be 6.16.9
uname -r

# GPU driver loaded
lsmod | grep amdgpu

# NPU driver absent
lsmod | grep amdxdna  # should return nothing

# GPU memory — should show ~137438953472 bytes (128GB)
find /sys/devices -name "mem_info_gtt_total" 2>/dev/null | xargs cat

# ROCm — GPU should be detected as gfx1151
rocminfo | grep -A5 "Agent 2"

# Live GPU stats
rocm-smi
```

**Pass criteria:**
- Kernel shows 6.16.9
- `amdgpu` loaded, `amdxdna` absent
- `mem_info_gtt_total` shows ~137438953472
- `rocminfo` shows GPU agent with gfx1151
- `rocm-smi` shows GPU accessible (GPU% column responds during inference; VRAM% always
  shows 0% on unified memory — this is expected)

If verification passes, proceed. If not, diagnose before continuing.

---

## Step 6 — Ollama

Ollama runs natively on the host for best AMD GPU performance. Docker adds unnecessary
complexity for ROCm passthrough.

```bash
curl -fsSL https://ollama.ai/install.sh | sh
sudo systemctl enable ollama
```

### Service Override (Critical)

Without this configuration Ollama cannot find the GPU and defaults to CPU inference.

```bash
sudo systemctl edit ollama
```

Paste the entire block — the `[Unit]` section must be included:

```ini
[Unit]
After=dev-dri-renderD128.device
Wants=dev-dri-renderD128.device

[Service]
Environment="OLLAMA_NUM_CTX=32768"
Environment="PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/rocm/bin"
Environment="LD_LIBRARY_PATH=/opt/rocm/lib"
Environment="HSA_OVERRIDE_GFX_VERSION=11.5.1"
Environment="HSA_XNACK=1"
Environment="OLLAMA_MAX_LOADED_MODELS=1"
ExecStartPre=/bin/bash -c 'until [ -c /dev/dri/renderD128 ]; do sleep 1; done'
```

| Variable | Why |
|---|---|
| `HSA_OVERRIDE_GFX_VERSION=11.5.1` | Required for gfx1151 — without it Ollama falls back to CPU (~5 t/s). `11.0.0` does NOT work. |
| `HSA_XNACK=1` | Enables page fault recovery on the GPU. Without it, long inference runs crash with "ROCm unspecified launch failure". |
| `LD_LIBRARY_PATH` | Ensures Ollama finds ROCm libraries at `/opt/rocm/lib` |
| `After=` / `ExecStartPre=` | Waits for the GPU device node before starting — prevents CPU fallback on fast boots |
| `OLLAMA_MAX_LOADED_MODELS=1` | Prevents Open WebUI from holding multiple models in memory simultaneously |

Apply:
```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

Verify GPU is being used:
```bash
ollama run qwen3:8b "hi" &
sleep 5 && ollama ps  # PROCESSOR column must show GPU, not CPU
```

---

## Step 7 — Docker

```bash
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

> Note: `docker-compose-plugin` is not available on Ubuntu 24.04. Use `docker-compose` (standalone).

---

## Step 8 — Open WebUI

```bash
docker run -d \
  --network=host \
  --name open-webui \
  --restart always \
  -v open-webui:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

Verify:
```bash
docker ps | grep webui
```

Access at `http://localhost:3000` or `http://<evo-ip>:3000` from LAN.

---

## Step 9 — Pull Models

Pull smallest to largest so you're productive immediately while larger models download.

```bash
# Embeddings — required for RAG and memory
ollama pull nomic-embed-text

# Chat and reasoning
ollama pull qwen3:8b
ollama pull qwen3:14b
ollama pull deepseek-r1:8b
ollama pull deepseek-r1:14b

# Coding and scripting — primary PowerShell/Graph generation models
ollama pull qwen2.5-coder:7b
ollama pull qwen2.5-coder:14b
ollama pull qwen2.5-coder:32b

# Qwen3.6 MoE — 36B total, ~3B active, vision capable, 262K context, ~50 t/s
ollama pull qwen3.6:35b

# Gemma4 MoE — 26B total, 4B active, 256K context, ~50 t/s, best Graph API scores in benchmark
ollama pull gemma4:26b
```

> **Note:** `llama3.2-vision:11b` uses the `mllama` architecture which ROCm does not
> currently support. Skip it — `qwen3.6:35b` covers vision use cases.

Confirm:
```bash
ollama list
```

---

## Step 10 — First Model Test

```bash
ollama run qwen3:14b "explain what this machine is in one paragraph"
```

In a second terminal while it responds:
```bash
ollama ps          # PROCESSOR must show GPU
rocm-smi           # GPU% must show >0%
```

**Expected performance baseline (validated on this hardware):**

| Model | Type | Speed |
|---|---|---|
| qwen3:8b | Dense | ~38-40 t/s (thinking on) / ~55 t/s (thinking off) |
| qwen3:14b | Dense | ~22 t/s (thinking on) / ~59 t/s (thinking off) |
| qwen3.6:35b | MoE | ~50 t/s at 262K context |
| qwen2.5-coder:32b | Dense | ~8-10 t/s |

If numbers are significantly lower, check that GRUB parameters applied and the GPU is
not falling back to CPU.

---

## Step 11 — Confirm Reachable from MacBook

From the MacBook terminal:
```bash
curl http://evo-x2.local:11434/api/tags
```

If mDNS doesn't resolve, use the IP directly:
```bash
curl http://<evo-ip>:11434/api/tags
```

---

## Step 12 — Run Benchmark

```bash
cd ~/projects/ai-runtime-starter
python3 scripts/ollama_model_benchmark.py \
  qwen3:8b qwen3:14b qwen2.5-coder:32b qwen3.6:35b \
  --host http://localhost:11434 \
  --prompt-set all \
  --prompt-size short \
  --runs 1
```

Results stream to `~/benchmark-results/` as each prompt completes — safe to Ctrl-C.

Then score with Opus:
```bash
python3 scripts/opus_scorer.py ~/benchmark-results/ollama-benchmark-*.jsonl
```

---

## Step 13 — Claude Code and API Key

### API Key

```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.bashrc
source ~/.bashrc
echo $ANTHROPIC_API_KEY  # confirm it prints
```

> Never commit this value to git.

### Claude Code

```bash
sudo npm install -g @anthropic-ai/claude-code
claude --version
claude  # log in with Anthropic account on first launch
```

### SSH Passwordless Login — MacBook → EVO

**On the MacBook:**

Check if an SSH key already exists:
```bash
ls ~/.ssh/id_*.pub
```

If none exists, generate one:
```bash
ssh-keygen -t ed25519 -C "mac-to-evo"
# Accept the default path (~/.ssh/id_ed25519), passphrase optional
```

Copy the public key to the EVO (you'll be prompted for the EVO password one last time):
```bash
ssh-copy-id <user>@evo-x2.local
```

If mDNS isn't resolving yet, use the IP:
```bash
ssh-copy-id <user>@<evo-ip>
```

**Set up SSH config for convenience:**

```bash
nano ~/.ssh/config
```

Add:
```
Host evo
    HostName evo-x2.local
    User <user>
    IdentityFile ~/.ssh/id_ed25519
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

Now you can connect with just:
```bash
ssh evo
```

**Test:**
```bash
ssh evo  # should connect without password prompt
ssh evo "ollama list"  # confirm remote commands work
```

**On the EVO — verify the key landed:**
```bash
cat ~/.ssh/authorized_keys  # should show your Mac's public key
```

---

## Known Issues

| Issue | Cause | Fix |
|---|---|---|
| `Unable to locate package rocm` | AMD repo not added | Use `amdgpu-install` script — see Step 4 |
| `Unit file tuned.service does not exist` | tuned not installed | `sudo apt install -y tuned` then retry |
| Kernel not in grub after mainline install | mainline didn't trigger update-grub | Re-run `mainline install 6.16.9` or `sudo update-grub` |
| Ollama runs on CPU despite GPU present | `HSA_OVERRIDE_GFX_VERSION` not set | Must be `11.5.1` — `11.0.0` does not work for gfx1151 |
| CPU fallback persists after setting HSA override | Race condition — Ollama started before GPU driver ready | Ensure `[Unit] After=dev-dri-renderD128.device` and `ExecStartPre` are in override — see Step 6 |
| amdgpu missing after reboot | `amdgpu-dkms` blacklist surviving purge | `sudo dpkg --purge amdgpu-dkms && sudo rm -f /etc/modprobe.d/blacklist-amdgpu.conf && sudo update-initramfs -u && sudo reboot` — must use `--purge` not `--remove` |
| ROCm unspecified launch failure on long generation | XNACK disabled — GPU crashes on page fault | Add `Environment="HSA_XNACK=1"` to ollama override — see Step 6 |
| `amdxdna` SVA bind errors flooding kernel log, system unstable at idle | NPU driver conflicts with amdgpu for SVM memory | Blacklist amdxdna — see Step 4 |
| OOM kill during model load | Model fell back to CPU — only 31GB available to CPU | Confirm GPU inference is working before loading large models |
| `VRAM% 0%` in rocm-smi | Expected on unified memory — no discrete VRAM to measure | Normal — use `GPU%` column as the utilization indicator |
| `mllama` architecture error on llama3.2-vision | ROCm does not support mllama | Skip — use qwen3.6:35b for vision tasks |
| `docker-compose-plugin` not found | Not available on Ubuntu 24.04 | Use `docker-compose` (standalone) |
| Model outputs raw role tokens (`<\|start_of_role\|>`) | GGUF missing embedded chat template | Create a Modelfile with the correct TEMPLATE for the model |
| Wi-Fi not working | Ubuntu 25.x kernel issue | Use Ubuntu 24.04 LTS only |

---

## Notes

- **mDNS hostname (`evo-x2.local`)** resolves automatically on the local network via Avahi (installed by default on Ubuntu). If it stops resolving, check `sudo systemctl status avahi-daemon`.
- **Ollama listens on `127.0.0.1:11434` by default** — it is not reachable from the MacBook without adding `Environment="OLLAMA_HOST=0.0.0.0:11434"` to the service override. Add this if you want to hit the API from the Mac without SSH tunneling.
- **Scoring env (`scoring`)** is a Python venv at `~/envs/scoring` with `anthropic` installed. Activate with `source ~/envs/scoring/bin/activate`. Keep `ANTHROPIC_API_KEY` in `~/.bashrc` so it's available inside the venv.
- **tmux** is the recommended way to run overnight benchmarks — detach with `Ctrl-B D`, reattach with `tmux attach`. Benchmark writes stream to disk after every prompt so a disconnect loses nothing.
- **Model storage** defaults to `~/.ollama/models`. With 2TB NVMe this is fine — no need to relocate.
- **Open WebUI** auto-updates when you restart the container with `docker pull` — do this deliberately, not on a schedule, since updates occasionally break things.
- **Benchmark results** write to `~/benchmark-results/` by default. Copy to Mac via `scp` or mount via SSHFS if needed.

---

## Done Criteria

- [ ] BIOS configured — Secure Boot off, UMA 96GB, IOMMU off, 85W
- [ ] Kernel 6.16.9 confirmed via `uname -r`
- [ ] LVM expanded — `df -h /` shows ~2TB
- [ ] GPU memory 128GB confirmed via `mem_info_gtt_total`
- [ ] `amdxdna` blacklisted — `lsmod | grep amdxdna` returns nothing
- [ ] `rocminfo` shows gfx1151 GPU agent
- [ ] `tuned` profile set to `accelerator-performance`
- [ ] Ollama service override applied with all env vars
- [ ] `ollama ps` shows GPU (not CPU) during inference
- [ ] Open WebUI running and reachable at port 3000
- [ ] All models pulled and listed in `ollama list`
- [ ] EVO reachable from MacBook by hostname
- [ ] Benchmark run completed, results saved to `~/benchmark-results/`
- [ ] `ANTHROPIC_API_KEY` set in `~/.bashrc`
- [ ] Claude Code installed and logged in
- [ ] SSH passwordless login from MacBook confirmed
