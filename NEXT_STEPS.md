# 🚀 Next Steps - Getting Your System Running

This guide helps you go from the implemented code to a fully working system.

---

## ✅ Quick Validation

First, verify all files are present:

```bash
python validate_structure.py
```

You should see all ✅ checkmarks.

---

## 📦 Step 1: Install Dependencies

### Option A: Using pip (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install with dev dependencies
pip install -e ".[dev]"
```

### Option B: Using Make (if available)

```bash
make install
```

### Verify Installation

```bash
pip list | grep -E "langgraph|langchain|pydantic|rich|typer"
```

You should see:
- langgraph >= 0.2.0
- langchain >= 0.3.0
- pydantic >= 2.7.0
- rich >= 13.0.0
- typer >= 0.12.0

---

## 🐳 Step 2: Start Docker Services

### Start Services

```bash
docker compose -f docker/docker-compose.yml up -d
```

### Verify Services Running

```bash
docker ps
```

You should see:
- `ollama/ollama:latest` on port 11434
- `postgres:16` on port 5432

### Troubleshooting

**Docker not installed?**
- Windows: Install Docker Desktop from docker.com
- Mac: Install Docker Desktop from docker.com
- Linux: `sudo apt install docker.io docker-compose`

**Services not starting?**
```bash
# Check logs
docker compose -f docker/docker-compose.yml logs

# Restart services
docker compose -f docker/docker-compose.yml restart
```

---

## 🗄️ Step 3: Initialize Database

```bash
python scripts/setup_db.py
```

**Expected output:**
```
Agentic SDLC - Database Setup
Database URL: postgresql://agentic:agentic@localhost:5432/agentic_sdlc
Creating database schema...
✅ Database initialized successfully!
```

**Troubleshooting:**
- ❌ Connection refused: Docker Postgres not running
- ❌ Authentication failed: Check .env.example vs your .env

---

## 🤖 Step 4: Pull Ollama Models

This downloads the AI models (may take 5-10 minutes):

```bash
python scripts/pull_models.py
```

**Expected output:**
```
Agentic SDLC - Model Setup
Models to pull:
  • llama3.1:8b-instruct-q4_K_M

Pulling model: llama3.1:8b-instruct-q4_K_M
✓ Successfully pulled llama3.1:8b-instruct-q4_K_M

Results:
  Successfully pulled: 1/1
✅ All models ready!
```

**Troubleshooting:**
- ❌ Ollama not found: Install from ollama.ai or ensure Docker Ollama is running
- ⚠️ Slow download: Large models (4-8GB), need good internet

**Alternative models:**
Edit `.env` to try smaller/larger models:
```env
# Faster but less capable
OLLAMA_MODEL=llama3.1:7b-instruct-q4_K_M

# Slower but more capable
OLLAMA_MODEL=qwen2.5:32b-instruct-q4_K_M
```

---

## 🏥 Step 5: Health Check

Verify everything is working:

```bash
python scripts/health_check.py
```

**Expected output:**
```
Agentic SDLC - System Health Check

┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Component         ┃ Status      ┃ Details               ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ Docker Containers │ ✓ Running   │ ollama, postgres      │
│ Ollama API        │ ✓ Accessible│ http://localhost:11434│
│ PostgreSQL        │ ✓ Connected │ localhost:5432/...    │
│ Python Deps       │ ✓ Installed │ All installed         │
└───────────────────┴─────────────┴───────────────────────┘

✅ All systems operational!

You're ready to run examples:
  python examples/01_basic_requirement.py
```

**If any component shows ✗:**
- Docker Containers: `docker compose up -d`
- Ollama API: Check Docker or local Ollama service
- PostgreSQL: Check Docker and connection string in `.env`
- Python Deps: Run `pip install -e ".[dev]"` again

---

## 🎯 Step 6: Run Your First Example

### Example 1: Basic Requirements Workflow

```bash
python examples/01_basic_requirement.py
```

**What it does:**
1. Submits an objective to the system
2. Program Manager routes to Requirements Agent
3. Requirements Agent develops 3 requirements
4. Outputs structured requirements

**Expected runtime:** 30-90 seconds (depends on model and hardware)

**Expected output:**
```
═══ Example 01: Basic Requirement Workflow ═══

