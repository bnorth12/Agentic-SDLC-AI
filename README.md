# Agentic SDLC AI Organization

**A self-hosted, persistent multi-agent AI system that replicates a full engineering organization for Systems & Software Development Lifecycle (SDLC) execution.**

Built with **LangGraph**, this project creates a virtual AI-powered engineering company where specialized agents collaborate with formal governance, shared memory, review boards, and human-in-the-loop oversight — bringing real systems engineering discipline to AI-generated work.

---

## The Problem It Solves

Modern AI coding tools excel at generating individual components but frequently fail at large-scale, governed system development. They suffer from:
- "Vibe coding" — solutions that feel right but miss critical requirements, safety, security, or interface considerations
- Lack of persistent context and cross-agent coordination
- No built-in engineering governance or review processes
- No long-term memory across development phases

**This project aims to solve that** by creating a complete AI engineering organization that operates with the same rigor as a professional systems engineering team.

---

## Vision

Imagine giving the system a high-level mission statement or set of stakeholder needs, and watching a virtual organization of AI agents:

- Elicit and baseline requirements
- Perform trade studies
- Develop architecture
- Conduct safety, security, and reliability analyses
- Generate code and verification artifacts
- Hold formal Architecture Review Boards, Risk Boards, and Configuration Management Boards
- Maintain full traceability and configuration control
- Ask human experts for guidance exactly when needed

All of this runs **locally on your hardware**, with full persistence, audit trails, and human override authority.

---

## Key Features

### Agentic Organization Structure
- **Leadership Layer**: Program Manager Agent + Chief Engineer Agent (with override authority)
- **Specialist Agents**: One dedicated agent per engineering discipline (Requirements, Architecture, Safety/Security/Reliability, Verification, Configuration Management, etc.)
- **Review Boards**: Collaborative multi-agent subgraphs that simulate formal boards (Architecture Review Board, Risk Board, Requirements Review Board, etc.) with discussion, voting, and recommendations
- **Defined Roles, Responsibilities, Authorities (RRA)**: Every agent has clear boundaries and escalation paths

### Technical Capabilities
- **Persistent Shared State & Memory**: Full program context (artifacts, decisions, risks, history) survives restarts via LangGraph checkpointing + vector database
- **Cross-Agent Collaboration**: Agents can query each other, reference past decisions, and maintain awareness of all equities
- **Human-in-the-Loop (HITL)**: Experts can interrupt at any critical decision, review outputs, provide corrections, or override board decisions
- **Background Execution**: Agents continue working on long-running tasks even when you close the interface
- **Formal Governance**: No major decision moves forward without appropriate review board approval (unless overridden by Chief Engineer/Program Manager with justification)

### Self-Hosted & Private
- Runs 100% locally using Ollama (or vLLM)
- No data leaves your machine
- Supports strong open-source models (Llama 3.1, Qwen2.5, Mistral, etc.)

---

## How It Works (High-Level Flow)

1. **Task Ingestion** — User or Program Manager introduces new work
2. **Supervisor Routing** — Chief Engineer + Program Manager assign work and track overall status
3. **Specialist Execution** — Relevant agents perform their discipline-specific work and update shared state
4. **Governance Gates** — Major artifacts (requirements baseline, architecture, design changes) are sent to the appropriate Review Board subgraph
5. **Board Review** — Multiple agents discuss, debate, vote, and produce a formal recommendation + rationale
6. **HITL Checkpoint** — Human experts review board output and either approve, request changes, or let leadership override
7. **Iteration & Integration** — Approved work proceeds; issues loop back to responsible agents
8. **Artifact Generation** — Requirements documents, architecture diagrams, code, test plans, verification evidence, etc.

All interactions and decisions are logged for traceability.

---

## Tech Stack

| Layer              | Technology                          |
|--------------------|-------------------------------------|
| Orchestration      | LangGraph + LangChain               |
| Inference          | Ollama (native Windows) or vLLM     |
| Persistence        | Postgres + LangGraph Checkpointer  |
| Vector Memory      | pgvector / Chroma                   |
| Tools              | Local code sandbox, git, file I/O   |
| UI (planned)       | Streamlit + FastAPI                 |
| Infrastructure     | Docker Compose                      |

