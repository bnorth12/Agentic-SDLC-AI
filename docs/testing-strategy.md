# Testing Strategy

## Test Pyramid

We follow the standard test pyramid with emphasis on fast, reliable tests:

```
         /\
        /E2E\          10% - End-to-end workflow tests
       /------\
      /  Inte  \       30% - Integration tests (agent + graph + state)
     /----------\
    /    Unit    \     60% - Unit tests (individual components)
   /--------------\
```

---

## Unit Tests (60%)

**What to test**:
- Individual agent logic
- State schema validation
- Tool functions
- Utility functions
- Board voting logic

**Characteristics**:
- Fast (<1ms per test)
- No external dependencies
- Mock LLM calls
- Deterministic

**Example**:
```python
# tests/unit/test_base_agent.py

from src.agents import BaseAgent
from src.state.schema import AgentState

def test_agent_escalation_logic():
    \"\"\"Test that agents correctly identify escalation scenarios.\"\"\"

    class TestAgent(BaseAgent):
        def get_system_prompt(self, state): return ""
        def process(self, state): return {}

    agent = TestAgent("test", "Test Role", "MEDIUM")

    # Should escalate on safety issues
    assert agent.should_escalate("Critical safety issue detected", AgentState())

    # Should not escalate on routine matters
    assert not agent.should_escalate("Updated documentation", AgentState())
```

**Run unit tests**:
```bash
pytest tests/unit/ -v
```

---

## Integration Tests (30%)

**What to test**:
- Agent interactions with state
- Graph execution flows
- Board workflows
- Database persistence
- Full agent → state → board cycles

**Characteristics**:
- Moderate speed (100ms - 1s per test)
- May use test database
- Mock or use small local LLMs
- Test real integrations

**Example**:
```python
# tests/integration/test_requirements_workflow.py

from src.agents import RequirementsAgent, ProgramManagerAgent
from src.graphs.supervisor import build_supervisor_graph
from src.state.schema import AgentState, Phase

def test_requirements_workflow():
    \"\"\"Test complete requirements development workflow.\"\"\"

    # Build graph
    graph = build_supervisor_graph()

    # Initial state
    initial_state = AgentState(
        objective="Build a simple calculator app"
    )

    # Execute graph
    config = {"recursion_limit": 10}
    result = graph.invoke(initial_state, config=config)

    # Assertions
    assert result["phase"] in [Phase.REQUIREMENTS, Phase.ARCHITECTURE]
    assert len(result["requirements"]) > 0
    assert any("calculator" in req.text.lower() 
              for req in result["requirements"].values())
```

**Run integration tests**:
```bash
pytest tests/integration/ -v
```

---

## End-to-End Tests (10%)

**What to test**:
- Complete workflows from objective to deliverable
- Multi-phase execution
- Human-in-the-loop flows (mocked)
- Real database and checkpointing
- Error recovery

**Characteristics**:
- Slow (5-30s per test)
- Uses real infrastructure (Docker required)
- May use actual LLMs (or mocked)
- Tests production-like scenarios

**Example**:
```python
# tests/e2e/test_full_workflow.py

import pytest
from src.graphs.supervisor import build_supervisor_graph
from src.state.schema import AgentState, Phase

@pytest.mark.slow
def test_full_requirements_to_architecture():
    \"\"\"Test complete flow from requirements through architecture approval.\"\"\"

    graph = build_supervisor_graph()

    initial_state = AgentState(
        objective="Build a RESTful API for user management"
    )

    config = {"recursion_limit": 25}
    result = graph.invoke(initial_state, config=config)

    # Verify complete workflow
    assert result["phase"] == Phase.ARCHITECTURE
    assert len(result["requirements"]) >= 3
    assert result["architecture"] is not None
    assert len(result["board_results"]) >= 1

    # Verify requirements quality
    reqs = result["requirements"]
    assert any("API" in req.text for req in reqs.values())
    assert any("user" in req.text.lower() for req in reqs.values())

    # Verify architecture addresses requirements
    arch = result["architecture"]
    assert len(arch["components"]) > 0
    assert len(arch["traced_requirements"]) == len(reqs)
```

**Run E2E tests**:
```bash
pytest tests/e2e/ -v --slow
```

---

## Mocking Strategy

### Mocking LLM Calls

**Option 1: Patch the model**
```python
from unittest.mock import Mock, patch

def test_agent_with_mocked_llm():
    with patch('src.agents.base_agent.ChatOllama') as mock_ollama:
        mock_response = Mock()
        mock_response.content = '{"result": "test"}'
        mock_ollama.return_value.invoke.return_value = mock_response

        # Test agent logic
        agent = YourAgent()
        result = agent.process(state)
```

**Option 2: Use test fixtures**
```python
# tests/fixtures/llm_responses.py

REQUIREMENTS_RESPONSE = {
    "REQ-001": {
        "text": "System shall do X",
        "category": "functional",
        "priority": "high"
    }
}
```

### Mocking HITL

```python
from unittest.mock import patch
from src.utils.hitl import ApprovalDecision, ApprovalResponse

def test_with_auto_approval():
    with patch('src.utils.hitl.request_human_approval') as mock_hitl:
        mock_hitl.return_value = ApprovalResponse(
            decision=ApprovalDecision.APPROVE,
            feedback="Auto-approved for testing"
        )

        # Test workflow with approval
```

