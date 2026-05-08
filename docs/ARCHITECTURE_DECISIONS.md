# Architecture Decision Records (ADRs)

This document captures key technical and architectural decisions made for the project.

---

## ADR-001: Use LangGraph for Multi-Agent Orchestration

**Status**: ✅ Accepted

**Context**: Need a framework to orchestrate multiple AI agents with:
- Persistent state across sessions
- Complex conditional routing
- Human-in-the-loop integration
- Checkpointing and recovery

**Decision**: Use LangGraph (by LangChain) as the core orchestration framework.

**Alternatives Considered**:
1. **Custom orchestration**: Too much reinvention, no checkpointing
2. **AutoGen**: Less flexible state management, heavier abstractions
3. **CrewAI**: Good for simple workflows, lacks fine-grained control
4. **Plain LangChain**: No graph-based routing, harder to visualize

**Consequences**:
- ✅ Built-in PostgreSQL checkpointing
- ✅ Clear graph visualization and debugging
- ✅ Strong integration with LangChain ecosystem
- ✅ Active development and community
- ⚠️ Learning curve for graph-based paradigm
- ⚠️ Relatively new (API may evolve)

---

## ADR-002: Self-Hosted Ollama for LLM Inference

**Status**: ✅ Accepted

**Context**: Need local LLM inference for:
- Privacy and data control
- Cost predictability
- No internet dependency
- Support for open-source models

**Decision**: Use Ollama as the primary inference engine.

**Alternatives Considered**:
1. **Cloud APIs (OpenAI, Anthropic)**: Privacy concerns, ongoing costs, internet required
2. **vLLM**: More complex setup, better for production scale
3. **llama.cpp directly**: Too low-level, no API server

**Consequences**:
- ✅ Complete privacy (data never leaves machine)
- ✅ Simple setup and model management
- ✅ Cross-platform support (Windows, Mac, Linux)
- ✅ Active model ecosystem
- ⚠️ Requires significant local hardware
- ⚠️ Inference speed limited by GPU
- ⚠️ Model quality depends on available open-source models

**Future**: May add vLLM support for production deployments.

---

## ADR-003: PostgreSQL for State Persistence

**Status**: ✅ Accepted

**Context**: Need reliable, queryable persistence for:
- Graph checkpoints (resume workflows)
- Long-term memory and history
- Vector embeddings (future)

**Decision**: Use PostgreSQL with LangGraph's native checkpointing.

**Alternatives Considered**:
1. **SQLite**: Too limited for production, no concurrent access
2. **Redis**: No persistent durability by default
3. **MongoDB**: Less mature LangGraph integration

**Consequences**:
- ✅ Mature, reliable database
- ✅ Native LangGraph support
- ✅ pgvector extension for embeddings
- ✅ Good query and analytics capabilities
- ✅ Easy backup and replication
- ⚠️ Requires Docker or separate installation
- ⚠️ Slightly heavier than SQLite for simple cases

---

## ADR-004: Pydantic for State Schema

**Status**: ✅ Accepted

**Context**: Need type-safe, validated state representation.

**Decision**: Use Pydantic v2 models for all state schemas.

**Alternatives Considered**:
1. **Plain dictionaries**: No validation, error-prone
2. **dataclasses**: Less validation, no serialization
3. **attrs**: Less LangChain integration

**Consequences**:
- ✅ Automatic validation
- ✅ Type safety with IDE support
- ✅ JSON serialization out of the box
- ✅ Excellent documentation through types
- ✅ Native LangGraph support
- ⚠️ Slight performance overhead
- ⚠️ Learning curve for complex models

---

## ADR-005: No Cloud Dependencies in Phase 1

**Status**: ✅ Accepted

**Context**: Initial focus should be on self-hosted, privacy-preserving deployment.

**Decision**: Phase 1 will not support cloud LLM APIs (OpenAI, Anthropic, etc.).

**Rationale**:
- Keeps architecture simple
- Forces optimization for local inference
- Aligns with privacy goals
- Reduces cost during development

**Consequences**:
- ✅ Simpler codebase
- ✅ No API key management
- ✅ Forces focus on prompt efficiency
- ⚠️ May limit initial model quality
- ⚠️ Steeper hardware requirements

**Future**: Phase 3+ may add optional cloud model support for specific roles (e.g., Chief Engineer with GPT-4).

---

## ADR-006: Hierarchical Agent Authority Model

**Status**: ✅ Accepted

**Context**: Need clear decision-making hierarchy and escalation paths.

**Decision**: Implement authority levels (LOW, MEDIUM, HIGH, HIGHEST) with escalation protocol.

**Model**:
```
HIGHEST: Chief Engineer, Program Manager (can override boards)
HIGH:    Safety Agent (can block unsafe designs)
MEDIUM:  Requirements, Architecture (need board approval)
LOW:     Development, Documentation (work within approved designs)
```

**Consequences**:
- ✅ Clear responsibility and accountability
- ✅ Prevents low-authority agents from making critical decisions
- ✅ Natural escalation paths
- ✅ Mirrors real engineering organizations
- ⚠️ Requires careful prompt engineering to respect boundaries
- ⚠️ May create bottlenecks at leadership level

---

## ADR-007: Review Boards as Separate Subgraphs

**Status**: ✅ Accepted

