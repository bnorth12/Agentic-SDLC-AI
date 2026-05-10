# Agentic SDLC AI — Project Plan

**Document ID**: PROJ-PLAN-001  
**Date**: 2026-05-08  
**Status**: Baseline

---

## 1. The Two-Layer Distinction

This project has an inherent meta-level challenge: **the repo is an AI tool that automates SDLC work — and we are using SDLC discipline to build it.** This creates two layers that must stay clearly separated.

### Layer 1 — Product Engineering (Object Level)
> *"What we are building"*

The Python codebase, agent implementations, LangGraph workflows, tests, Docker setup, and documentation that make up the **Agentic-SDLC-AI tool** itself. This is work that ends up in `src/`, `tests/`, `scripts/`, `docker/`, and `examples/`.

- Writing a new agent class → Layer 1
- Adding a unit test for the supervisor → Layer 1
- Fixing a bug in `base_agent.py` → Layer 1
- Setting up CI/CD pipeline → Layer 1

### Layer 2 — Project Governance (Meta Level)
> *"How we manage building it"*

Sprint planning, backlog management, policies, governance documents, and process artifacts that govern HOW we develop the tool. This is work that lives in `docs/`, `.github/`, and process artifacts.

- Writing this project plan → Layer 2
- Declaring sprint goals and acceptance criteria → Layer 2
- Running a HITL gate review on a sprint → Layer 2
- Updating the enforcement matrix → Layer 2

### The Dogfooding Principle

Both layers use the **same SDLC patterns and terminology** because we are proving the methodology by applying it to ourselves. When a sprint produces a new agent implementation (Layer 1), the project review for that sprint is governed by our own gate/HITL model (Layer 2). This is intentional validation — if the process is too burdensome to apply to our own work, it needs improvement.

**Rule**: When writing a task, prefix the work item type:
- `[IMPL]` — Layer 1 implementation work on the product
- `[GOV]` — Layer 2 project governance or process work
- `[TEST]` — Layer 1 test work
- `[INFRA]` — Layer 1 infrastructure/DevOps work
- `[DOC]` — documentation for the product (Layer 1) or process (Layer 2)

---

## 2. Project Objective

Build a **production-quality, multi-agent AI system** that automates systems engineering and SDLC workflows for complex software programs, using LangGraph orchestration, Ollama local inference, and a governance-first design.

### Success Criteria

| Criterion | Measure |
|-----------|---------|
| All planned agents implemented | 12 agents passing unit and integration tests |
| End-to-end SDLC workflow executes | Requirements intake → Architecture → Gate review → HITL → Decision in single graph run |
| Governance gates enforced | Supervisor blocks invalid READY transitions automatically |
| Test coverage | ≥ 80% unit test coverage across `src/` |
| HITL workflow functional | Human can pause, review context, approve/reject, and resume |
| Observability | Structured logs, traces, and health checks operational |
| Documentation complete | Getting-started guide produces working system in < 30 min |

---

## 3. Current State Assessment (Replan Snapshot)

### What Exists Now

| Area | Status | Notes |
|------|--------|-------|
| Core infrastructure (state, config, CLI) | ✅ Done | Pydantic v2, Typer, Rich |
| Base agent class | ✅ Done | Authority levels, governance output contract |
| Supervisor graph | ✅ Done | LangGraph, gate hook, HITL wiring |
| Core + specialist agents | ✅ Done | 12 agents total, including security/safety/compliance/integration/QA/ops/maintenance |
| Governance gates | ✅ Done | Requirements, architecture, implementation, deployment gate nodes wired |
| Governance policies and plans | ✅ Done | Baseline policy and engineering-plan corpus in place |
| Governance evidence validator | ✅ Done | Module + CLI + tests |
| Checkpoint persistence | ✅ Done | Postgres checkpointer with optional dependency handling |
| WorkPackage orchestration | ✅ Done | Queue model plus checkpoint resume semantics |
| KPI / metrics scaffolding | ✅ Done | Gate outcome aggregation and report generation |
| Integration and E2E tests | ✅ Done | Gate routing, persistence, and implementation-to-maintenance traceability |
| Docker compose (Ollama + PostgreSQL) | ✅ Done | Local stack definition exists |
| CI workflow | ⚠️ Partial | GitHub Actions exists, but it still needs coverage/lint hardening |
| Production Docker hardening | ❌ Not done | Non-root image, health checks, and runtime polish still pending |

