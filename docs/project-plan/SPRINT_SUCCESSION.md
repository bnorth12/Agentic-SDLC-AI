# Sprint Succession Plan

**Document ID**: SPRINT-PLAN-001  
**Scope**: Agentic-SDLC-AI, Sprints 0–8 (Phases 0–4)  
**Date**: 2026-05-08

---

## Overview

The Agentic-SDLC-AI project spans **8 development sprints** grouped into **4 phases**, each culminating in a major capability release. Each sprint is 2 weeks and includes explicit Gate readiness checks.

---

## Phase 0 → Phase 1 Transition (Sprint 0 Complete, Sprint 1 Starting)

### Phase 0 — Foundation (COMPLETE)

**Sprint 0** delivered:
- ✅ Pydantic v2 shared state schema with requirement, decision, risk, verification models
- ✅ LangGraph supervisor orchestration framework with HITL interrupt points
- ✅ 4 core agents: Program Manager, Chief Engineer, Requirements, Architecture
- ✅ Base agent class with governance output contract
- ✅ Governance validation and supervisor gate hook (automated READY blocking)
- ✅ 6 governance policies + 10 engineering plans
- ✅ Policy-to-agent enforcement matrix
- ✅ PostgreSQL checkpointing and persistence layer
- ✅ Docker Compose setup (Ollama + PostgreSQL)
- ✅ CLI skeleton with Typer

**Phase 0 Exit Criteria**: ✅ Met  
**Readiness for Phase 1**: ✅ Yes

---

## Phase 1 — MVP Completion (Sprints 1–3)

### Goal
Deliver all 11 planned agents, complete governance integration, and execute an end-to-end SDLC workflow from intake through architecture review with HITL gates.

### Sprint 1 — Planning & Infrastructure
**Dates**: May 9–23, 2026  
**Goal**: Establish planning baseline, architecture framework, and development infrastructure  

**Deliverables**:
- Architecture Decomposition Structure (ARCH-0001 through ARCH-0004)
- GitHub Actions CI/CD pipeline with 80% coverage gate (INFRA-0001, INFRA-0010)
- Mock LLM test harness (INFRA-0002)
- Sprint 2–3 backlog fully decomposed
- Requirements Authoring Guide

**Gate 1 Criteria**:
- All sprint items merged and tests passing
- Architecture approved by Chief Engineer
- CI/CD pipeline operational
- No P1 blockers

**Agents Delivered**: 4 (from Phase 0)  
**Agents Added**: 0  
**Requirements Coverage**: All L1 + L2/L3 (planning focus) APPROVED

---

### Sprint 2 — Requirements Agent Completion & HITL Activation
**Dates**: May 24–June 6, 2026  
**Goal**: Complete Requirements Development Agent with noun-SHALL-verb format, hierarchy validation, and full attribute population. Activate HITL pause/review flows.

**Deliverables**:
- Requirements Agent: noun-SHALL-verb format enforcement (AGT-0002, AGT-0010)
- Requirements Agent: unique ID assignment with persistence (AGT-0003, AGT-0011)
- Requirements Agent: hierarchy validation and orphan detection (AGT-0005, AGT-0012)
- Requirements Agent: full attribute population before APPROVED (AGT-0004)
- HITL activation: pause workflow and present evidence package (HITL-0001)
- Requirements Traceability Matrix (RTM) generation (GOV-0002)
- Integration tests for Gate 1 → Gate 2 transition with HITL pause

**Gate 2 Criteria** (Requirements Review):
- Requirements Agent passes all tests and produces APPROVED requirements in noun-SHALL-verb format
- RTM complete and included in Gate 2 evidence package
- HITL pause/resume working (human can pause, review, approve/reject)
- No orphan requirements; all L1 requirements decomposed to L2

**Agents Delivered**: 5 (4 + Requirements-enhanced)  
**Agents Added**: 1 (Requirements enhanced with full governance)  
**Requirements Coverage**: AGT-0002 through AGT-0005, GOV-0002, HITL-0001 → VERIFIED

---

### Sprint 3 — Safety/Security Agent & Integration Testing
**Dates**: June 7–20, 2026  
**Goal**: Add Safety/Security/Reliability agent for threat modeling, hazard analysis, and security controls. Implement first integration test covering intake through Gate 3.

**Deliverables**:
- Safety/Security/Reliability Agent (new)
- Hazard log and threat model generation
- Security controls mapping
- Integration test: full workflow intake → Gate 3 with all agents
- End-to-end observability: structured logs and traces for all agent outputs
- Metrics dashboard stub (planned for Phase 3)