---

## Project Structure
.
├── docs/                    # Comprehensive documentation
├── src/
│   ├── agents/              # Individual agent implementations
│   ├── graphs/              # Supervisor, specialist workflows, board subgraphs
│   ├── state/               # Shared Pydantic state schema
│   ├── tools/               # Reusable tools
│   ├── boards/              # Review board logic
│   └── utils/
├── docker/                  # Docker services
├── examples/                # Demo scripts
├── tests/
└── ... (see full structure in docs)


---

## Getting Started (Windows 11)

See [`docs/getting-started.md`](docs/getting-started.md) for complete Windows + VS Code instructions.

**Quick Summary**:
1. Install Docker Desktop + Ollama
2. `docker compose up -d`
3. Create venv and `pip install -e ".[dev]"`
4. Run first example

---

## Hardware Requirements

See [`docs/hardware-requirements.md`](docs/hardware-requirements.md)

**Recommended for good performance**: RTX 4090 (or equivalent) + 64GB+ RAM.

---

## Roadmap

See [`docs/roadmap.md`](docs/roadmap.md) — currently in **Phase 0 (Foundation)**.

---

## Agent Roles

See [`docs/agent-roles.md`](docs/agent-roles.md) for the full list of planned agents and their responsibilities.

---

## Why This Project Matters

This is more than just "AI agents writing code."  
It is an attempt to encode **professional systems engineering governance** into an autonomous yet controllable AI system — something that could dramatically improve the quality, safety, and maintainability of AI-generated complex software.

---

## Contributing

We welcome contributors! See [`CONTRIBUTING.md`](CONTRIBUTING.md) for details.

Especially needed:
- Review board implementation logic
- Tool development (code execution sandbox, diagramming)
- UI development
- Prompt engineering for engineering domains
- Testing & validation

---

## License

MIT License — see [LICENSE](LICENSE) file.

---

## Community & Support

- **GitHub Discussions**: Ask questions, share ideas
- **Issues**: Report bugs, request features
- **Pull Requests**: Contribute code
- **Documentation**: Improve guides and examples

---

## Success Metrics & Goals

We measure progress by:
- ✅ **Working agents**: 4/12 core agents implemented
- ✅ **Review boards**: 1/4 primary boards working
- ✅ **Test coverage**: Targeting 80%+ overall
- ⚠️ **End-to-end workflows**: Basic flow working, needs refinement
- ❌ **UI**: Not yet started
- ❌ **Real-world validation**: Needs production testing

**Goal**: Build a truly useful engineering tool that professional teams can adopt, not just another demo.

---

## FAQ

**Q: Can this replace human engineers?**  
A: No. This is a tool to augment human engineering teams, not replace them. Human oversight, judgment, and creativity remain essential.

**Q: What models work best?**  
A: Qwen2.5-32B and Llama 3.1-70B show best results. Smaller models (7B-8B) work for simple tasks but struggle with complex reasoning.

**Q: Can I use cloud LLM APIs (OpenAI, Anthropic)?**  
A: Not currently, but support could be added. The focus is on self-hosted, private deployment.

**Q: How long does a workflow take?**  
A: Depends on model size and complexity. With an 8B model on RTX 4090: basic requirements workflow ~30-60 seconds. With 32B model: 2-5 minutes.

**Q: Is this production-ready?**  
A: No. This is Phase 0 (Foundation). Use for experimentation and research. Production readiness is Phase 4 goal (8+ months out).

---

**Project Status**: Phase 0 - Foundation (Active Development)  
**Version**: 0.1.0  
**License**: MIT

---

**Ready to begin?**  
```bash
make setup
python examples/01_basic_requirement.py
```

Clone the repo, follow the [Getting Started guide](docs/getting-started.md), and help us build the future of agentic systems engineering.

**Star ⭐ this repo** if you find it interesting!
