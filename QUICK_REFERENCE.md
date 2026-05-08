# Quick Reference Guide

## 🚀 Getting Started

### First Time Setup
```bash
# Option 1: Automated (recommended)
make setup

# Option 2: Manual
pip install -e ".[dev]"
docker compose -f docker/docker-compose.yml up -d
python scripts/setup_db.py
python scripts/pull_models.py
```

### Verify Installation
```bash
python scripts/health_check.py
```

---

## 📋 Common Commands

### Makefile Commands
```bash
make help          # Show all available commands
make setup         # Complete first-time setup
make install       # Install Python dependencies only
make docker-up     # Start Docker services
make docker-down   # Stop Docker services
make test          # Run tests
make test-cov      # Run tests with coverage
make lint          # Run linters (ruff, mypy)
make format        # Format code
make health        # Check system health
make run-example   # Run basic example
make clean         # Clean build artifacts
```

### Python Scripts
```bash
# Setup and health
python scripts/setup_db.py        # Initialize database
python scripts/pull_models.py     # Download Ollama models
python scripts/health_check.py    # Verify system is ready

# Examples
python examples/01_basic_requirement.py    # Requirements workflow
python examples/02_review_board.py         # Architecture review board
python examples/03_hitl_workflow.py        # Human-in-the-loop demo

# CLI
python -m src.cli.main --help                      # Show CLI help
python -m src.cli.main run "Your objective"        # Run workflow
python -m src.cli.main init-db                     # Initialize DB
python -m src.cli.main config                      # Show configuration
python -m src.cli.main version                     # Show version
```

### Docker Commands
```bash
# Start services
docker compose -f docker/docker-compose.yml up -d

# Stop services
docker compose -f docker/docker-compose.yml down

# View logs
docker compose -f docker/docker-compose.yml logs -f

# Restart services
docker compose -f docker/docker-compose.yml restart
```

### Testing Commands
```bash
# All tests
pytest

# Specific test file
pytest tests/test_starter_modules.py

# With verbose output
pytest -v

# With coverage
pytest --cov=src --cov-report=html

# Unit tests only
pytest tests/unit/

# Slow tests (E2E)
pytest --slow

# Watch mode (requires pytest-watch)
ptw
```

---

## 🔧 Development Workflow

### Starting Development
```bash
# 1. Pull latest code
git pull origin main

# 2. Create feature branch
git checkout -b feature/my-feature

# 3. Ensure environment is ready
make health

# 4. Make your changes
# ...

# 5. Format code
make format

# 6. Run tests
make test

# 7. Commit and push
git add .
git commit -m "Add my feature"
git push origin feature/my-feature
```

### Adding a New Agent
```bash
# 1. Create agent file
touch src/agents/my_agent.py

# 2. Implement agent (see docs/development-guide.md)
# ...

# 3. Add to __init__.py
# Edit src/agents/__init__.py

# 4. Register in supervisor
# Edit src/graphs/supervisor.py

# 5. Add tests
touch tests/unit/test_my_agent.py

# 6. Run tests
pytest tests/unit/test_my_agent.py -v
```

### Creating a New Board
```bash
# 1. Create board file
touch src/boards/my_board.py

# 2. Implement board (inherit from BaseReviewBoard)
# ...

# 3. Add to __init__.py
# Edit src/boards/__init__.py

# 4. Register in supervisor
# Edit src/graphs/supervisor.py

# 5. Test
pytest tests/integration/ -v
```

---

## 🐛 Debugging

### View Logs
```bash
# Application logs
tail -f data/logs/agentic_sdlc.log

# Docker logs
docker compose -f docker/docker-compose.yml logs -f ollama
docker compose -f docker/docker-compose.yml logs -f postgres
```

### Database Access
```bash
# Connect to PostgreSQL
docker exec -it agentic-sdlc-ai-postgres-1 psql -U agentic -d agentic_sdlc

# View checkpoints
SELECT * FROM langgraph_checkpoints LIMIT 10;
```

### Python Interactive
```bash
# Start IPython with project context
python -m IPython

# In IPython:
from src.state import AgentState
from src.agents import RequirementsAgent
from src.graphs import build_supervisor_graph

state = AgentState(objective="Test")
graph = build_supervisor_graph()
# ... interact with objects
```

### Enable Tracing
```bash
# Edit .env
ENABLE_TRACING=true
LANGSMITH_API_KEY=your_key_here

# Run with tracing
python examples/01_basic_requirement.py
# View at https://smith.langchain.com/
```

---

## 📦 Dependency Management

### Install Dependencies
```bash
# Core dependencies
pip install -e .

# With development tools
pip install -e ".[dev]"

# With UI tools (future)
pip install -e ".[ui]"
```

### Update Dependencies
```bash
# Show outdated packages
pip list --outdated

# Update specific package
pip install --upgrade langgraph

# Regenerate requirements (if using)
pip freeze > requirements.txt
```

### Virtual Environment
```bash
# Create venv
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Deactivate
deactivate
```

---

## 🔍 Troubleshooting

### Docker Issues
```bash
# Docker not running
docker ps  # If fails, start Docker Desktop

# Port conflicts
docker compose -f docker/docker-compose.yml down
# Edit docker-compose.yml to change ports

# Reset everything
docker compose -f docker/docker-compose.yml down -v
docker compose -f docker/docker-compose.yml up -d
python scripts/setup_db.py
```