**Gate 3 Criteria** (Architecture Review):
- Architecture Review Board (ARB) subgraph exercises review authority
- Safety/Security Agent produces threat model and hazard log
- Architecture-Requirement traceability complete
- Integration test passes end-to-end

**Agents Delivered**: 6 (5 + Safety/Security)  
**Agents Added**: 1 (Safety/Security/Reliability)  
**Requirements Coverage**: SYS-0005, SYS-0006 child requirements → VERIFIED

**Phase 1 Exit Criteria**:
- ✅ 6 agents implemented and tested
- ✅ Gate 1 → Gate 3 workflows executed with HITL approval
- ✅ End-to-end integration test passing
- ✅ Requirements, architecture, governance working
- ✅ CI/CD passing with ≥80% coverage

---

## Phase 2 — SDLC Expansion (Sprints 4–5)

### Goal
Add implementation and verification agents to complete a software development workflow (Gate 4 and Gate 5).

### Sprint 4 — Software Development & Configuration Management Agents
**Dates**: June 21–July 4, 2026  
**Goal**: Add Development and Configuration Management agents.

**Deliverables**:
- Software Development Agent (new)
- Configuration Management Agent (new)
- Code generation stubs (simplified for testing)
- Baseline register and change control tracking
- Integration test: intake → Gate 4 (Implementation Ready)

**Agents Delivered**: 8 (6 + Development + Configuration Management)  
**Gate 4 Criteria**:
- Requirements linked to generated code stubs
- CM baseline established and change log started
- Configuration tags applied to artifacts

---

### Sprint 5 — Verification & Validation Agent
**Dates**: July 5–18, 2026  
**Goal**: Add V&V agent to verify requirements against tests.

**Deliverables**:
- Verification & Validation Agent (new)
- Test plan generation and coverage tracking
- Requirements-to-Test mapping
- Integration test: intake → Gate 5 (Verification Complete)

**Agents Delivered**: 9 (8 + V&V)  
**Gate 5 Criteria**:
- All requirements linked to test cases
- Test coverage ≥80%
- V&V sign-off on requirement-test traceability

**Phase 2 Exit Criteria**:
- ✅ 9 agents implemented
- ✅ Full SDLC workflow: intake → Gate 5
- ✅ Code generation, testing, verification working

---

## Phase 3 — Persistent Multi-Run Operations (Sprint 6)

### Goal
Add robust checkpointing, recovery, long-horizon planning, and observability dashboards.

### Sprint 6 — Persistence & Observability
**Dates**: July 19–August 1, 2026  
**Goal**: Enhance checkpointing for multi-hour workflows; add metrics dashboard.

**Deliverables**:
- Enhanced PostgreSQL checkpointing with transaction rollback
- Workflow resumption from arbitrary point
- Metrics collection: agent execution time, gate transition times, error rates
- Structured logging to observability backend (ELK or similar stub)
- Health dashboard with historical metrics

**Phase 3 Exit Criteria**:
- ✅ Multi-hour workflows can pause/resume without data loss
- ✅ Observability dashboard functional

---

## Phase 4 — Advanced Capabilities (Sprints 7–8)

### Goal
Add multi-model routing, advanced compliance evidence, and scalable orchestration patterns.

### Sprint 7 — Multi-Model Routing & Role-Based Policies
**Dates**: August 2–15, 2026  
**Goal**: Enable different models for different agent roles based on complexity/latency requirements.

**Deliverables**:
- Multi-model inference layer (route by agent role and task type)
- Role-based model policies (e.g., Requirements uses fast model, Architecture uses larger model)
- Model performance tracking and adaptive selection

---

### Sprint 8 — Advanced Compliance & Automation
**Dates**: August 16–29, 2026  
**Goal**: Deepen compliance evidence generation; add remaining agents (QA, Integration, Data Management).

**Deliverables**:
- Quality Assurance Agent (new)
- Integration & Test Agent (new)
- Data Management Agent (new)
- Advanced compliance evidence generation (waiver management, risk acceptance)
- Multi-team orchestration patterns

**Agents Delivered**: 12 (9 + QA + Integration + Data Management)  
**Phase 4 Exit Criteria**:
- ✅ Full 12-agent system operational
- ✅ Advanced compliance and governance features enabled
- ✅ Multi-team orchestration demonstrated

---

## Cumulative Feature Timeline

