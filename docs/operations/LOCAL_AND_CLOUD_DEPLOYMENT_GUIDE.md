# Local Hardware and Cloud Deployment Guide

This guide is for future bring-up after you have hardware available.
It covers:

- Ubuntu post-install setup
- Development and testing deployment of this repository
- Promotion path from test environment to production candidate
- Cloud rental recommendations and what instance type to rent

## 0. One-Command Bootstrap (Local and Cloud)

Yes, you can use the same installer command pattern for both local hardware and rented Ubuntu servers.
Use the same script and switch only the `--target` or optional flags.

From repository root:

```bash
bash scripts/bootstrap_ubuntu.sh --target local
```

For rented Ubuntu server:

```bash
bash scripts/bootstrap_ubuntu.sh --target cloud
```

Useful options:

- `--runtime postgres-only` (recommended) or `--runtime full-compose`
- `--install-nvidia-drivers true` for fresh local hardware where drivers are not installed yet
- `--run-tests true` to run full validation at the end

Examples:

```bash
bash scripts/bootstrap_ubuntu.sh --target local --install-nvidia-drivers true --run-tests true
bash scripts/bootstrap_ubuntu.sh --target cloud --runtime postgres-only --run-tests true
```

### 0.1 Remote One-Liner (No Manual Clone)

If you want to run the installer without cloning first, use:

```bash
curl -fsSL https://raw.githubusercontent.com/bnorth12/Agentic-SDLC-AI/main/scripts/bootstrap_ubuntu.sh | \
  bash -s -- --target cloud --workdir "$HOME/agentic-sdlc-ai"
```

For local hardware:

```bash
curl -fsSL https://raw.githubusercontent.com/bnorth12/Agentic-SDLC-AI/main/scripts/bootstrap_ubuntu.sh | \
  bash -s -- --target local --install-nvidia-drivers true --workdir "$HOME/agentic-sdlc-ai"
```

Notes:

- This uses the same bootstrap script as local repo execution.
- In remote mode, the script auto-clones the repository into `--workdir`.
- If `--workdir` is non-empty, the script exits to avoid overwriting files.

## 1. Prerequisites

- Ubuntu 22.04 LTS or 24.04 LTS installed
- Sudo access
- Stable internet connection
- GitHub access to this repository
- Optional but recommended for local model inference: NVIDIA GPU

## 2. Hardware Sizing Profiles

Use this as a quick decision table.

| Profile | Use Case | CPU | RAM | GPU | Storage |
| --- | --- | ---: | ---: | ---: | ---: |
| Minimum Dev | Basic integration/testing, light local inference | 8 cores | 32 GB | 8-12 GB VRAM | 500 GB SSD |
| Recommended Dev/Test | Daily development and repeatable testing | 12+ cores | 64+ GB | 24 GB VRAM | 1 TB NVMe |
| Production Candidate | Multi-user or longer runs | 16+ cores | 128+ GB | 1-2 x 24+ GB VRAM | 2 TB NVMe |

For background reference, see [docs/hardware-requirements.md](docs/hardware-requirements.md).

## 3. Ubuntu Host Preparation (After OS Install)

If you use Section 0 bootstrap script, this section is executed automatically.

Run these commands once.

```bash
sudo apt update && sudo apt -y upgrade
sudo apt -y install git curl wget make build-essential ca-certificates gnupg lsb-release \
  python3 python3-venv python3-pip python3-dev
```

### 3.1 Install Docker Engine + Compose Plugin

```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo $VERSION_CODENAME) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
newgrp docker
```

Validate:

```bash
docker --version
docker compose version
```

### 3.2 Optional: NVIDIA Driver + CUDA Toolkit (GPU Hosts)

If you have NVIDIA hardware:

```bash
ubuntu-drivers devices
sudo ubuntu-drivers autoinstall
sudo reboot
```

After reboot:

```bash
nvidia-smi
```

If `nvidia-smi` works, GPU drivers are ready.

## 4. Clone and Configure the Repository

```bash
git clone https://github.com/bnorth12/Agentic-SDLC-AI.git
cd Agentic-SDLC-AI
cp .env.example .env
```

Edit `.env` and confirm at least these values:

- `APP_ENV=development`
- `OLLAMA_BASE_URL=http://localhost:11434`
- `POSTGRES_URL=postgresql://agentic:agentic@localhost:5432/agentic_sdlc`