**Context**: Formal review processes need multi-agent collaboration and voting.

**Decision**: Implement review boards as reusable subgraphs that can be invoked from main supervisor graph.

**Structure**:
```python
Board Subgraph:
  1. Gather member assessments (parallel or sequential)
  2. Tally votes according to rules
  3. Compile decision with rationale
  4. Return to supervisor for HITL
```

**Consequences**:
- ✅ Reusable across different board types
- ✅ Clear separation of concerns
- ✅ Easy to test independently
- ✅ Flexible voting algorithms
- ⚠️ Increased graph complexity
- ⚠️ More LLM calls (cost in time/compute)

---

## ADR-008: Synchronous Execution (Phase 1)

**Status**: ✅ Accepted (for Phase 1)

**Context**: LangGraph executes nodes sequentially by default.

**Decision**: Accept synchronous execution for Phase 1 MVP.

**Rationale**:
- Simpler to reason about and debug
- Sufficient for proof-of-concept
- Most agent work has dependencies anyway

**Consequences**:
- ✅ Easier debugging and development
- ✅ Predictable execution order
- ✅ Simpler state management
- ⚠️ Slower for independent work streams
- ⚠️ Doesn't leverage full hardware capacity

**Future**: Phase 3 may introduce parallel execution for independent agents or work items.

---

## ADR-009: Rich Terminal UI for Phase 0-1

**Status**: ✅ Accepted

**Context**: Need user interface for development and demos.

**Decision**: Use Rich library for formatted terminal output; defer web UI to Phase 2.

**Rationale**:
- Fast to implement
- No frontend complexity
- Great for development and debugging
- Works in CI/CD pipelines

**Consequences**:
- ✅ Beautiful, readable output immediately
- ✅ No JavaScript/frontend required
- ✅ Works over SSH
- ⚠️ Not suitable for non-technical users
- ⚠️ Limited interactivity

**Future**: Phase 2 will add Streamlit/Gradio web UI.

---

## ADR-010: Examples Over Tests for Initial Validation

**Status**: ✅ Accepted (temporary)

**Context**: Need rapid iteration during Phase 0.

**Decision**: Prioritize working examples over comprehensive test suite initially.

**Rationale**:
- Examples serve as both documentation and validation
- Faster to iterate on agent behavior
- More valuable for early adopters to understand system

**Consequences**:
- ✅ Clear demonstrations of capabilities
- ✅ Fast iteration
- ⚠️ Risk of regressions without tests
- ⚠️ Technical debt

**Plan**: Transition to test-driven development in Phase 1 as architecture stabilizes.

---

## ADR-011: Minimal Tool Ecosystem Initially

**Status**: ✅ Accepted

**Context**: Could build extensive tool library (code exec, Git, diagramming, etc.).

**Decision**: Implement only essential tools (file I/O, basic code analysis) in Phase 0.

**Rationale**:
- Focus on core orchestration and agent logic
- Tools can be added incrementally
- Avoid over-engineering before validating approach

**Consequences**:
- ✅ Faster to MVP
- ✅ Simpler to understand and debug
- ⚠️ Limited practical capabilities
- ⚠️ Agents can't execute or verify code yet

**Future**: Phase 1-2 will add sandbox execution, Git integration, diagramming tools.

---

## ADR-012: Human-in-the-Loop at Board Decisions

**Status**: ✅ Accepted

**Context**: Where should human approval gates be placed?

**Decision**: Require human approval after major board decisions (can be disabled via config).

**Rationale**:
- Board decisions are high-impact (baselines, approvals)
- Gives humans ultimate control
- Prevents runaway AI decision-making
- Builds trust in system

**Consequences**:
- ✅ Safety net for critical decisions
- ✅ Human maintains authority
- ✅ Opportunity to provide feedback
- ⚠️ Interrupts workflow
- ⚠️ Requires human availability

**Configuration**: Can disable for testing or trusted workflows via `ENABLE_HITL=false`.

---

## ADR-013: Configuration via Environment Variables

**Status**: ✅ Accepted

**Context**: Need flexible configuration for different environments.

**Decision**: Use Pydantic Settings with `.env` files for configuration.

**Rationale**:
- 12-factor app principle
- Easy to override for different environments
- Type-safe with Pydantic
- No configuration code changes needed

**Consequences**:
- ✅ Flexible per-environment configuration
- ✅ No secrets in code
- ✅ Easy to understand and modify
- ⚠️ Need to manage `.env` files
- ⚠️ Can be complex with many options

**File**: `.env.example` provides template with all options documented.

---

## Future ADRs to Consider

- **ADR-014**: Vector database selection (pgvector vs. Chroma vs. Pinecone)
- **ADR-015**: Multi-model routing strategy
- **ADR-016**: Web UI framework (Streamlit vs. Gradio vs. custom React)
- **ADR-017**: Code execution sandbox approach
- **ADR-018**: Git integration strategy
- **ADR-019**: Observability and monitoring approach
- **ADR-020**: Scale-out strategy for multiple concurrent projects

---

## How to Propose a New ADR

1. Open a GitHub Discussion under "Architecture"
2. Describe the problem/decision needed
3. List alternatives considered
4. Propose recommendation with rationale
5. Community discusses
6. Maintainers approve and add to this document

---

**Last Updated**: 2024 (Phase 0)
