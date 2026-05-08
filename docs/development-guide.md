# Development Guide

## Architecture Deep Dive

### LangGraph Execution Model

This project uses **LangGraph** for stateful, multi-agent orchestration. Key concepts:

- **StateGraph**: Directed graph where nodes are functions that process and update shared state
- **Nodes**: Agent execution functions that receive state and return updates
- **Edges**: Control flow between agents (conditional or fixed)
- **Checkpointing**: Automatic state persistence after each node execution
- **Human-in-the-Loop**: Interrupt points for human review before/after nodes

### State Management Patterns

**Shared State (`AgentState`)**:
- Single source of truth for all agents
- Immutable updates (return dictionaries to merge)
- Pydantic models for type safety and validation
- Checkpointed to PostgreSQL for persistence

**State Update Pattern**:
```python
def agent_node(state: AgentState) -> dict[str, Any]:
    # Read from state
    requirements = state.requirements

    # Perform work
    new_req = create_requirement()

    # Return updates (will be merged into state)
    return {
        "requirements": {**requirements, new_req.id: new_req},
        "messages": [f"Added requirement {new_req.id}"],
    }
```

### Agent Communication Protocols

Agents communicate through:
1. **Shared State**: Primary mechanism - all agents read/write to `AgentState`
2. **Messages List**: Inter-agent communication log
3. **Work Queue**: Task assignment system
4. **Board Results**: Formal review outcomes

**Message Format**:
```
[agent_name] Message content
```

Example:
```python
{"messages": ["[requirements_agent] Developed 5 requirements"]}
```

### Review Board Voting Algorithms

**Board Composition**:
- Required roles (e.g., Chief Engineer, Architect, Requirements Engineer)
- Each member independently assesses the item under review
- Members provide: assessment, concerns, questions, vote, rationale

**Vote Types**:
- `APPROVE`: Accept as-is
- `APPROVE_WITH_CONDITIONS`: Approve with specific requirements
- `REJECT`: Do not approve, needs significant changes
- `DEFER`: Need more information before deciding

**Decision Algorithm**:
```python
def tally_votes(votes):
    if any(vote == REJECT):
        return REJECT
    if any(vote == DEFER):
        return DEFER
    if any(has_conditions):
        return APPROVE_WITH_CONDITIONS
    return APPROVE
```

---

## Adding a New Agent

### Step 1: Define Agent Class

Create `src/agents/your_agent.py`:

```python
from src.agents.base_agent import BaseAgent
from src.config.prompts import YOUR_AGENT_PROMPT
from src.state.schema import AgentState

class YourAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="your_agent",
            role="Your Role Title",
            authority_level="MEDIUM",  # LOW, MEDIUM, HIGH, HIGHEST
        )

    def get_system_prompt(self, state: AgentState) -> str:
        return YOUR_AGENT_PROMPT.format(objective=state.objective)

    def process(self, state: AgentState) -> dict[str, Any]:
        # 1. Check if you have work assigned
        # 2. Perform your domain-specific analysis
        # 3. Update state with outputs
        # 4. Request review if needed

        updates = {"messages": []}

        # Your logic here

        return updates
```

### Step 2: Add Prompt Template

In `src/config/prompts.py`:

```python
YOUR_AGENT_PROMPT = BASE_AGENT_PROMPT.format(
    systems_context=SYSTEMS_ENGINEERING_CONTEXT,
    role_name="Your Role",
    responsibilities=\"""
- Responsibility 1
- Responsibility 2
\""",
    authority_level="MEDIUM - Description of authority",
    objective="{objective}",
)
```

### Step 3: Register in Supervisor Graph

In `src/graphs/supervisor.py`:

```python
from src.agents import YourAgent

def your_agent_node(state: AgentState) -> dict[str, Any]:
    agent = YourAgent()
    return agent(state)

# In build_supervisor_graph():
workflow.add_node("your_agent", your_agent_node)

# Add edges to/from your agent
workflow.add_edge("some_node", "your_agent")
```

