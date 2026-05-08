# Contributing to Agentic SDLC AI Organization

Thank you for considering contributing!

## Development Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -e ".[dev]"`
4. Copy `.env.example` to `.env` and configure
5. Start services: `docker compose up -d` (Postgres + Ollama)

## Code Style
- Python 3.11+
- Follow PEP 8 + type hints (ruff + mypy)
- Use docstrings (Google style)
- Black + isort formatting

## Adding New Agents
1. Create new file in `src/agents/`
2. Define role prompt and tools
3. Register the agent in the supervisor graph
4. Update `docs/agent-roles.md`
5. Add tests

## Pull Request Process
1. Create an issue describing the change
2. Branch from `main` (`feature/xxx` or `agent/xxx`)
3. Make changes + tests
4. Ensure all tests pass
5. Open PR with clear description

## Areas Needing Help
- Review board voting logic
- Advanced tool implementations
- Streamlit / Gradio UI
- Fine-tuning prompts for engineering domains
- Docker optimization

Questions? Open a Discussion or Issue.