Objective: Build a web application for tracking personal fitness goals...

Building supervisor graph...
Starting workflow execution...

[program_manager] Received objective...
[requirements_agent] Developed 3 initial requirements

═══ Results ═══

Final Phase: requirements
Requirements Developed:

  REQ-001: The system shall accept user input...
    Category: functional
    Priority: critical
    Verification: test

  REQ-002: The system shall maintain persistent state...
    Category: non-functional
    Priority: high
    Verification: test

  REQ-003: The system shall provide human approval gates...
    Category: functional
    Priority: high
    Verification: demonstration

✅ Example complete!
```

### Example 2: Architecture Review Board

```bash
python examples/02_review_board.py
```

**What it does:**
1. Starts with predefined requirements
2. Architecture Agent develops architecture
3. Architecture Review Board evaluates
4. Shows voting and decision-making

**Expected output:**
```
═══ Example 02: Architecture Review Board ═══

Running Architecture Agent...
✓ Architecture developed

Architecture Overview:
  Multi-agent orchestration system with persistent state

Components:
  • Supervisor Graph: Coordinate agents...
  • Specialist Agents: Domain-specific work...
  • Review Boards: Governance and approval...
  • Persistence Layer: State management...

Convening Architecture Review Board...

═══ Board Decision ═══

Decision: APPROVE

Votes:
  • chief_engineer: approve
  • architecture_agent: approve
  • requirements_agent: approve

Rationale:
chief_engineer: Meets all technical requirements...
architecture_agent: All components properly defined...
requirements_agent: Complete traceability established

✅ Example complete!
```

### Example 3: Human-in-the-Loop

```bash
python examples/03_hitl_workflow.py
```

**What it does:**
1. Demonstrates approval requests
2. Shows interactive prompts
3. Collects human feedback

**This is interactive** - you'll be prompted for input.

---

## 🎨 Step 7: Try the CLI

### Run with an objective

```bash
python -m src.cli.main run "Build a REST API for user management"
```

### Check configuration

```bash
python -m src.cli.main config
```

### Initialize database (alternative to script)

```bash
python -m src.cli.main init-db
```

### Get help

```bash
python -m src.cli.main --help
```

---

## 🧪 Step 8: Run Tests

### Run all tests

```bash
pytest
```

### Run with coverage

```bash
pytest --cov=src --cov-report=html
```

### View coverage report

```bash
# On Windows
start htmlcov/index.html

# On Mac
open htmlcov/index.html

# On Linux
xdg-open htmlcov/index.html
```

---

## 🔧 Step 9: Configure for Your Needs

### Create your .env file

```bash
cp .env.example .env
```

### Edit settings

Common customizations in `.env`:

```env
# Use a different model
OLLAMA_MODEL=qwen2.5:14b-instruct-q4_K_M

# Disable HITL for automated testing
ENABLE_HITL=false

# Adjust timeouts
DEFAULT_TIMEOUT_SECONDS=180

# Enable tracing (requires LangSmith account)
ENABLE_TRACING=true
LANGSMITH_API_KEY=your_key_here
```

---

## 📊 Step 10: Monitor and Debug

### View logs

Logs are written to `data/logs/agentic_sdlc.log`

```bash
tail -f data/logs/agentic_sdlc.log
```

### Check database

```bash
# Connect to database
psql postgresql://agentic:agentic@localhost:5432/agentic_sdlc

