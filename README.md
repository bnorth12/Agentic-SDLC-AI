# Agentic SDLC AI Organization

A self-hosted, persistent multi-agent engineering platform for orchestrating the full Systems/Software Development Lifecycle (SDLC) with **LangGraph** and **Ollama**.

## Vision

Build an engineering-grade AI organization where specialist agents collaborate under governance to plan, design, implement, verify, and maintain complex systems.

## Key Features

- Hierarchical LangGraph orchestration with supervisor agents
- Specialist SDLC agent roles (requirements, architecture, development, V&V, CM, safety/security)
- Shared state and persistent checkpoints for long-running work
- Human-in-the-loop (HITL) approval and escalation gates
- Review board subgraphs for design, safety, and release governance
- Self-hosted model execution using Ollama (with optional vLLM-compatible backends)

## Tech Stack

- Python 3.11+
- LangGraph / LangChain
- Pydantic v2 for typed state models
- PostgreSQL for persistence and retrieval workflows
- Docker / Docker Compose for local platform services

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -c "from src.state.schema import AgentState; print(AgentState())"
```

Then follow [`docs/getting-started.md`](docs/getting-started.md) for first graph execution.

## Hardware Tiers

| Tier | Typical Use | Example |
| --- | --- | --- |
| Minimal | Single-user prototyping | 8-core CPU, 32 GB RAM, no GPU or small 8 GB VRAM GPU |
| Recommended | Daily development | 12-16 core CPU, 64 GB RAM, 24 GB VRAM GPU |
| Production | Multi-user concurrent workflows | 32+ core CPU, 128+ GB RAM, 2x+ GPUs (48-80 GB VRAM total) |

Full sizing guidance: [`docs/hardware-requirements.md`](docs/hardware-requirements.md)

## Documentation

- [Getting Started](docs/getting-started.md)
- [Architecture](docs/architecture.md)
- [Agent Roles](docs/agent-roles.md)
- [Hardware Requirements](docs/hardware-requirements.md)
- [Roadmap](docs/roadmap.md)
- [Contributing](CONTRIBUTING.md)

## Development Status

This repository is the initial scaffold for rapid iteration and planning of a full agentic SDLC platform.