### Database Issues
```bash
# Cannot connect to database
python scripts/health_check.py  # Check status
docker compose -f docker/docker-compose.yml restart postgres

# Reset database
python scripts/setup_db.py
```

### Ollama Issues
```bash
# Ollama not responding
docker compose -f docker/docker-compose.yml restart ollama

# Re-pull models
python scripts/pull_models.py

# Check models
docker exec agentic-sdlc-ai-ollama-1 ollama list
```

### Import Errors
```bash
# Cannot import src
pip install -e .

# Module not found
pip install -e ".[dev]"
```

### Permission Issues (Linux/Mac)
```bash
# Cannot write to data/
sudo chown -R $USER:$USER data/

# Docker permission denied
sudo usermod -aG docker $USER
# Log out and back in
```

---

## 📊 Monitoring

### System Resources
```bash
# Docker stats
docker stats

# Container resource usage
docker compose -f docker/docker-compose.yml top
```

### Application Metrics
```bash
# Check database size
docker exec agentic-sdlc-ai-postgres-1 \
  psql -U agentic -d agentic_sdlc \
  -c "SELECT pg_size_pretty(pg_database_size('agentic_sdlc'));"

# Count checkpoints
docker exec agentic-sdlc-ai-postgres-1 \
  psql -U agentic -d agentic_sdlc \
  -c "SELECT COUNT(*) FROM langgraph_checkpoints;"
```

---

## 🎯 Common Tasks

### Run a Simple Workflow
```bash
python -m src.cli.main run "Build a REST API for task management" --max-iter 20
```

### Test a Single Agent
```python
python -c "
from src.agents import RequirementsAgent
from src.state import AgentState

agent = RequirementsAgent()
state = AgentState(objective='Build a calculator app')
updates = agent.process(state)
print(updates)
"
```

### Check Configuration
```bash
python -m src.cli.main config
```

### Export Requirements
```python
python -c "
from src.graphs import build_supervisor_graph
from src.state import AgentState
import json

graph = build_supervisor_graph()
result = graph.invoke(AgentState(objective='Build an app'))

# Export requirements to JSON
with open('requirements.json', 'w') as f:
    reqs = {k: v.dict() for k, v in result['requirements'].items()}
    json.dump(reqs, f, indent=2, default=str)

print('Exported to requirements.json')
"
```

---

## 🌐 Environment Variables

### Key Settings
```bash
# Model configuration
export OLLAMA_MODEL=llama3.1:8b-instruct-q4_K_M

# Enable/disable HITL
export ENABLE_HITL=true

# Adjust timeouts
export DEFAULT_TIMEOUT_SECONDS=120
export MAX_ITERATIONS=25

# Database
export POSTGRES_URL=postgresql://user:pass@localhost:5432/db

# Tracing
export ENABLE_TRACING=true
export LANGSMITH_API_KEY=your_key
```

### Load from .env
```bash
# Copy example
cp .env.example .env

# Edit .env
nano .env  # or your editor

# Load in shell
set -a; source .env; set +a
```

---

## 🎓 Learning Resources

### Documentation
```bash
# Read docs
cat docs/development-guide.md | less
cat docs/testing-strategy.md | less
cat docs/ARCHITECTURE_DECISIONS.md | less

# Generate HTML docs (if using Sphinx in future)
# make docs
# open docs/_build/html/index.html
```

### Code Examples
```bash
# Study examples
cat examples/01_basic_requirement.py
cat examples/02_review_board.py
cat examples/03_hitl_workflow.py

# Run with modifications
# Copy and edit an example, then run it
```

---

## 🔐 Security Notes

### Sensitive Data
- Never commit `.env` file
- Keep `LANGSMITH_API_KEY` secret
- Database credentials should be changed in production
- Model data stays local (Ollama)

### Production Checklist
- [ ] Change default database password
- [ ] Use strong credentials
- [ ] Enable SSL/TLS for Postgres
- [ ] Restrict network access
- [ ] Regular backups
- [ ] Monitor logs for anomalies

---

## 💾 Backup and Restore

### Backup Database
```bash
# Backup
docker exec agentic-sdlc-ai-postgres-1 \
  pg_dump -U agentic agentic_sdlc > backup.sql

# Restore
cat backup.sql | docker exec -i agentic-sdlc-ai-postgres-1 \
  psql -U agentic -d agentic_sdlc
```

### Backup Ollama Models
```bash
# Models stored in Docker volume
docker run --rm -v agentic-sdlc-ai_ollama_data:/data \
  -v $(pwd):/backup alpine tar czf /backup/ollama-backup.tar.gz /data
```

---

## 📞 Getting Help

### Documentation
- `README.md` - Project overview
- `docs/getting-started.md` - Setup guide
- `docs/development-guide.md` - Development guide
- `docs/testing-strategy.md` - Testing guide
- `CONTRIBUTING.md` - How to contribute

### Community
- GitHub Discussions - Ask questions
- GitHub Issues - Report bugs
- Pull Requests - Contribute code

### Logs and Debugging
- Check `data/logs/agentic_sdlc.log`
- Run `python scripts/health_check.py`
- Enable tracing for detailed execution logs

---

**Quick Start**: `make setup && python examples/01_basic_requirement.py`