### Step 4: Update Exports

In `src/agents/__init__.py`:

```python
from src.agents.your_agent import YourAgent

__all__ = [..., "YourAgent"]
```

### Step 5: Add Tests

Create `tests/unit/test_your_agent.py`:

```python
from src.agents import YourAgent
from src.state.schema import AgentState

def test_your_agent_initialization():
    agent = YourAgent()
    assert agent.name == "your_agent"
    assert agent.authority_level == "MEDIUM"

def test_your_agent_process():
    agent = YourAgent()
    state = AgentState(objective="Test objective")
    updates = agent.process(state)
    assert "messages" in updates
```

### Step 6: Update Documentation

Update `docs/agent-roles.md` with your agent's role and responsibilities.

---

## Implementing a Review Board

### Step 1: Create Board Class

Create `src/boards/your_review_board.py`:

```python
from src.boards.base_board import (
    BaseReviewBoard,
    BoardMemberAssessment,
    BoardVote,
)
from src.state.schema import AgentState, BoardDecision

class YourReviewBoard(BaseReviewBoard):
    def __init__(self):
        super().__init__(
            name="Your Review Board",
            required_roles=["role1", "role2", "role3"],
        )

    def evaluate(
        self, state: AgentState, item_to_review: dict
    ) -> BoardDecision:
        # 1. Gather assessments from required roles
        assessments = self._gather_assessments(state, item_to_review)

        # 2. Tally votes
        overall_vote = self.tally_votes(assessments)

        # 3. Compile decision
        decision = self.compile_decision(assessments, overall_vote)

        return decision

    def _gather_assessments(
        self, state: AgentState, item: dict
    ) -> list[BoardMemberAssessment]:
        assessments = []

        # For each required role, create an assessment
        # In production, invoke actual agents with LLM

        return assessments
```

### Step 2: Register in Supervisor

In `src/graphs/supervisor.py`:

```python
from src.boards import YourReviewBoard

def review_board_node(state: AgentState) -> dict[str, Any]:
    if state.active_board == "your_review":
        board = YourReviewBoard()
        decision = board.evaluate(state, state.your_artifact)
        # ... handle decision
```

### Step 3: Add Tests

Test vote tallying, decision compilation, and end-to-end board flow.

---

## Prompt Engineering Best Practices

### Structured Output Requirements

Always request structured output (JSON) for parsing:

```python
messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content=f\"""
Analyze X and provide output in JSON format:
{{
    "field1": "value",
    "field2": ["list", "of", "items"],
    "rationale": "explanation"
}}
\"""),
]
```

### Few-Shot Examples

Include examples in prompts for better output quality:

```python
EXAMPLE_PROMPT = \"""
Example 1:
Input: "Build a todo app"
Output: {{
    "id": "REQ-001",
    "text": "System shall allow users to create tasks",
    "category": "functional"
}}

Example 2:
Input: "Secure authentication"
Output: {{
    "id": "REQ-002",
    "text": "System shall implement multi-factor authentication",
    "category": "security"
}}

Now analyze: {user_input}
\"""
```

### Chain-of-Thought Reasoning

Ask agents to explain their reasoning:

```python
prompt = \"""
Task: {task}

Think through this step-by-step:
1. What are the key considerations?
2. What are the risks?
3. What is your recommendation?
4. What is your rationale?

Provide your analysis:
\"""
```

### Domain-Specific Prompting

**Requirements Engineering**:
- Emphasize "shall" statements
- Request verification criteria
- Ask for traceability to stakeholder needs

**Architecture**:
- Request views (structural, behavioral, deployment)
- Ask for interface definitions
- Require traceability to requirements

**Safety/Security**:
- Ask for threat modeling
- Request hazard analysis
- Require risk assessment (probability × impact)

---

## Debugging & Troubleshooting