| Sprint | Agents | Major Capability | Phase |
|--------|--------|-----------------|-------|
| 0 | 4 | Multi-agent orchestration, state persistence, HITL framework, governance baseline | 0 |
| 1 | 4 | Planning infrastructure, architecture decomposition, CI/CD | 1 |
| 2 | 5 | Requirements agent with full hierarchy and noun-SHALL-verb | 1 |
| 3 | 6 | Safety/Security agent, architecture review, integration test | 1 |
| 4 | 8 | Development & CM agents, code generation stubs | 2 |
| 5 | 9 | V&V agent, test planning and coverage tracking | 2 |
| 6 | 9 | Persistent checkpointing, observability dashboard | 3 |
| 7 | 9 | Multi-model routing, role-based policies | 4 |
| 8 | 12 | QA, Integration, Data Management agents, advanced compliance | 4 |

---

## Risk-Based Prioritization

### Critical Path (Must Complete)
1. Sprint 1 — Architecture framework (enables all downstream planning)
2. Sprint 2 — Requirements agent (foundation for all subsequent requirements)
3. Sprint 3 — Integration test (proves system works end-to-end)
4. Sprint 4–5 — Development + V&V (completes basic SDLC)

### Defer-Capable (Phase 4)
- Sprint 7–8 — Advanced agents and multi-model routing (nice-to-have for MVP but not blocking)

### Contingency Plan
If any sprint slips by more than 3 days:
- Defer non-critical agents (QA, Data Management) to post-Phase-4 release
- Extend Sprints 7–8 or split into Sprint 8–9
- Maintain Gate 1–5 schedule (requirements through verification is non-negotiable)

---

## Success Metrics by Phase

| Phase | Exit Criterion | Verification |
|-------|---|---|
| **0** | Foundation operational | CLI works, agents update state, checkpointing saves/restores |
| **1** | MVP workflow end-to-end | Intake → Gate 3 integration test passes |
| **2** | Full SDLC coverage | Intake → Gate 5 integration test passes, 9 agents active |
| **3** | Production-grade durability | Multi-hour workflow resume test passes, dashboard shows metrics |
| **4** | Enterprise ready | 12 agents, multi-model routing, advanced compliance features working |

---

## Gate Review Schedule

| Gate | Sprint Close Date | HITL Review | Approval Authority |
|------|---|---|---|
| Gate 1 (Intake) | May 23 | Sprint planning, backlog review | Chief Engineer |
| Gate 2 (Requirements) | June 6 | Requirements review board | Chief Engineer + Requirements Agent |
| Gate 3 (Architecture) | June 20 | Architecture review board | Chief Engineer + Architecture Agent |
| Gate 4 (Implementation) | July 4 | Code review, CM baseline | Development Team Lead |
| Gate 5 (Verification) | July 18 | V&V sign-off | QA / V&V Agent |
| Phase 3 Readiness | August 1 | Persistence/observability demo | Chief Engineer |
| Phase 4 Readiness | August 29 | Full system demo, compliance evidence | Chief Engineer + Program Manager |

---

## Dependencies Between Sprints

```
Sprint 0 (Foundation)
  ↓
Sprint 1 (Planning & Infrastructure)
  ├─ Sprint 2 (Requirements Agent) — blocks Gate 2
  │   ├─ Sprint 3 (Safety Agent) — blocks Gate 3
  │   │   ├─ Sprint 4 (Development Agent) — blocks Gate 4
  │   │   │   └─ Sprint 5 (V&V Agent) — blocks Gate 5
  │   │   │       └─ Sprint 6 (Persistence & Observability)
  │   │   │           ├─ Sprint 7 (Multi-Model Routing)
  │   │   │           └─ Sprint 8 (Advanced Compliance & Remaining Agents)
  │   │   └─ (no Sprint 4/5 dependency on Sprint 3; parallel ok)
  └─ (no Sprint 2 dependency on Sprint 1; parallel possible but not recommended)
```

**Critical Path**: Sprints 0 → 1 → 2 → 3 → 4 → 5 → 6 (serial)  
**Non-Critical**: Sprints 7–8 can run in parallel with 6 or follow sequentially

---

## Resource Allocation

Assuming **1 full-time developer** (you):
- Each sprint assumes ~40 productive hours (80 hours − meeting/planning overhead)
- Current estimate: ~31 hours per sprint average
- Buffer: ~9 hours per sprint for contingency

If additional resources available:
- Parallel agent development possible starting Sprint 4 (Development + CM in parallel with Sprint 3)
- Safety/Security could be off-loaded to contractor in Sprint 3

---

## Post-Phase-4 Roadmap (Future)

Beyond Sprint 8, potential enhancements:
- **Multi-Org Orchestration**: Coordinate multiple teams across different programs
- **AI-Driven Trade Studies**: Automated constraint solving and design space exploration
- **Continuous Integration to Production**: Automated deployment pipelines
- **Learning & Feedback Loops**: Agent performance metrics driving model retraining
- **Compliance Automation**: Automated waiver generation and risk acceptance workflows
