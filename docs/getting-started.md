# Getting Started

## 1. Prerequisites

- Python 3.11+
- Docker + Docker Compose (optional but recommended)
- Ollama installed (if running model host directly)

## 2. Clone and Setup

```bash
git clone <your-fork-or-repo-url>
cd Agentic-SDLC-AI
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## 3. Start Platform Services (Optional)

```bash
docker compose -f docker/docker-compose.yml up -d
```

## 4. Validate Starter Modules

```bash
python -c "from src.state.schema import AgentState; print(AgentState())"
python -c "from src.graphs.supervisor import build_supervisor_graph; print(build_supervisor_graph())"
```

## 5. Next Steps

- Define first agent nodes under `src/agents/`
- Expand supervisor routing logic in `src/graphs/supervisor.py`
- Add persistent checkpoint and vector-retrieval integrations