### LangSmith Integration

Enable tracing in `.env`:
```
ENABLE_TRACING=true
LANGSMITH_API_KEY=your_key
LANGSMITH_PROJECT=agentic-sdlc-ai
```

View traces at https://smith.langchain.com/

### Checkpoint Inspection

Query checkpoints directly:

```python
from src.state.persistence import get_persistence_manager

manager = get_persistence_manager()
checkpointer = manager.get_checkpointer()

# List checkpoints for a thread
checkpoints = checkpointer.list(
    {"configurable": {"thread_id": "your_thread_id"}}
)

for cp in checkpoints:
    print(f"Checkpoint: {cp.id} at {cp.ts}")
```

### State Debugging Tools

Add debugging node to graph:

```python
def debug_node(state: AgentState) -> dict:
    from rich import print as rprint
    rprint("[bold]Current State:[/]")
    rprint(f"Phase: {state.phase}")
    rprint(f"Requirements: {len(state.requirements)}")
    rprint(f"Messages: {state.messages[-5:]}")  # Last 5
    return {}
```

### Common Issues and Fixes

**Issue**: Graph runs forever
- **Cause**: Conditional routing logic has no END path
- **Fix**: Ensure `should_continue()` can return "END"

**Issue**: Agent not executing
- **Cause**: Work queue empty or wrong assignment
- **Fix**: Check work item `assigned_to` field matches agent name

**Issue**: State not persisting
- **Cause**: Database not initialized or connection failed
- **Fix**: Run `python scripts/setup_db.py`, check Postgres is running

**Issue**: Model responses are poor quality
- **Cause**: Prompt too vague or model too small
- **Fix**: Add examples to prompts, use larger model (13B+)

---

## Performance Optimization

### Model Selection Guidelines

**Small Models (7B-8B)**:
- Fast inference (~1-3 sec per response)
- Good for: simple classification, routing, structured extraction
- Limitation: Less reasoning capability

**Medium Models (13B-32B)**:
- Moderate speed (~3-10 sec per response)
- Good for: most engineering tasks, analysis, generation
- **Recommended for production**

**Large Models (70B+)**:
- Slow inference (~30-60 sec per response)
- Good for: complex reasoning, architecture decisions, safety analysis
- Use for: Chief Engineer, critical reviews only

**Role-Based Model Assignment**:
```env
OLLAMA_MODEL=llama3.1:8b-instruct-q4_K_M  # Default
MODEL_CHIEF_ENGINEER=qwen2.5:32b-instruct-q4_K_M  # Upgrade for critical roles
MODEL_SAFETY=qwen2.5:32b-instruct-q4_K_M
```

### Batch Processing Strategies

Process multiple items in one LLM call:

```python
# Instead of:
for req in requirements:
    analyze(req)  # N LLM calls

# Do:
analyze_batch(requirements)  # 1 LLM call
```

### Caching Mechanisms

**Prompt Caching** (not yet in Ollama):
- Cache system prompts to reduce processing
- Will significantly speed up repeated calls

**Result Caching**:
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def analyze_requirement(req_text: str):
    # Expensive LLM call
    return result
```

### Parallel Execution

LangGraph doesn't natively support parallel nodes, but you can:

1. Use concurrent tool calls within a node
2. Process independent work items in parallel
3. Batch process when possible

```python
from concurrent.futures import ThreadPoolExecutor

def parallel_analysis_node(state: AgentState) -> dict:
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(analyze, item)
            for item in state.work_queue
        ]
        results = [f.result() for f in futures]

    return {"results": results}
```

---

## Testing Strategy

See [`docs/testing-strategy.md`](testing-strategy.md) for the complete testing approach.

---

## Next Steps

1. Implement your first custom agent
2. Add a new review board
3. Create end-to-end workflow tests
4. Optimize prompts for your domain
5. Contribute back to the project!

For questions, open a GitHub Discussion.