### Remaining Gaps

1. **CI/CD hardening** — add lint and coverage enforcement, and broaden workflow validation.
2. **Production Docker config** — harden the app image and add container health checks.
3. **Observability dashboard** — turn KPI scaffolding into a human-readable status view.
4. **Remaining governance depth** — finish the broader compliance and model-routing items from the historical plan.

### Known Backlog (Capability Gaps from Enforcement Matrix)

1. **Safety/Security/Reliability Agent** — required for Gates 5-6; hazard log, threat model, security tests
2. **Software Development Agent** — required for Gate 4; code generation, requirement-linked PRs
3. **Verification & Validation Agent** — required for Gate 5; test plans, coverage, RTM
4. **Configuration Management Agent** — required for Gates 4 and 6; baseline register, change control
5. **Data Management Agent** — required for Gates 5-7; data inventory, quality reports
6. **Integration & Test Agent** — required for Gate 6; integration plans, system test execution
7. **Quality Assurance Agent** — required for Gate 7; QA audit trail, release checklist
8. **CI/CD Pipeline** — GitHub Actions: lint, test, coverage gate
9. **End-to-end integration tests** — full workflow from intake to Gate 3 with assertions
10. **HITL interactive test harness** — simulated human approval in test environment
11. **Observability dashboard** — metrics collection, structured trace output, health summary
12. **Multi-model routing** — route by agent role to appropriate Ollama model
13. **Prompt output linting** — automated checking that agent responses contain required governance fields
14. **Gate-specific response templates** — per-phase structured output schemas
15. **RAG / memory integration** — long-term project memory across runs
16. **CLI completion** — full Typer CLI covering all workflows
17. **Docker production config** — production-grade Dockerfile with non-root user, health checks

---

## 4. Phase Map

The roadmap phases align directly to sprint groups:

| Phase | Description | Sprints | Exit Condition |
|-------|-------------|---------|----------------|
| Phase 0 | Foundation (DONE) | Sprint 0 | Core infra + 4 agents + governance baseline |
| Phase 1 | MVP Completion | Sprints 1-3 | Expanded agents, gates, and baseline workflow now delivered in code |
| Phase 2 | SDLC Expansion | Sprints 4-5 | End-to-end workflow, HITL, and traceability have working coverage |
| Phase 3 | Persistent Multi-Run | Sprint 6 | Checkpointing, recovery, work packages, and metrics scaffolding are in place |
| Phase 4 | Advanced Capabilities | Sprints 7-8 | Remaining productionization and multi-model features |

---

## 5. Risk Register Summary

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| LLM output non-determinism breaks governance validation | High | High | Add output parsing + retry with structured prompts |
| Ollama local inference too slow for integration tests | Medium | Medium | Add mock LLM mode for testing; Ollama only in e2e tests |
| PostgreSQL not available in CI | Medium | High | Use SQLite or in-memory checkpointer for CI |
| Meta-confusion (Layer 1 vs Layer 2 drift) | Medium | Medium | Enforce `[IMPL]/[GOV]` prefix discipline in sprint items |
| Prompt alignment degrades as agents added | High | Medium | Automate governance field linting (Sprint 2) |
| Test coverage falls below threshold | Medium | High | Coverage gate in CI from Sprint 1 |

---

## 6. Definition of Done (per Sprint)

A sprint is done when:

1. All `[IMPL]` items are merged to main and tests pass
2. Test coverage ≥ 80% for changed modules
3. CI pipeline green
4. Sprint governance review completed (Gate checklist signed off)
5. Known blockers documented in next sprint backlog
6. `SPRINT_SUCCESSION.md` updated with sprint outcomes

---

## 7. Roles for This Project

Since this is a small repo with one active developer, roles collapse:

| SDLC Role | Who Plays It |
|-----------|-------------|
| Program Manager | Developer (using `project-development-manager` VS Code agent) |
| Chief Engineer | Developer (technical decisions) |
| Requirements / Architecture | Developer + GitHub Copilot |
| HITL Reviewer | Developer (deliberate review pauses) |
| All specialist agents | Implemented in code; exercised in tests |
