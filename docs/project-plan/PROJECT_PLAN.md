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

---

## 8. Skills Architecture Layer (Agent Overlay)

### Why This Layer Is Needed

The current product architecture is role-centric (agents map to SDLC roles). To increase capability depth without multiplying agent count, we introduce a **Skills Layer** that is composed onto agents at runtime.

**Definition**: A skill is a reusable, discipline-specific capability module that can be attached to one or more agents to produce policy-conformant outputs.

Examples:
- Requirements quality checks attached to Requirements + Chief Engineer agents
- Threat modeling attached to Safety/Security + Architecture agents
- Traceability synthesis attached to Requirements + V&V + QA agents

### Architectural Position

Layer relationship:

1. Workflow Layer: supervisor graph, gate transitions, HITL pauses
2. Agent Layer: role authority and decision ownership
3. Skills Layer: reusable technical competencies (this addition)
4. Tooling Layer: file/code/memory/integration tool adapters
5. Evidence Layer: artifacts, trace links, gate evidence payloads

### Skill Contract (Governance-Critical)

Each skill module shall implement:

- `skill_id`, `name`, `discipline`, `version`
- `inputs_required` and `artifacts_produced`
- `policy_checks` mapped to gate criteria
- `traceability_links` generation (requirement, risk, decision, test refs)
- `confidence_score` and `escalation_conditions`
- deterministic `output_schema` for linting and validation

### Integration Rules

1. Skills augment agent outputs but do not change authority ownership.
2. Gate readiness is evaluated on agent output plus required skill evidence.
3. A gate cannot transition to READY if any mandatory skill evidence is missing.
4. Skills remain reusable across agents; no duplicate discipline logic in agent prompts.

---

## 9. Skills Backlog (Initial Implementation Set)

The following skills are prioritized around core engineering disciplines.

| Priority | Skill | Discipline | Primary Agents | Primary Gates | Core Outputs |
|----------|-------|------------|----------------|---------------|--------------|
| P0 | Requirements Quality Skill | Requirements Engineering | Requirements Dev, Chief Engineer | Gate 2 | noun-SHALL-verb checks, hierarchy integrity, orphan report |
| P0 | Architecture Allocation Skill | Systems Architecture | Architecture, Chief Engineer | Gate 3 | requirement-to-component allocation matrix, interface completeness report |
| P0 | Threat & Hazard Skill | Safety/Security Engineering | Safety/Security/Reliability, Architecture | Gate 3 | STRIDE model, hazard log, mitigation linkage |
| P0 | Traceability Synthesis Skill | Systems Integration | Requirements Dev, V&V, QA | Gates 2-6 | RTM rollup, forward/backward trace validation |
| P1 | Test Design Skill | Verification and Validation | V&V / Test Agent | Gate 5 | requirement-linked test cases, verification method coverage map |
| P1 | Configuration Baseline Skill | Configuration Management | Configuration Manager | Gate 4, Gate 6 | baseline register, change-set impact report |
| P1 | Release Readiness Skill | Integration and Release | Integration Agent, QA | Gate 6, Gate 7 | release checklist, unresolved defect waiver set |
| P1 | Data Governance Skill | Data Engineering / Governance | Data Management | Gates 3-7 | data inventory, quality constraints, data control evidence |
| P2 | Operational Reliability Skill | Operations Engineering | Integration Agent, Maintenance Agent | Gate 7 | SLO checks, deployment risk score, rollback readiness |
| P2 | Compliance Packaging Skill | Quality/Compliance | QA, Program Manager | Gates 6-7 | audit package bundle, policy compliance manifest |

---

## 10. Sprint Placement Recommendation for Skills

Because the concept is critical and cross-cutting, skills should start as a dedicated stream in **Sprint 4** (not deferred to Sprint 7-8).

Recommended rollout:

1. Sprint 4: Skills framework foundation
	- skill contract schema
	- runtime skill registry
	- mandatory skill-to-gate mapping table
	- P0 implementation for Requirements Quality + Traceability Synthesis
2. Sprint 5: Verification-centered expansion
	- P0 completion for Architecture Allocation + Threat & Hazard
	- P1 Test Design + Configuration Baseline
	- gate validators consume skill evidence directly
3. Sprint 6: Observability + reliability hardening
	- skill execution metrics, confidence trends, escalation rates
	- Release Readiness skill integration to dashboard
4. Sprint 7-8: advanced skills and optimization
	- Data Governance, Operational Reliability, Compliance Packaging
	- model-policy coupling for skill selection

Rationale:
- Sprint 4 is the first implementation-heavy point where reusable discipline logic prevents prompt duplication.
- Introducing skills before full release hardening prevents late rework across multiple agents.

---

## 11. Exit Criteria Additions (Skills)

In addition to existing Definition of Done:

1. Required skills for targeted gates are registered and versioned.
2. Skill outputs pass schema validation and policy lint checks.
3. Skill-to-requirement and skill-to-test trace links are generated.
4. Missing mandatory skill evidence blocks gate READY transition.
5. Skill execution telemetry is captured for observability.