# List checkpoints
SELECT * FROM langgraph_checkpoints LIMIT 10;
```

### Use LangSmith (Optional)

1. Sign up at smith.langchain.com
2. Get API key
3. Set in `.env`:
   ```env
   ENABLE_TRACING=true
   LANGSMITH_API_KEY=your_key
   ```
4. Run examples and view traces in LangSmith UI

---

## 🚀 Step 11: Start Developing

### Add a new agent

See `docs/development-guide.md` for complete tutorial.

Quick version:
1. Create `src/agents/your_agent.py`
2. Inherit from `BaseAgent`
3. Implement `get_system_prompt()` and `process()`
4. Add to supervisor graph
5. Write tests

### Add a new tool

1. Create `src/tools/your_tool.py`
2. Implement functions with clear docstrings
3. Add to `src/tools/__init__.py`
4. Use in agents

### Add a new example

1. Create `examples/04_your_example.py`
2. Import agents and state
3. Demonstrate specific functionality
4. Add clear output and explanations

---

## 📚 Additional Resources

### Documentation
- `README.md` - Project overview
- `docs/development-guide.md` - Complete developer guide
- `docs/testing-strategy.md` - Testing approach
- `docs/ARCHITECTURE_DECISIONS.md` - Design decisions
- `CONTRIBUTING.md` - How to contribute

### Community
- GitHub Issues - Bug reports and feature requests
- GitHub Discussions - Questions and ideas
- Pull Requests - Code contributions

---

## ❓ Common Issues

### Issue: "ModuleNotFoundError: No module named 'langgraph'"

**Solution:** Dependencies not installed
```bash
pip install -e ".[dev]"
```

### Issue: "Connection refused" when connecting to Postgres

**Solution:** Docker not running or wrong URL
```bash
docker compose -f docker/docker-compose.yml up -d
# Check .env has: POSTGRES_URL=postgresql://agentic:agentic@localhost:5432/agentic_sdlc
```

### Issue: "Ollama model not found"

**Solution:** Model not pulled
```bash
python scripts/pull_models.py
# Or manually: ollama pull llama3.1:8b-instruct-q4_K_M
```

### Issue: Examples run but produce poor output

**Solution:** Model too small or prompts need tuning
```bash
# Try a larger model in .env
OLLAMA_MODEL=qwen2.5:14b-instruct-q4_K_M
```

### Issue: Out of memory errors

**Solution:** Model too large for your GPU
```bash
# Use smaller model
OLLAMA_MODEL=llama3.1:7b-instruct-q4_K_M
# Or use CPU (slower)
```

### Issue: Tests fail with "fixture not found"

**Solution:** Tests directory not in Python path
```bash
# Run from project root
cd /path/to/agentic-sdlc-ai
pytest
```

---

## ✅ Success Checklist

- [ ] All dependencies installed (`pip list` shows langgraph, etc.)
- [ ] Docker services running (`docker ps` shows ollama, postgres)
- [ ] Database initialized (`scripts/setup_db.py` succeeded)
- [ ] Models downloaded (`scripts/pull_models.py` succeeded)
- [ ] Health check passes (`scripts/health_check.py` shows all ✓)
- [ ] Example 1 runs successfully
- [ ] Tests pass (`pytest` succeeds)
- [ ] Can import modules (`python -c "from src.agents import RequirementsAgent"`)

---

## 🎉 You're Ready!

If all steps above succeeded, you now have:
- ✅ Fully working multi-agent system
- ✅ Running infrastructure (Docker, Postgres, Ollama)
- ✅ Working examples
- ✅ Test suite
- ✅ CLI tools
- ✅ Development environment

**Next:**
1. Read `docs/development-guide.md` to understand the architecture
2. Experiment with the examples
3. Try modifying prompts or agent logic
4. Add your own agents or tools
5. Contribute back to the project!

---

## 💡 Pro Tips

1. **Start small**: Run examples before modifying code
2. **Read the logs**: `data/logs/agentic_sdlc.log` is your friend
3. **Use health check often**: `python scripts/health_check.py`
4. **Experiment with models**: Different models have different strengths
5. **Write tests**: Makes development much faster
6. **Use the CLI**: `python -m src.cli.main --help`
7. **Join discussions**: Ask questions, share learnings

---

**Questions?** Open a GitHub Discussion or Issue.

**Found a bug?** Open an Issue with reproduction steps.

**Have an improvement?** Open a Pull Request!

**Happy Engineering! 🚀**
