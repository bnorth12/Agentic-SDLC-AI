#!/usr/bin/env bash
set -euo pipefail

TARGET="local"
RUNTIME_PATTERN="postgres-only"
INSTALL_OLLAMA="true"
INSTALL_MODELS="true"
INSTALL_NVIDIA_DRIVERS="false"
RUN_TESTS="false"
MODEL_NAME="llama3.1:8b-instruct-q4_K_M"
REPO_URL="https://github.com/bnorth12/Agentic-SDLC-AI.git"
REPO_BRANCH="main"
WORKDIR="$HOME/agentic-sdlc-ai"

log() {
  echo "[bootstrap] $*"
}

usage() {
  cat <<'EOF'
Usage: bash scripts/bootstrap_ubuntu.sh [options]

Options:
  --target <local|cloud>            Deployment target (default: local)
  --runtime <postgres-only|full-compose>
                                    Runtime pattern (default: postgres-only)
  --install-ollama <true|false>     Install Ollama (default: true)
  --install-models <true|false>     Pull models via scripts/pull_models.py (default: true)
  --model <model-name>              Ollama model to pull directly (default: llama3.1:8b-instruct-q4_K_M)
  --install-nvidia-drivers <true|false>
                                    Install NVIDIA drivers via ubuntu-drivers (default: false)
  --run-tests <true|false>          Run unittest suite at end (default: false)
  --repo-url <url>                  Repository URL for auto-clone mode
  --branch <name>                   Repository branch to clone (default: main)
  --workdir <path>                  Target path for auto-clone mode
  -h, --help                        Show this help

Examples:
  bash scripts/bootstrap_ubuntu.sh
  bash scripts/bootstrap_ubuntu.sh --target cloud --runtime postgres-only
  bash scripts/bootstrap_ubuntu.sh --target local --install-nvidia-drivers true
  curl -fsSL https://raw.githubusercontent.com/bnorth12/Agentic-SDLC-AI/main/scripts/bootstrap_ubuntu.sh | \
    bash -s -- --target cloud --workdir "$HOME/agentic-sdlc-ai"
EOF
}

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    log "Missing required command: $1"
    exit 1
  fi
}

run_compose() {
  if docker info >/dev/null 2>&1; then
    docker compose -f docker/docker-compose.yml "$@"
  else
    sudo docker compose -f docker/docker-compose.yml "$@"
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      TARGET="$2"
      shift 2
      ;;
    --runtime)
      RUNTIME_PATTERN="$2"
      shift 2
      ;;
    --install-ollama)
      INSTALL_OLLAMA="$2"
      shift 2
      ;;
    --install-models)
      INSTALL_MODELS="$2"
      shift 2
      ;;
    --model)
      MODEL_NAME="$2"
      shift 2
      ;;
    --install-nvidia-drivers)
      INSTALL_NVIDIA_DRIVERS="$2"
      shift 2
      ;;
    --run-tests)
      RUN_TESTS="$2"
      shift 2
      ;;
    --repo-url)
      REPO_URL="$2"
      shift 2
      ;;
    --branch)
      REPO_BRANCH="$2"
      shift 2
      ;;
    --workdir)
      WORKDIR="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      log "Unknown argument: $1"
      usage
      exit 1
      ;;
  esac
done

if [[ "$TARGET" != "local" && "$TARGET" != "cloud" ]]; then
  log "--target must be local or cloud"
  exit 1
fi

if [[ "$RUNTIME_PATTERN" != "postgres-only" && "$RUNTIME_PATTERN" != "full-compose" ]]; then
  log "--runtime must be postgres-only or full-compose"
  exit 1
fi

if [[ ! -f /etc/os-release ]]; then
  log "Unsupported OS: /etc/os-release not found"
  exit 1
fi

# shellcheck disable=SC1091
source /etc/os-release
if [[ "${ID:-}" != "ubuntu" ]]; then
  log "Unsupported OS: this script currently supports Ubuntu only"
  exit 1
fi

log "Target=$TARGET Runtime=$RUNTIME_PATTERN"

require_cmd sudo
require_cmd curl
require_cmd git

REPO_DIR=""
if [[ -f "pyproject.toml" && -d "scripts" ]]; then
  REPO_DIR="$PWD"
  log "Using existing repository checkout at $REPO_DIR"
else
  if [[ -e "$WORKDIR" && -n "$(find "$WORKDIR" -mindepth 1 -maxdepth 1 2>/dev/null | head -n 1)" ]]; then
    log "Workdir is not empty: $WORKDIR"
    log "Choose an empty --workdir path or run from repository root."
    exit 1
  fi

  log "Cloning repository into $WORKDIR"
  mkdir -p "$WORKDIR"
  git clone --depth 1 --branch "$REPO_BRANCH" "$REPO_URL" "$WORKDIR"
  REPO_DIR="$WORKDIR"
fi

cd "$REPO_DIR"

log "Updating apt package index"
sudo apt update
sudo apt -y upgrade

log "Installing base packages"
sudo apt -y install \
  git curl wget make build-essential ca-certificates gnupg lsb-release \
  python3 python3-venv python3-pip python3-dev

log "Installing Docker Engine and compose plugin"
sudo install -m 0755 -d /etc/apt/keyrings
if [[ ! -f /etc/apt/keyrings/docker.gpg ]]; then
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
fi
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu ${VERSION_CODENAME} stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list >/dev/null

sudo apt update
sudo apt -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

if ! groups "$USER" | grep -q '\bdocker\b'; then
  log "Adding $USER to docker group (new login session required to fully apply)"
  sudo usermod -aG docker "$USER"
fi

sudo systemctl enable --now docker

if [[ "$INSTALL_NVIDIA_DRIVERS" == "true" ]]; then
  log "Installing NVIDIA drivers via ubuntu-drivers"
  sudo apt -y install ubuntu-drivers-common
  sudo ubuntu-drivers autoinstall || true
  log "NVIDIA drivers installation requested. Reboot may be required before GPU workloads."
fi

if [[ ! -f .env ]]; then
  log "Creating .env from .env.example"
  cp .env.example .env
else
  log ".env already exists, leaving as-is"
fi

if [[ "$INSTALL_OLLAMA" == "true" ]]; then
  if ! command -v ollama >/dev/null 2>&1; then
    log "Installing Ollama"
    curl -fsSL https://ollama.com/install.sh | sh
  else
    log "Ollama already installed"
  fi
  sudo systemctl enable --now ollama || true

  if [[ "$INSTALL_MODELS" == "true" ]]; then
    log "Pulling model: $MODEL_NAME"
    ollama pull "$MODEL_NAME" || true
  fi
fi

log "Starting container services"
if [[ "$RUNTIME_PATTERN" == "postgres-only" ]]; then
  run_compose up -d postgres
else
  run_compose up -d
fi

log "Setting up Python virtual environment"
if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e ".[dev]"

log "Initializing database"
python scripts/setup_db.py

if [[ "$INSTALL_MODELS" == "true" ]]; then
  log "Running model pull helper script"
  python scripts/pull_models.py || true
fi

log "Running health check"
python scripts/health_check.py

if [[ "$RUN_TESTS" == "true" ]]; then
  log "Running full unit/integration test suite"
  python -m unittest discover -s tests -p "test_*.py"
fi

log "Bootstrap complete"
log "If docker group was just assigned, log out/in before running docker without sudo."
if [[ "$INSTALL_NVIDIA_DRIVERS" == "true" ]]; then
  log "If NVIDIA drivers were newly installed, reboot before GPU validation with nvidia-smi."
fi