### Using VCR.py for Recording Real Interactions

```python
import vcr

@vcr.use_cassette('fixtures/vcr_cassettes/requirements_call.yaml')
def test_real_llm_interaction():
    \"\"\"This test records real LLM calls on first run, replays on subsequent runs.\"\"\"
    agent = RequirementsAgent()
    result = agent.process(state)
    assert result is not None
```

---

## Test Fixtures

Create reusable test data:

```python
# tests/fixtures/states.py

from src.state.schema import AgentState, Requirement, Phase

def basic_state():
    return AgentState(
        objective="Test objective"
    )

def state_with_requirements():
    return AgentState(
        objective="Test objective",
        phase=Phase.ARCHITECTURE,
        requirements={
            "REQ-001": Requirement(
                id="REQ-001",
                text="Test requirement",
                category="functional",
                priority="high",
                verification_method="test",
                created_by="test",
            )
        }
    )
```

Use in tests:
```python
from tests.fixtures.states import state_with_requirements

def test_architecture_agent():
    state = state_with_requirements()
    agent = ArchitectureAgent()
    result = agent.process(state)
```

---

## Pytest Configuration

`tests/conftest.py`:

```python
import pytest
from src.utils.logging import setup_logging
from src.config import get_settings

@pytest.fixture(scope="session", autouse=True)
def setup():
    \"\"\"Setup test environment once for entire session.\"\"\"
    setup_logging()

@pytest.fixture
def settings():
    \"\"\"Provide test settings.\"\"\"
    return get_settings()

@pytest.fixture
def clean_state():
    \"\"\"Provide a fresh AgentState for each test.\"\"\"
    from src.state.schema import AgentState
    return AgentState(objective="Test objective")

def pytest_addoption(parser):
    parser.addoption(
        "--slow", action="store_true", default=False, help="run slow tests"
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")

def pytest_collection_modifyitems(config, items):
    if config.getoption("--slow"):
        return
    skip_slow = pytest.mark.skip(reason="need --slow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
```

---

## CI/CD Pipeline

`.github/workflows/ci.yml`:

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_DB: test_db
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -e ".[dev]"

      - name: Lint
        run: |
          ruff check src tests
          mypy src

      - name: Unit tests
        run: pytest tests/unit/ -v

      - name: Integration tests
        run: pytest tests/integration/ -v
        env:
          POSTGRES_URL: postgresql://test:test@localhost:5432/test_db

      - name: Coverage report
        run: pytest --cov=src --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v4
```

---

## Coverage Goals

**Target Coverage**: 80%+ overall

**Breakdown**:
- Core agents: 90%+
- State management: 95%+
- Tools: 85%+
- Boards: 80%+
- CLI: 70%+ (interactive components harder to test)

**Generate coverage report**:
```bash
pytest --cov=src --cov-report=html
open htmlcov/index.html
```

---

## Testing Best Practices

1. **Test behavior, not implementation**
   - Focus on outputs and state changes
   - Don't test internal details

2. **Use descriptive test names**
   - `test_requirements_agent_creates_valid_requirements`
   - Not: `test_req_agent`

3. **One assertion per test (when possible)**
   - Makes failures easier to diagnose

4. **Use fixtures for common setup**
   - Reduces duplication
   - Makes tests more readable

5. **Mock external dependencies**
   - LLM calls
   - Network requests
   - File I/O (when not testing file operations)

6. **Test edge cases**
   - Empty inputs
   - Invalid data
   - Boundary conditions

7. **Test error handling**
   - What happens when LLM fails?
   - What if database is unavailable?

---

## Running Tests Locally

```bash
# All tests
make test

# With coverage
make test-cov

# Specific test file
pytest tests/unit/test_base_agent.py -v

# Specific test
pytest tests/unit/test_base_agent.py::test_escalation_logic -v

# With output
pytest tests/unit/ -v -s

# Fast tests only
pytest tests/unit/ tests/integration/ -v

# All tests including slow E2E
pytest tests/ -v --slow
```

---

## Writing New Tests

### Template for Unit Test

```python
\"\"\"Unit tests for [module name].\"\"\"

from src.your_module import YourClass
from src.state.schema import AgentState

def test_your_function_basic_case():
    \"\"\"Test basic functionality of your_function.\"\"\"
    # Arrange
    input_data = "test"

    # Act
    result = your_function(input_data)

    # Assert
    assert result == expected_output

def test_your_function_edge_case():
    \"\"\"Test edge case handling.\"\"\"
    # Test with empty input
    result = your_function("")
    assert result is not None
```

### Template for Integration Test

```python
\"\"\"Integration tests for [workflow name].\"\"\"

from src.agents import YourAgent
from src.state.schema import AgentState, Phase

def test_your_workflow():
    \"\"\"Test complete workflow.\"\"\"
    # Setup
    state = AgentState(objective="Test")
    agent = YourAgent()

    # Execute
    updates = agent(state)

    # Apply updates
    for key, value in updates.items():
        setattr(state, key, value)

    # Verify
    assert state.phase == Phase.EXPECTED
    assert len(state.your_artifact) > 0
```

---

## Questions?

For testing questions, open a GitHub Discussion with the `testing` label.