Environment variable definitions are in [src/config/settings.py](src/config/settings.py).

## 5. Choose a Runtime Pattern

Use one of these two patterns.

### Pattern A (Recommended for Linux GPU): Ollama Native + Postgres in Docker

This keeps model serving on host GPU and persistence in containers.

1. Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

1. Start Postgres only:

```bash
docker compose -f docker/docker-compose.yml up -d postgres
```

1. Start Ollama service and pull model:

```bash
sudo systemctl enable --now ollama
ollama pull llama3.1:8b-instruct-q4_K_M
```

### Pattern B: Full Docker Compose

Use when you want all services from one compose file.

```bash
docker compose -f docker/docker-compose.yml up -d
```

Note: For GPU acceleration in containerized Ollama, you may need NVIDIA container runtime configuration.

## 6. Python Environment and Project Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

Initialize and verify:

```bash
python scripts/setup_db.py
python scripts/pull_models.py
python scripts/health_check.py
```

You can also run:

```bash
make setup
```

(Uses targets in [Makefile](Makefile).)

## 7. Development and Testing Workflow (Test Environment)

From repo root:

```bash
source .venv/bin/activate
make health
make test
make lint
python examples/01_basic_requirement.py
```

Recommended Sprint validation command:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## 8. Promote Test Environment Toward Production

When this host starts serving production-like workloads, apply these controls.

### 8.1 Environment Profiles

- Keep separate `.env` files per stage (dev/test/prod)
- Set `APP_ENV=production` in production candidate
- Use stronger DB credentials than compose defaults

### 8.2 Service Hardening

- Run behind reverse proxy (Nginx or Caddy)
- Restrict inbound ports with UFW (allow only SSH + required app ports)
- Configure automated backup for Postgres volume
- Add systemd restart policies and health checks

### 8.3 Operational Practices

- Pin model and dependency versions before release windows
- Run test suite before each deploy
- Keep rollback path: previous git tag + DB backup
- Track key metrics with dashboard service and logs

## 9. Cloud Rental Recommendations (Interim Environment)

If local hardware is delayed, rent GPU compute now and keep the same workflow.

### 9.1 What to Rent

For this project, rent a **GPU VM** (not serverless inference) so you can run Docker, Ollama, Postgres, tests, and scripts end-to-end.

Recommended baseline for development/testing:

- 1 x NVIDIA 24 GB GPU (RTX 4090, L4, A10, or L40S)
- 8-16 vCPU
- 32-64 GB RAM
- 200-500 GB NVMe SSD
- Ubuntu 22.04/24.04

### 9.2 Provider Shortlist

1. RunPod (good price/performance for dev)

- Best for: fast start, hourly GPU cost control
- Suggested instance: RTX 4090 24 GB (or L40S if available)
- Rent: Secure Cloud GPU VM + persistent volume

1. Lambda Cloud (simple dedicated GPU VMs)

- Best for: stable long-lived VM workflows
- Suggested instance: 1 x A10 or 1 x 4090 class GPU
- Rent: on-demand GPU VM with 200+ GB storage

1. AWS EC2 (enterprise controls and networking)

- Best for: future production posture, IAM, VPC, backup controls
- Suggested instance families: g5 or g6
- Rent: GPU EC2 + gp3 EBS + security group + snapshot plan

### 9.3 Cost-Control Tips

- Stop VMs when idle (or use auto-shutdown cron)
- Start with one 24 GB GPU; scale only if queue latency requires it
- Use quantized models first (Q4/Q5)
- Keep persistent disk, replace only compute node if needed

## 10. Quick Cloud Bring-Up Checklist

1. Create Ubuntu GPU VM
1. Open ports minimally:

- SSH (22) from your IP only
- Optional app ports (8501 dashboard, 11434 Ollama) from trusted CIDR only

1. Follow Sections 3 through 7 in this guide
1. Confirm with:

```bash
python scripts/health_check.py
python -m unittest discover -s tests -p "test_*.py"
```

1. Snapshot disk after successful setup

## 11. Suggested Path For You

Given your timeline:

1. Use cloud GPU VM now as test environment
1. Keep all setup scripted from this guide
1. Re-run identical steps on local hardware later
1. After local bring-up is stable, decide whether cloud remains backup or production candidate

This minimizes rework and keeps dev/test/prod setup as close as possible.
