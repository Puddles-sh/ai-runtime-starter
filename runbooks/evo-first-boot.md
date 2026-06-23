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
sudo apt install -y curl wget git htop tuned
```

Set hostname and confirm network:

```bash
sudo hostnamectl set-hostname evo-x2
ip a  # confirm IP, note it for static/reserved DHCP lease
```

### Performance Profile

Enable the accelerator performance tuning profile for a free 5-8% improvement:

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
sudo reboot
```

Confirm after reboot:
```bash
uname -r  # should show 6.16.9
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

```bash
sudo apt install -y amdgpu-dkms rocm
```

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
```

Apply:
```bash
sudo systemctl restart ollama
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
rocm-smi  # should show GPU memory in use
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

From your MacBook, SSH into the EVO and launch Claude Code:

```bash
ssh charles@evo-x2.local
cd /opt/ai-runtime
claude
```

Claude Code will use the `ANTHROPIC_API_KEY` from the EVO's environment. All file
access, bash commands, and context are on the EVO — your MacBook is just the terminal.

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
| llama-server segfaults on startup | Kernel 6.17 + ROCm ABI mismatch | Stay on kernel 6.16.9 |
| `HSA_STATUS_ERROR_OUT_OF_RESOURCES` | Missing udev rules or wrong groups | Add 99-amd-kfd.rules, re-add user to render/video |
| GPU only sees small memory slice | GRUB gttsize not applied | Verify `/etc/default/grub` and rerun `update-grub` |
| Slow inference despite GPU | Flash attention disabled | Add `-fa 1` flag if using llama.cpp directly |
| Wi-Fi not working | Ubuntu 25.x kernel issue | Use Ubuntu 24.04 LTS only |

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
