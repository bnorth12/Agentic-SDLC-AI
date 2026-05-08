# Project Roadmap

**Agentic SDLC AI Organization**  
*Self-hosted multi-agent systems engineering environment*

This roadmap outlines the phased development of the project. We are currently in **Phase 0**.

---

## Phase 0 — Foundation (Current — May 2026)

**Status: In Progress**

**Goals:**
- Establish clean project structure
- Create comprehensive documentation
- Set up local development environment (Windows 11 friendly)
- Define core architecture and shared state
- Basic Docker + Ollama + Postgres infrastructure

**Deliverables:**
- ✅ Repository skeleton with proper folder layout
- ✅ All initial Markdown documentation (README, CONTRIBUTING, architecture, agent-roles, hardware, getting-started, roadmap)
- ✅ `pyproject.toml` + dependency management
- ✅ Docker Compose for Postgres checkpointer
- ✅ Basic `AgentState` schema
- Basic supervisor graph placeholder

---

## Phase 1 — Minimum Viable Product (MVP) (Next 4–8 weeks)

**Goals:**
- Functional multi-agent system with core leadership and 3–4 specialist agents
- Persistent state and basic cross-agent memory
- Working Human-in-the-Loop (HITL) mechanism
- At least one review board working

**Key Features:**
- Program Manager + Chief Engineer supervisor agents
- Core agents: Requirements Development, Systems Architecture, Software Development
- One Review Board (e.g., Architecture Review Board) as a subgraph with voting
- LangGraph checkpointing with Postgres
- Simple CLI + basic Streamlit UI for HITL
- Tool integration (file I/O, basic code execution)

**Success Criteria:**
- You can give the system a high-level requirement and watch agents collaborate through a review board with human approval gates.

---

## Phase 2 — Full Engineering Organization (2–4 months)

**Goals:**
- Implement the complete set of specialist agents
- Mature governance and review processes
- Robust tool ecosystem

**Agents to Add:**
- Safety / Security / Reliability
- Interface Design
- Verification & Validation
- Integration & Test
- Configuration Management
- Data Management
- Documentation & Training
- Quality Assurance
- DevOps / Deployment
- Human Factors

**Features:**
- Multiple Review Boards (Requirements, Risk, CM, etc.)
- Advanced shared memory & summarization
- Git integration + local code sandbox
- Better HITL web interface
- Decision logging and audit trail
- Basic program dashboard

---

## Phase 3 — Advanced Agentic Capabilities (4–8 months)

**Goals:**
- Make the system truly intelligent and self-improving
- Support complex, long-running programs

**Features:**
- Long-term memory across multiple programs
- Automated trade studies and decision support
- Multi-modal support (diagrams, code, documents)
- Agent fine-tuning / domain-specific prompting
- Simulation & what-if analysis
- Parallel execution of independent workstreams
- Risk prediction and proactive mitigation

---

## Phase 4 — Production Readiness & Scaling (8+ months)

**Goals:**
- Turn this into a reliable engineering tool
- Support real-world programs

**Features:**
- Multi-user roles and permissions (different experts have different HITL authority)
- Observability & tracing (LangSmith / Langfuse self-hosted)
- Security hardening
- Deployment templates (single machine → server)
- Performance optimization (model routing, caching)
- Exportable artifacts (requirements docs, architecture diagrams, verification reports)
- Integration with real tools (Jira, GitHub, DOORS, etc.)

---

## Stretch Goals (Future)

- Autonomous sprint execution
- Integration with physical hardware / digital twins
- Support for hardware + software co-design
- Learning from past program outcomes (organizational memory)
- Open-source community contributions and extensions

---

## Current Priorities (May 2026)

1. Finish Phase 0 infrastructure on Windows 11
2. Build and test the basic supervisor graph
3. Implement the first 3 agents + one review board
4. Create a working end-to-end demo (requirements → architecture review)

---

**Want to help?**  
Check the [CONTRIBUTING.md](../CONTRIBUTING.md) or open an Issue/Discussion with the label `good first issue`.

---

*Last updated: May 2026*