# Product Requirements Register

**Document ID**: PRR-001  
**Plan Reference**: RMP-PLAN-001 (Requirements Management Plan)  
**Policy Reference**: RMP-001  
**Date**: 2026-05-08  
**Status**: DRAFT — Pending Gate 2 Baseline

> All requirements follow the noun-SHALL-verb format and **four-level hierarchy** defined in RMP-PLAN-001 §2.  
> L0→L1→L2→L3 represents increasing implementation detail. L0/L1 are verified by rollup from their children.  
> Prefix legend: `SH` Stakeholder | `SYS` System | `AGT` Agent | `GOV` Governance | `HITL` Human-in-the-Loop | `INFRA` Infrastructure | `SEC` Security | `PERF` Performance | `INT` Interface | `DATA` Data | `TEST` Test/Verification

---

## Hierarchy Overview

```
L0 — Stakeholder Needs (what the people building complex programs need)
  ├─ SH-0001  Automated SDLC Discipline
  ├─ SH-0002  Local / Secure Operation
  ├─ SH-0003  Human Authority Preserved
  └─ SH-0004  Verifiable Governance Evidence

L1 — System Requirements (what Agentic-SDLC-AI must do)
  ├─ SYS-0001  Multi-Agent Orchestration          ← SH-0001
  ├─ SYS-0002  Shared State Persistence           ← SH-0001
  ├─ SYS-0003  Human-in-the-Loop Gateway          ← SH-0003
  ├─ SYS-0004  Local LLM Inference                ← SH-0002
  ├─ SYS-0005  End-to-End SDLC Coverage           ← SH-0001
  └─ SYS-0006  Governance Evidence Generation     ← SH-0004

L2 — Subsystem / Component Requirements (what each agent/module must do)
  ├─ AGT-0001  Agent Governance Output Contract   ← SYS-0006
  ├─ AGT-0002  Requirements Noun-SHALL-Verb       ← SYS-0005
  ├─ AGT-0003  Unique Requirement ID Assignment   ← AGT-0002
  ├─ AGT-0004  Full Attribute Population          ← AGT-0002
  ├─ AGT-0005  Requirements Hierarchy Decomp.     ← AGT-0002
  ├─ GOV-0001  Automated Gate Evidence Validation ← SYS-0006
  ├─ GOV-0002  RTM Generation                     ← SYS-0006
  ├─ HITL-0001 Complete Evidence Presentation     ← SYS-0003
  ├─ INFRA-0001 CI/CD Pipeline with Coverage Gate ← SYS-0001
  └─ INFRA-0002 Mock LLM Mode for Testing         ← INFRA-0001

L3 — Implementation Requirements (precise constraints narrowing how L2 is satisfied)
  ├─ AGT-0010  Requirement Format Validation Rule ← AGT-0002
  ├─ AGT-0011  ID Uniqueness Enforcement          ← AGT-0003
  ├─ AGT-0012  Orphan Detection and Reporting     ← AGT-0005
  ├─ GOV-0010  Gate Hook Intercept Contract       ← GOV-0001
  └─ INFRA-0010 Coverage Threshold Enforcement   ← INFRA-0001
```

---

## L0 — Stakeholder Needs

### SH-0001 — Automated SDLC Discipline

| Field | Value |
|-------|-------|
| **ID** | SH-0001 |
| **Short Name** | Automated SDLC Discipline |
| **Level** | L0-Stakeholder |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | Project vision, README.md |
| **Trace: Parent** | ORIGIN |
| **Trace: Children** | SYS-0001, SYS-0002, SYS-0005 |
| **Trace: Work Item** | — (L0: verified by children) |
| **Trace: Test** | — (rollup: verified when all children VERIFIED) |

**Requirement Text**  
The Agentic-SDLC-AI system SHALL enable engineering organizations to execute rigorous, multi-phase SDLC workflows for complex software programs using coordinated AI agents without requiring manual handoffs between phases.

**Rationale**  
Complex programs involving systems engineering, safety, security, and compliance disciplines require consistent process discipline that human teams struggle to maintain at scale. AI agent automation provides disciplined repeatability across every project phase.

**Verification Method(s)**  
Demonstration

**Verification Statement**  
Verified when children SYS-0001, SYS-0002, and SYS-0005 are all in VERIFIED status.

---

### SH-0002 — Local and Secure Operation

| Field | Value |
|-------|-------|
| **ID** | SH-0002 |
| **Short Name** | Local and Secure Operation |
| **Level** | L0-Stakeholder |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/hardware-requirements.md |
| **Trace: Parent** | ORIGIN |
| **Trace: Children** | SYS-0004 |
| **Trace: Work Item** | — |
| **Trace: Test** | — (rollup: verified when SYS-0004 VERIFIED) |

**Requirement Text**  
The Agentic-SDLC-AI system SHALL operate entirely within a locally controlled environment so that sensitive program data, requirements, and architecture artifacts are never transmitted to external services.

**Rationale**  
Programs in regulated industries (defense, aerospace, medical) cannot route project data through cloud APIs. Local-only operation is a non-negotiable constraint for adoption in these environments.

**Verification Method(s)**  
Inspection

**Verification Statement**  
Verified when child SYS-0004 is in VERIFIED status.

---

### SH-0003 — Human Authority Preserved

| Field | Value |
|-------|-------|
| **ID** | SH-0003 |
| **Short Name** | Human Authority Preserved |
| **Level** | L0-Stakeholder |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/plans/hitl-governance-plan.md |
| **Trace: Parent** | ORIGIN |
| **Trace: Children** | SYS-0003 |
| **Trace: Work Item** | — |
| **Trace: Test** | — (rollup: verified when SYS-0003 VERIFIED) |

**Requirement Text**  
The Agentic-SDLC-AI system SHALL preserve human decision-making authority at every critical lifecycle gate so that no consequential engineering commitment is made autonomously without explicit human approval.

**Rationale**  
AI systems making irreversible engineering decisions without human oversight present unacceptable technical and organizational risk. Stakeholders must retain authority to approve, reject, or redirect at defined checkpoints.

**Verification Method(s)**  
Demonstration

**Verification Statement**  
Verified when child SYS-0003 is in VERIFIED status.

---

### SH-0004 — Verifiable Governance Evidence

| Field | Value |
|-------|-------|
| **ID** | SH-0004 |
| **Short Name** | Verifiable Governance Evidence |
| **Level** | L0-Stakeholder |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/policies/systems-engineering-management-policy.md |
| **Trace: Parent** | ORIGIN |
| **Trace: Children** | SYS-0006 |
| **Trace: Work Item** | — |
| **Trace: Test** | — (rollup: verified when SYS-0006 VERIFIED) |

**Requirement Text**  
The Agentic-SDLC-AI system SHALL generate machine-readable, auditable governance evidence at every lifecycle gate so that compliance with program policies can be verified independently of the agents that produced the work.

**Rationale**  
Compliance audits require objective evidence that processes were followed. Agent-produced outputs lacking structured, policy-linked evidence cannot satisfy audit requirements.

**Verification Method(s)**  
Inspection, Test

**Verification Statement**  
Verified when child SYS-0006 is in VERIFIED status.

---

## L1 — System Requirements

### SYS-0001 — Multi-Agent Orchestration

| Field | Value |
|-------|-------|
| **ID** | SYS-0001 |
| **Short Name** | Multi-Agent Orchestration |
| **Level** | L1-System |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | README.md, docs/architecture.md |

---

## Sprint 3 Derived Requirements (Execution Update)

### SEC-0100 — Architecture Threat Model Artifact

**Requirement Text**  
The system SHALL generate an architecture-phase threat model artifact containing at least one identified threat scenario, severity, and mitigation linkage before Gate 3 readiness evaluation.

**Traceability**  
- Parent: SYS-0006
- Work Item: Sprint 3
- Verification: `tests/integration/test_e2e_intake_to_gate3.py`

### SAF-0100 — Architecture Hazard Log Artifact

**Requirement Text**  
The system SHALL generate an architecture-phase hazard log containing hazard identifiers, likelihood, severity, and mitigations before Gate 3 readiness evaluation.

**Traceability**  
- Parent: SYS-0006
- Work Item: Sprint 3
- Verification: `tests/integration/test_e2e_intake_to_gate3.py`

### REL-0100 — Architecture Reliability Assessment Artifact

**Requirement Text**  
The system SHALL generate an architecture-phase reliability risk artifact including failure modes, detection strategy, and resilience controls before Gate 3 readiness evaluation.

**Traceability**  
- Parent: SYS-0006
- Work Item: Sprint 3
- Verification: `tests/integration/test_e2e_intake_to_gate3.py`

### DEV-0200 — Requirement-Linked Code Stub Generation

**Requirement Text**  
The system SHALL generate requirement-linked implementation stubs during the implementation phase and include them in Gate 4 evidence.

**Traceability**  
- Parent: SYS-0005
- Work Item: Sprint 4
- Verification: `tests/integration/test_e2e_intake_to_gate4.py`

### CM-0200 — Configuration Baseline and Change Log Evidence

**Requirement Text**  
The system SHALL produce configuration baseline updates, configuration tags, and change control log entries before Gate 4 readiness evaluation.

**Traceability**  
- Parent: SYS-0006
- Work Item: Sprint 4
- Verification: `tests/integration/test_e2e_intake_to_gate4.py`

### VNV-0300 — Requirement-to-Test Traceability and Coverage Evidence

**Requirement Text**  
The system SHALL generate verification-phase artifacts that map all active requirements to test cases, report coverage of at least 80 percent, and include V&V sign-off before Gate 5 readiness declaration.

**Traceability**  
- Parent: SYS-0005
- Work Item: Sprint 5
- Verification: `tests/integration/test_e2e_intake_to_gate5.py`

### PERS-0400 — Checkpoint Restore Points and Rollback Semantics

**Requirement Text**  
The system SHALL persist checkpoint restore points per workflow session and support rollback to an arbitrary restore point without losing subsequent session continuity.

**Traceability**  
- Parent: SYS-0002
- Work Item: Sprint 6
- Verification: `tests/integration/test_persistence_snapshots.py`

### OBS-0400 — Historical Observability Metrics and Structured Logging Stub

**Requirement Text**  
The system SHALL record agent execution metrics, phase transition timing, error-rate data, and structured observability events to a backend stub that can be visualized in a historical dashboard view.

**Traceability**  
- Parent: SYS-0006
- Work Item: Sprint 6
- Verification: `tests/unit/test_kpi_tracker.py`

### MMR-0500 — Role and Complexity Aware Model Routing with Adaptive Fallback

**Requirement Text**  
The system SHALL select inference models per agent role and estimated task complexity, record model-selection telemetry, and adaptively fallback to alternate configured models when runtime error or latency thresholds are exceeded.

**Traceability**  
- Parent: SYS-0004
- Work Item: Sprint 7
- Verification: `tests/unit/test_model_router.py`, `tests/unit/test_kpi_tracker.py`

### AC8-0600 — Quality Assurance, Integration and Test, and Data Management Agents

**Requirement Text**  
The system SHALL execute Quality Assurance, Integration and Test, and Data Management agents within the multi-agent orchestration to extend specialist role coverage to 12 agents supporting advanced compliance evidence generation (waivers, risk acceptance) and multi-team orchestration patterns.

**Traceability**  
- Parent: SYS-0001
- Work Item: Sprint 8
- Verification: `tests/unit/test_sprint8_agents.py`

### AC8-0610 — Advanced Compliance Waivers and Risk Acceptance

**Requirement Text**  
The system SHALL persist and report approved compliance waivers with justification and explicit risk acceptances with owner signature, enabling organizations to document intentional policy deviations with accountability.

**Traceability**  
- Parent: SYS-0006
- Work Item: Sprint 8
- Verification: `src/state/schema.py` (waivers, risk_acceptances fields)
Derived from SH-0001 to address the orchestration mechanism. A single monolithic agent cannot provide the role separation, authority delegation, and specialization required for rigorous systems engineering.

**Verification Method(s)**  
Test, Demonstration

**Verification Statement**  
Integration test invokes `build_supervisor_graph()` and asserts multi-agent state updates. Verified when children AGT-0001 and INFRA-0001 reach VERIFIED.

---

### SYS-0002 — Shared State Persistence

| Field | Value |
|-------|-------|
| **ID** | SYS-0002 |
| **Short Name** | Shared State Persistence |
| **Level** | L1-System |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/architecture.md |
| **Trace: Parent** | SH-0001 |
| **Trace: Children** | NONE (L2 TBD Sprint 2) |
| **Trace: Work Item** | Sprint 0 (complete) |
| **Trace: Test** | tests/unit/test_base_agent.py |

**Requirement Text**  
The system SHALL persist all agent state, decisions, requirements, and risks to a PostgreSQL database using LangGraph checkpointing so multi-run workflows can resume after interruption.

**Rationale**  
Derived from SH-0001. Complex SDLC workflows span hours or days; without durable persistence, failures lose all prior work.

**Verification Method(s)**  
Test

**Verification Statement**  
Test invokes a graph run, interrupts mid-flight, resumes from same `thread_id`, and asserts prior state is restored from PostgreSQL.

---

### SYS-0003 — Human-in-the-Loop Gateway

| Field | Value |
|-------|-------|
| **ID** | SYS-0003 |
| **Short Name** | HITL Gateway |
| **Level** | L1-System |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/plans/hitl-governance-plan.md |
| **Trace: Parent** | SH-0003 |
| **Trace: Children** | HITL-0001 |
| **Trace: Work Item** | Sprint 0 (partial), Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The system SHALL pause workflow execution and request human approval at each defined lifecycle gate before permitting phase transitions.

**Rationale**  
Derived from SH-0003. Autonomous AI systems making consequential engineering decisions without human oversight present unacceptable risk.

**Verification Method(s)**  
Demonstration, Test

**Verification Statement**  
Demonstration shows system pausing at Gate 2, presenting evidence package, and preventing advancement without explicit approval. Verified when child HITL-0001 reaches VERIFIED.

---

### SYS-0004 — Local LLM Inference

| Field | Value |
|-------|-------|
| **ID** | SYS-0004 |
| **Short Name** | Local LLM Inference |
| **Level** | L1-System |
| **Status** | APPROVED |
| **Priority** | P2-High |
| **Source** | docs/hardware-requirements.md |
| **Trace: Parent** | SH-0002 |
| **Trace: Children** | NONE (L2 TBD Sprint 3) |
| **Trace: Work Item** | Sprint 0 (complete) |
| **Trace: Test** | scripts/health_check.py |

**Requirement Text**  
The system SHALL execute all LLM inference locally using Ollama so that no project data, requirements, or architecture artifacts are transmitted to external cloud services.

**Rationale**  
Derived from SH-0002. Regulated industries (defense, aerospace, medical) cannot route project data through cloud APIs.

**Verification Method(s)**  
Inspection, Test

**Verification Statement**  
Inspection of `src/config/settings.py` confirms `OLLAMA_BASE_URL` points to localhost. Health check test confirms Ollama responds on configured local address.

---

### SYS-0005 — End-to-End SDLC Coverage

| Field | Value |
|-------|-------|
| **ID** | SYS-0005 |
| **Short Name** | End-to-End SDLC Coverage |
| **Level** | L1-System |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/agent-roles.md, docs/roadmap.md |
| **Trace: Parent** | SH-0001 |
| **Trace: Children** | AGT-0002 |
| **Trace: Work Item** | Sprints 1–3 (phased) |
| **Trace: Test** | TBD — Sprint 3 end-to-end |

**Requirement Text**  
The system SHALL provide specialized agents covering all major SDLC disciplines — requirements, architecture, safety/security, software development, verification, configuration management, data management, integration, and quality assurance — so that every phase of a program lifecycle can be executed by the system.

**Rationale**  
Derived from SH-0001. Gaps in agent coverage leave entire SDLC phases unsupported, breaking automated workflow.

**Verification Method(s)**  
Inspection, Test

**Verification Statement**  
Verified when all L2 agent requirements (AGT-0002 and siblings) are VERIFIED through Sprint 3.

---

### SYS-0006 — Governance Evidence Generation

| Field | Value |
|-------|-------|
| **ID** | SYS-0006 |
| **Short Name** | Governance Evidence Generation |
| **Level** | L1-System |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/governance/policy-agent-enforcement-matrix.md |
| **Trace: Parent** | SH-0004 |
| **Trace: Children** | AGT-0001, GOV-0001, GOV-0002 |
| **Trace: Work Item** | Sprints 0–2 (phased) |
| **Trace: Test** | tests/unit/test_governance_*.py |

**Requirement Text**  
The system SHALL produce structured, policy-linked governance evidence at every lifecycle gate that can be independently validated without re-executing the agents that produced the work.

**Rationale**  
Derived from SH-0004. Agent outputs must carry auditable evidence payloads so HITL reviewers and automated gate hooks can confirm compliance.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
Verified when children AGT-0001, GOV-0001, and GOV-0002 reach VERIFIED status.

---

## L2 — Subsystem / Component Requirements

### AGT-0001 — Agent Governance Output Contract

| Field | Value |
|-------|-------|
| **ID** | AGT-0001 |
| **Short Name** | Agent Governance Output Contract |
| **Level** | L2-Subsystem |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/governance/policy-agent-enforcement-matrix.md |
| **Trace: Parent** | SYS-0006 |
| **Trace: Children** | GOV-0010 |
| **Trace: Work Item** | Sprint 0 (complete) |
| **Trace: Test** | tests/unit/test_agent_governance_output_contract.py |

**Requirement Text**  
Every agent SHALL emit a structured governance output payload containing `policy_compliance`, `traceability_links`, `gate_readiness`, `evidence_links`, and `risks_or_blockers` fields when completing a phase transition.

**Rationale**  
Derived from SYS-0006. HITL reviewers and automated gate hooks need a consistent, machine-readable evidence package from each agent.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
Test asserts `build_governance_output()` returns dict with all five required keys. Inspection confirms payload included in each agent's state update.

---

### AGT-0002 — Requirements Noun-SHALL-Verb Elicitation

| Field | Value |
|-------|-------|
| **ID** | AGT-0002 |
| **Short Name** | Requirements Noun-SHALL-Verb Elicitation |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | RMP-PLAN-001 §2.1 |
| **Trace: Parent** | SYS-0005 |
| **Trace: Children** | AGT-0003, AGT-0004, AGT-0005, AGT-0010 |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The Requirements Development Agent SHALL elicit and record all requirements in noun-SHALL-verb format and flag any elicited requirement that does not conform before accepting it.

**Rationale**  
Derived from SYS-0005. Consistent syntax is prerequisite to automated parsing, traceability linking, and verification mapping.

**Verification Method(s)**  
Test

**Verification Statement**  
Test submits conforming and non-conforming candidates and asserts non-conforming ones are flagged while conforming ones are accepted with populated attributes.

---

### AGT-0003 — Unique Requirement ID Assignment

| Field | Value |
|-------|-------|
| **ID** | AGT-0003 |
| **Short Name** | Unique Requirement ID Assignment |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | RMP-PLAN-001 §2.2 |
| **Trace: Parent** | AGT-0002 |
| **Trace: Children** | AGT-0011 |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The Requirements Development Agent SHALL assign unique identifiers following `[PREFIX]-[NNNN]` scheme and never reuse IDs, including for RETIRED requirements.

**Rationale**  
Derived from AGT-0002. Unique, stable IDs enable unambiguous traceability across all artifact levels.

**Verification Method(s)**  
Test

**Verification Statement**  
Test retires a requirement, creates a new one in same domain, and asserts new ID is distinct from all prior IDs including retired ones.

---

### AGT-0004 — Full Attribute Population

| Field | Value |
|-------|-------|
| **ID** | AGT-0004 |
| **Short Name** | Full Attribute Population |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | RMP-PLAN-001 §2.3 |
| **Trace: Parent** | AGT-0002 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The Requirements Development Agent SHALL populate all mandatory attributes including Level, Trace:Parent, and Trace:Children before marking APPROVED and reject transitions when attributes are absent.

**Rationale**  
Derived from AGT-0002. Incomplete records cannot be verified or managed. Level and parent/child links are mandatory for hierarchy validation.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
Test attempts APPROVED status with absent mandatory attributes and asserts rejection. Inspection of `Requirement` Pydantic model confirms all mandatory fields are non-optional.

---

### AGT-0005 — Requirements Hierarchy Decomposition

| Field | Value |
|-------|-------|
| **ID** | AGT-0005 |
| **Short Name** | Requirements Hierarchy Decomposition |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | RMP-PLAN-001 §2.4 |
| **Trace: Parent** | AGT-0002 |
| **Trace: Children** | AGT-0012 |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The Requirements Development Agent SHALL enforce the four-level hierarchy (L0→L1→L2→L3) by detecting and reporting orphan requirements with no parent link and decomposition gaps where non-leaf requirements lack children.

**Rationale**  
Derived from AGT-0002. Without hierarchy enforcement, requirements accumulate at single level with no traceable derivation path.

**Verification Method(s)**  
Test

**Verification Statement**  
Test creates L1 with no L2 children and asserts decomposition gap reported. Test creates L2 with no L1 parent and asserts orphan violation reported.

---

### GOV-0001 — Automated Gate Evidence Validation

| Field | Value |
|-------|-------|
| **ID** | GOV-0001 |
| **Short Name** | Automated Gate Evidence Validation |
| **Level** | L2-Subsystem |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/governance/lifecycle-gate-checklists.md |
| **Trace: Parent** | SYS-0006 |
| **Trace: Children** | GOV-0010 |
| **Trace: Work Item** | Sprint 0 (complete) |
| **Trace: Test** | tests/unit/test_governance_validation.py |

**Requirement Text**  
The supervisor graph SHALL automatically invoke governance evidence validator before permitting any phase transition where an agent declares gate readiness READY.

**Rationale**  
Derived from SYS-0006. Manual-only enforcement is unreliable and will not scale as agents multiply.

**Verification Method(s)**  
Test

**Verification Statement**  
Test asserts missing evidence causes `requires_human_approval=True` and `gate_readiness_status=NOT_READY`.

---

### GOV-0002 — RTM Generation

| Field | Value |
|-------|-------|
| **ID** | GOV-0002 |
| **Short Name** | RTM Generation |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P2-High |
| **Source** | RMP-001 §Traceability Rules |
| **Trace: Parent** | SYS-0006 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 3 |
| **Trace: Test** | TBD — Sprint 3 |

**Requirement Text**  
The system SHALL generate a Requirements Traceability Matrix (RTM) mapping each requirement across all four hierarchy levels to architecture elements, work items, and test cases, and include RTM in Gate 2 evidence package.

**Rationale**  
Derived from SYS-0006. RTM is the primary audit artifact demonstrating requirements are implemented and tested.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
Test runs requirements-to-Gate-2 workflow and asserts RTM in evidence package with hierarchy-level annotations.

---

### HITL-0001 — Complete Evidence Package Presentation

| Field | Value |
|-------|-------|
| **ID** | HITL-0001 |
| **Short Name** | Complete Evidence Package Presentation |
| **Level** | L2-Subsystem |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/plans/hitl-governance-plan.md |
| **Trace: Parent** | SYS-0003 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The HITL gateway SHALL present the human reviewer with the full governance evidence package — policy compliance, traceability links, gate readiness, evidence links, and unresolved risks — before requesting approval decision.

**Rationale**  
Derived from SYS-0003. Reviewers lacking full evidence context may inadvertently approve incomplete work.

**Verification Method(s)**  
Demonstration, Test

**Verification Statement**  
Demonstration shows all five evidence fields displayed before approval prompt. Test asserts missing fields raise error before approval request.

---

### INFRA-0001 — CI/CD Pipeline with Coverage Gate

| Field | Value |
|-------|-------|
| **ID** | INFRA-0001 |
| **Short Name** | CI/CD Pipeline with Coverage Gate |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | docs/plans/software-development-plan.md |
| **Trace: Parent** | SYS-0001 |
| **Trace: Children** | INFRA-0010 |
| **Trace: Work Item** | Sprint 1 |
| **Trace: Test** | .github/workflows/ci.yml |

**Requirement Text**  
The project SHALL maintain GitHub Actions CI/CD pipeline running linting, unit tests, and coverage checks on every PR and blocking merges when coverage falls below 80%.

**Rationale**  
Derived from SYS-0001. Without automated CI enforcement, code quality and test coverage degrade incrementally.

**Verification Method(s)**  
Inspection, Test

**Verification Statement**  
Inspection of `ci.yml` confirms lint, test, coverage steps. Test PR with uncovered code fails coverage check and blocks merge.

---

### INFRA-0002 — Mock LLM Mode for Testing

| Field | Value |
|-------|-------|
| **ID** | INFRA-0002 |
| **Short Name** | Mock LLM Mode for Testing |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | Risk Register — Ollama speed in CI |
| **Trace: Parent** | INFRA-0001 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 1 |
| **Trace: Test** | tests/conftest.py |

**Requirement Text**  
The test infrastructure SHALL provide a mock LLM stub replacing Ollama for all unit and integration tests so tests run without live Ollama and complete in under 60 seconds.

**Rationale**  
Derived from INFRA-0001. Live Ollama in CI makes pipeline slow and hardware-dependent.

**Verification Method(s)**  
Test

**Verification Statement**  
Full unit test suite runs with Ollama unavailable, all tests pass in under 60 seconds total.

---

## L3 — Implementation Requirements

### AGT-0010 — Requirement Format Validation Rule

| Field | Value |
|-------|-------|
| **ID** | AGT-0010 |
| **Short Name** | Requirement Format Validation Rule |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | RMP-PLAN-001 §2.1 |
| **Trace: Parent** | AGT-0002 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The Requirements Development Agent's format validator SHALL reject requirement text not matching `<noun phrase> SHALL <verb phrase>` pattern and return error message identifying offending text and violated rule.

**Rationale**  
Derived from AGT-0002 to specify exact validation rule. Regex or grammar-based check provides deterministic enforcement.

**Verification Method(s)**  
Test

**Verification Statement**  
Test passes requirement strings with missing SHALL, verb-only, and imperative forms to validator and asserts each returns `FormatViolation` with error message.

---

### AGT-0011 — ID Uniqueness Enforcement

| Field | Value |
|-------|-------|
| **ID** | AGT-0011 |
| **Short Name** | ID Uniqueness Enforcement |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | RMP-PLAN-001 §2.2 |
| **Trace: Parent** | AGT-0003 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The Requirements Development Agent SHALL maintain persistent ID registry in `AgentState` and raise error if any attempt assigns ID already in registry, whether ACTIVE or RETIRED.

**Rationale**  
Derived from AGT-0003. ID uniqueness must be enforced at state level to survive session interruptions.

**Verification Method(s)**  
Test

**Verification Statement**  
Test serializes state with retired ID to checkpoint, resumes session, attempts new requirement with same ID, and asserts `IDConflictError` raised.

---

### AGT-0012 — Orphan Detection and Reporting

| Field | Value |
|-------|-------|
| **ID** | AGT-0012 |
| **Short Name** | Orphan Detection and Reporting |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P2-High |
| **Source** | RMP-PLAN-001 §2.4 Decomposition Rules |
| **Trace: Parent** | AGT-0005 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The Requirements Development Agent SHALL scan requirements register at Gate 2 and produce orphan report listing every L1 requirement with no L0 parent, every L2 with no L1 parent, and every non-leaf requirement lacking children.

**Rationale**  
Derived from AGT-0005 to specify reporting artifact. Structured report gives Gate 2 reviewer actionable hierarchy completeness information.

**Verification Method(s)**  
Test

**Verification Statement**  
Test populates register with deliberate orphans and gaps, triggers Gate 2 scan, and asserts orphan report identifies each violation by ID with rule violated.

---

### GOV-0010 — Gate Hook Intercept Contract

| Field | Value |
|-------|-------|
| **ID** | GOV-0010 |
| **Short Name** | Gate Hook Intercept Contract |
| **Level** | L3-Implementation |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | src/graphs/supervisor.py |
| **Trace: Parent** | GOV-0001 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 0 (complete) |
| **Trace: Test** | tests/unit/test_supervisor_governance_hook.py |

**Requirement Text**  
The supervisor gate hook SHALL intercept every node update setting `gate_readiness.status` to READY, invoke `validate_outputs()`, and if validation fails SHALL remove phase transition, set `gate_readiness_status` to NOT_READY, and set `requires_human_approval` to True.

**Rationale**  
Derived from GOV-0001. Exact intercept-and-downgrade contract must be specified so implementation can be tested precisely.

**Verification Method(s)**  
Test

**Verification Statement**  
Test asserts all three post-failure state mutations present: transition removed, status NOT_READY, approval required.

---

### INFRA-0010 — Coverage Threshold Enforcement

| Field | Value |
|-------|-------|
| **ID** | INFRA-0010 |
| **Short Name** | Coverage Threshold Enforcement |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | INFRA-0001 |
| **Trace: Parent** | INFRA-0001 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 1 |
| **Trace: Test** | .github/workflows/ci.yml |

**Requirement Text**  
The CI pipeline SHALL use `pytest-cov` with `--cov-fail-under=80` threshold and fail pipeline step — preventing merge — if overall branch coverage across `src/` drops below 80%.

**Rationale**  
Derived from INFRA-0001 to specify exact tool and threshold. Concrete threshold prevents slow degradation.

**Verification Method(s)**  
Inspection, Test

**Verification Statement**  
Inspection confirms `--cov-fail-under=80` in pytest invocation. Test branch reducing coverage below 80% causes CI job to exit non-zero.

---

## Architecture Requirements

### ARCH-0001 — System Architecture Decomposition Structure

| Field | Value |
|-------|-------|
| **ID** | ARCH-0001 |
| **Short Name** | System Architecture Decomposition Structure |
| **Level** | L1-System |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | PROJECT_PLAN.md, Sprint 1 planning |
| **Trace: Parent** | ORIGIN |
| **Trace: Children** | ARCH-0002, ARCH-0003, ARCH-0004, ARCH-0005 |
| **Trace: Work Item** | Sprint 1 |
| **Trace: Test** | docs/architecture/DECOMPOSITION_STRUCTURE.md (inspection) |

**Requirement Text**  
The architecture decomposition structure of Agentic-SDLC-AI SHALL define all physical and logical component layers — Hardware Environment, Software Framework, Agent Subsystem, HITL/HMI Framework, and Governance Layer — with each layer subdivided into components and documented in a formal architecture decomposition matrix.

**Rationale**  
A multi-agent system requires clear component boundaries and layered structure to support requirements traceability, interface specification, and team coordination. Without a formal decomposition structure, requirements cannot be reliably allocated to components, and component interactions become ambiguous.

**Verification Method(s)**  
Inspection, Analysis

**Verification Statement**  
Inspection of `docs/architecture/DECOMPOSITION_STRUCTURE.md` confirms all planned layers are defined with sub-components listed. Analysis of requirements-to-component mappings shows every L2/L3 requirement traces to at least one component.

---

### ARCH-0002 — Hardware Environment Decomposition

| Field | Value |
|-------|-------|
| **ID** | ARCH-0002 |
| **Short Name** | Hardware Environment Decomposition |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P2-High |
| **Source** | ARCH-0001, docs/hardware-requirements.md |
| **Trace: Parent** | ARCH-0001 |
| **Trace: Children** | NONE (leaf) |
| **Trace: Work Item** | Sprint 1 |
| **Trace: Test** | docs/architecture/HARDWARE_LAYERS.md |

**Requirement Text**  
The Hardware Environment layer SHALL be decomposed into clearly defined sub-layers — Hardware Configuration/Constraints, Compute Node (CPU/GPU/Memory), Network/Storage, Power/Thermal — with rationale for each sub-layer and specification of constraints that affect Software Environment design.

**Rationale**  
Derived from ARCH-0001. Hardware constraints directly affect software requirements (e.g., memory limits, GPU availability, network latency). Making these layers explicit prevents software design from ignoring feasibility.

**Verification Method(s)**  
Inspection

**Verification Statement**  
Inspection of `docs/architecture/HARDWARE_LAYERS.md` confirms each sub-layer is defined with constraints and affected requirements/design decisions documented.

---

### ARCH-0003 — Software Environment Decomposition

| Field | Value |
|-------|-------|
| **ID** | ARCH-0003 |
| **Short Name** | Software Environment Decomposition |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P2-High |
| **Source** | ARCH-0001 |
| **Trace: Parent** | ARCH-0001 |
| **Trace: Children** | NONE (leaf) |
| **Trace: Work Item** | Sprint 1 |
| **Trace: Test** | docs/architecture/SOFTWARE_LAYERS.md |

**Requirement Text**  
The Software Environment layer SHALL be decomposed into Framework/Orchestration, Agent Subsystem, HITL/HMI Framework, and Governance/Policy Layer, with each layer further subdivided (e.g., Agent Subsystem into individual agent components).

**Rationale**  
Derived from ARCH-0001. Clear software layer separation enables parallel development, interface definition, and independent testing.

**Verification Method(s)**  
Inspection

**Verification Statement**  
Inspection of `docs/architecture/SOFTWARE_LAYERS.md` confirms all layers listed with sub-layers and inter-layer dependencies documented.

---

### ARCH-0004 — Component-to-Requirement Mapping Matrix

| Field | Value |
|-------|-------|
| **ID** | ARCH-0004 |
| **Short Name** | Component-to-Requirement Mapping Matrix |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P2-High |
| **Source** | ARCH-0001, RMP-PLAN-001 |
| **Trace: Parent** | ARCH-0001 |
| **Trace: Children** | NONE (leaf) |
| **Trace: Work Item** | Sprint 1 |
| **Trace: Test** | docs/architecture/REQUIREMENT_COMPONENT_MAP.md |

**Requirement Text**  
An Architecture-Requirement Mapping Matrix SHALL be created showing which component(s) at which layer(s) are responsible for satisfying each L2 and L3 requirement, enabling bidirectional traceability from requirements to components.

**Rationale**  
Derived from ARCH-0001. Bidirectional traceability prevents requirements gaps (unallocated requirements) and orphan components (components not justified by requirements).

**Verification Method(s)**  
Inspection, Analysis

**Verification Statement**  
Inspection confirms matrix covers all L2/L3 requirements. Analysis confirms no requirement has zero components assigned and no component exists without justifying requirement(s).

---

### ARCH-0005 — Interface and Dependency Specification

| Field | Value |
|-------|-------|
| **ID** | ARCH-0005 |
| **Short Name** | Interface and Dependency Specification |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P3-Medium |
| **Source** | ARCH-0001 |
| **Trace: Parent** | ARCH-0001 |
| **Trace: Children** | NONE (leaf) |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | docs/architecture/INTERFACES.md |

**Requirement Text**  
Formal interface specifications SHALL be defined for all inter-layer and intra-layer component interactions, including data types, protocols, error handling, and dependency order.

**Rationale**  
Derived from ARCH-0001. Explicit interfaces enable parallel development and prevent integration surprises.

**Verification Method(s)**  
Inspection

**Verification Statement**  
Inspection of `docs/architecture/INTERFACES.md` confirms interfaces for all identified inter-component interactions.

### SYS-0001 — Multi-Agent Orchestration

| Field | Value |
|-------|-------|
| **ID** | SYS-0001 |
| **Short Name** | Multi-Agent Orchestration |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | README.md, docs/architecture.md |
| **Trace: Parent** | ORIGIN |
| **Trace: Work Item** | Sprint 0 (complete) |
| **Trace: Test** | tests/test_starter_modules.py |

**Requirement Text**  
The Agentic-SDLC-AI system SHALL orchestrate multiple specialized AI agents through a directed LangGraph supervisor graph to execute end-to-end SDLC workflows.

**Rationale**  
A single monolithic agent cannot provide the role separation, authority delegation, and specialization required for rigorous systems engineering. LangGraph's state-machine model provides deterministic orchestration with human interrupt points.

**Verification Method(s)**  
Test, Demonstration

**Verification Statement**  
An integration test SHALL invoke `build_supervisor_graph()`, submit a requirement intake message, and assert that at least Program Manager and Requirements agents each update the shared state before the workflow halts or completes.

---

### SYS-0002 — Shared State Persistence

| Field | Value |
|-------|-------|
| **ID** | SYS-0002 |
| **Short Name** | Shared State Persistence |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/architecture.md, IMPLEMENTATION_SUMMARY.md |
| **Trace: Parent** | ORIGIN |
| **Trace: Work Item** | Sprint 0 (complete) |
| **Trace: Test** | tests/unit/test_base_agent.py |

**Requirement Text**  
The system SHALL persist all agent state, decisions, requirements, and risks to a PostgreSQL database using LangGraph checkpointing so that multi-run workflows can resume after interruption.

**Rationale**  
Complex SDLC workflows span hours or days. Without durable persistence, any failure or human review pause loses all prior work. Checkpointing enables resume, audit, and replay.

**Verification Method(s)**  
Test

**Verification Statement**  
A test SHALL invoke a graph run, interrupt it mid-flight, and then resume from the same `thread_id`, asserting that all prior state fields are restored from the PostgreSQL checkpoint.

---

### SYS-0003 — Human-in-the-Loop Gateway

| Field | Value |
|-------|-------|
| **ID** | SYS-0003 |
| **Short Name** | HITL Gateway |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/plans/hitl-governance-plan.md, HITL-001 |
| **Trace: Parent** | ORIGIN |
| **Trace: Work Item** | Sprint 0 (partial), Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The system SHALL pause workflow execution and request human approval at each defined lifecycle gate before permitting phase transitions.

**Rationale**  
Autonomous AI systems making consequential engineering decisions without human oversight present unacceptable risk. Mandatory HITL gates ensure expert human review at critical decision points.

**Verification Method(s)**  
Demonstration, Test

**Verification Statement**  
A demonstration SHALL show the system pausing at Gate 2, presenting the evidence package to a human reviewer, and preventing state advancement until an explicit `approve` or `reject` response is received. A test SHALL assert that the `requires_human_approval` flag is set when gate validation fails.

---

### SYS-0004 — Local LLM Inference

| Field | Value |
|-------|-------|
| **ID** | SYS-0004 |
| **Short Name** | Local LLM Inference |
| **Status** | APPROVED |
| **Priority** | P2-High |
| **Source** | docs/hardware-requirements.md, README.md |
| **Trace: Parent** | ORIGIN |
| **Trace: Work Item** | Sprint 0 (complete) |
| **Trace: Test** | scripts/health_check.py |

**Requirement Text**  
The system SHALL execute all LLM inference locally using Ollama so that no project data, requirements, or architecture artifacts are transmitted to external cloud services.

**Rationale**  
Programs handling sensitive or proprietary engineering data cannot use cloud-based LLM APIs. Local inference ensures data sovereignty and eliminates per-token API costs.

**Verification Method(s)**  
Inspection, Test

**Verification Statement**  
Inspection of `src/config/settings.py` SHALL confirm `OLLAMA_BASE_URL` points to localhost. A health check test SHALL confirm Ollama responds on the configured local address with the required model loaded.

---

## Agent Requirements

### AGT-0001 — Agent Governance Output Contract

| Field | Value |
|-------|-------|
| **ID** | AGT-0001 |
| **Short Name** | Agent Governance Output Contract |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/governance/policy-agent-enforcement-matrix.md |
| **Trace: Parent** | GOV-0001 |
| **Trace: Work Item** | Sprint 0 (complete) |
| **Trace: Test** | tests/unit/test_agent_governance_output_contract.py |

**Requirement Text**  
Every agent SHALL emit a structured governance output payload containing `policy_compliance`, `traceability_links`, `gate_readiness`, `evidence_links`, and `risks_or_blockers` fields when completing a phase transition.

**Rationale**  
HITL reviewers and automated gate hooks need a consistent, machine-readable evidence package from each agent. Without a contract, governance validation cannot be automated and HITL reviewers lack complete context.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
`tests/unit/test_agent_governance_output_contract.py` SHALL assert that `build_governance_output()` returns a dict containing all five required keys with non-null values. Inspection of each agent's `run()` method SHALL confirm the payload is included in the returned state update.

---

### AGT-0002 — Requirements Noun-SHALL-Verb Elicitation

| Field | Value |
|-------|-------|
| **ID** | AGT-0002 |
| **Short Name** | Requirements Noun-SHALL-Verb Elicitation |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | RMP-PLAN-001 §2.1 |
| **Trace: Parent** | AGT-0001 |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The Requirements Development Agent SHALL elicit and record all requirements in noun-SHALL-verb format and reject or flag any elicited requirement that does not conform to this format.

**Rationale**  
Consistent requirement syntax is prerequisite to automated parsing, traceability linking, and verification mapping. Non-conforming requirements cannot be reliably verified and create ambiguity in implementation.

**Verification Method(s)**  
Test

**Verification Statement**  
A unit test SHALL submit a set of requirement candidates including both conforming and non-conforming examples to the Requirements Agent, and assert that non-conforming candidates are flagged with a format violation and conforming candidates are accepted with populated attribute fields.

---

### AGT-0003 — Unique Requirement ID Assignment

| Field | Value |
|-------|-------|
| **ID** | AGT-0003 |
| **Short Name** | Unique Requirement ID Assignment |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | RMP-PLAN-001 §2.2 |
| **Trace: Parent** | AGT-0002 |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The Requirements Development Agent SHALL assign a unique identifier following the `[PREFIX]-[NNNN]` scheme defined in RMP-PLAN-001 §2.2 to every accepted requirement and SHALL never reuse an identifier, including for retired requirements.

**Rationale**  
Unique, stable identifiers enable unambiguous traceability across requirements, architecture elements, work items, and test cases. Reuse of IDs after retirement corrupts traceability history.

**Verification Method(s)**  
Test

**Verification Statement**  
A test SHALL create multiple requirements through the agent, retire one, then create a new one in the same domain, and assert that the new ID is distinct from all previously issued IDs including the retired one.

---

### AGT-0004 — Full Requirement Attribute Population

| Field | Value |
|-------|-------|
| **ID** | AGT-0004 |
| **Short Name** | Full Attribute Population |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | RMP-PLAN-001 §2.3 |
| **Trace: Parent** | AGT-0002 |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The Requirements Development Agent SHALL populate all mandatory requirement attributes — ID, Short Name, Requirement Text, Rationale, Verification Method(s), Verification Statement, Status, Priority, Source, and Trace fields — before marking a requirement APPROVED.

**Rationale**  
Incomplete requirement records cannot be verified, traced, or managed through change control. A requirement with missing rationale or verification statement cannot pass Gate 2.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
A unit test SHALL attempt to set a requirement to APPROVED status with one or more mandatory attributes absent and assert that the state transition is rejected. Inspection of the `Requirement` Pydantic model in `src/state/schema.py` SHALL confirm all mandatory fields are non-optional.

---

## Governance Requirements

### GOV-0001 — Automated Gate Evidence Validation

| Field | Value |
|-------|-------|
| **ID** | GOV-0001 |
| **Short Name** | Automated Gate Evidence Validation |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/governance/lifecycle-gate-checklists.md |
| **Trace: Parent** | ORIGIN |
| **Trace: Work Item** | Sprint 0 (complete) |
| **Trace: Test** | tests/unit/test_governance_validation.py |

**Requirement Text**  
The supervisor graph SHALL automatically invoke the governance evidence validator before permitting any phase transition where an agent has declared gate readiness status of READY.

**Rationale**  
Manual-only gate enforcement is unreliable and will not scale as the number of agents and gates grows. Automated validation ensures no READY transition bypasses the evidence completeness check.

**Verification Method(s)**  
Test

**Verification Statement**  
`tests/unit/test_supervisor_governance_hook.py` SHALL assert that the supervisor gate hook intercepts a READY transition with missing evidence and sets `requires_human_approval=True` and `gate_readiness_status=NOT_READY`.

---

### GOV-0002 — Requirements Traceability Matrix Generation

| Field | Value |
|-------|-------|
| **ID** | GOV-0002 |
| **Short Name** | RTM Generation |
| **Status** | DRAFT |
| **Priority** | P2-High |
| **Source** | RMP-001 §Traceability Rules |
| **Trace: Parent** | GOV-0001 |
| **Trace: Work Item** | Sprint 3 |
| **Trace: Test** | TBD — Sprint 3 |

**Requirement Text**  
The system SHALL generate a Requirements Traceability Matrix (RTM) that maps each requirement to its architecture elements, work items, and test cases, and SHALL include this RTM in the Gate 2 evidence package.

**Rationale**  
The RTM is the primary audit artifact demonstrating that all requirements are implemented and tested. Without it, gate reviewers cannot confirm end-to-end traceability.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
A test SHALL run a complete requirements-to-Gate-2 workflow and assert that the resulting evidence package contains an RTM field with entries for each APPROVED requirement. Inspection of the RTM SHALL confirm all three trace dimensions (architecture, work item, test) are present.

---

## HITL Requirements

### HITL-0001 — Complete Evidence Package Presentation

| Field | Value |
|-------|-------|
| **ID** | HITL-0001 |
| **Short Name** | Complete Evidence Package Presentation |
| **Status** | APPROVED |
| **Priority** | P1-Critical |
| **Source** | docs/plans/hitl-governance-plan.md, HITL-001 |
| **Trace: Parent** | SYS-0003 |
| **Trace: Work Item** | Sprint 2 |
| **Trace: Test** | TBD — Sprint 2 |

**Requirement Text**  
The HITL gateway SHALL present the human reviewer with the full governance evidence package — including policy compliance declarations, traceability links, gate readiness status, evidence links, and unresolved risks — before requesting an approve or reject decision.

**Rationale**  
A human reviewer who lacks the full evidence context may inadvertently approve incomplete or non-compliant work. The complete package ensures informed, accountable decisions.

**Verification Method(s)**  
Demonstration, Test

**Verification Statement**  
A demonstration SHALL show a HITL pause displaying all five evidence package fields in the terminal output. A test SHALL assert that the `hitl.py` approval request function raises an error or warning if any of the five mandatory fields are absent from the package passed to it.

---

## Infrastructure Requirements

### INFRA-0001 — CI/CD Pipeline with Coverage Gate

| Field | Value |
|-------|-------|
| **ID** | INFRA-0001 |
| **Short Name** | CI/CD Pipeline with Coverage Gate |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | docs/plans/software-development-plan.md |
| **Trace: Parent** | ORIGIN |
| **Trace: Work Item** | Sprint 1 |
| **Trace: Test** | .github/workflows/ci.yml |

**Requirement Text**  
The project SHALL maintain a GitHub Actions CI/CD pipeline that runs linting, unit tests, and coverage checks on every pull request and blocks merges when unit test coverage falls below 80%.

**Rationale**  
Without automated CI enforcement, code quality and test coverage degrade incrementally. A coverage gate ensures the governance principle of verified implementation is upheld throughout development.

**Verification Method(s)**  
Inspection, Test

**Verification Statement**  
Inspection of `.github/workflows/ci.yml` SHALL confirm lint, test, and coverage steps are defined. A test PR with a deliberately uncovered module SHALL be observed to fail the coverage check and block merge.

---

### INFRA-0002 — Mock LLM Mode for Testing

| Field | Value |
|-------|-------|
| **ID** | INFRA-0002 |
| **Short Name** | Mock LLM Mode for Testing |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | Risk Register — Ollama speed in CI |
| **Trace: Parent** | ORIGIN |
| **Trace: Work Item** | Sprint 1 |
| **Trace: Test** | tests/conftest.py |

**Requirement Text**  
The test infrastructure SHALL provide a mock LLM stub that replaces Ollama for all unit and integration tests so that tests run without a live Ollama instance and complete in under 60 seconds.

**Rationale**  
Requiring a live Ollama instance for every test run makes CI impractical (slow, hardware-dependent) and prevents developers from running tests offline. A deterministic stub enables fast, reliable test execution.

**Verification Method(s)**  
Test

**Verification Statement**  
The full unit test suite SHALL be executed with `OLLAMA_BASE_URL` unset or pointing to an invalid address, and all tests SHALL pass. Total test execution time SHALL be measured and confirmed below 60 seconds.

---

## Skills Requirements Addendum (Draft)

This addendum captures requirements for the skills layer that overlays agent roles. Architecture-impact requirements are listed first, followed by individual skill requirements.

### Architecture-Impact Requirements

### SYS-0010 — Skills Layer Overlay Architecture

| Field | Value |
|-------|-------|
| **ID** | SYS-0010 |
| **Short Name** | Skills Layer Overlay Architecture |
| **Level** | L1-System |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | docs/project-plan/PROJECT_PLAN.md §8-11 |
| **Trace: Parent** | SH-0001, SH-0004 |
| **Trace: Children** | AGT-0100, AGT-0101, INT-0100, GOV-0101, DATA-0100, PERF-0100, TEST-0100 |
| **Trace: Work Item** | Sprint 4-6 |
| **Trace: Test** | tests/integration/test_skills_layer_end_to_end.py (planned) |

**Requirement Text**  
The system SHALL implement a reusable skills layer that composes engineering-discipline capabilities onto agents at runtime while preserving existing agent authority and gate governance behavior.

**Rationale**  
Derived from SH-0001 and SH-0004 to address capability depth without multiplying role agents and to ensure auditable evidence generation remains consistent.

**Verification Method(s)**  
Inspection, Test

**Verification Statement**  
Inspection SHALL confirm skills architecture artifacts and binding configuration exist. Integration test SHALL show required skills executing for a gate and producing auditable evidence without bypassing authority controls.

---

### AGT-0100 — Skill Contract Schema

| Field | Value |
|-------|-------|
| **ID** | AGT-0100 |
| **Short Name** | Skill Contract Schema |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | SYS-0010 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 4 |
| **Trace: Test** | tests/unit/test_skill_contract_schema.py (planned) |

**Requirement Text**  
The skills subsystem SHALL define a versioned skill contract containing skill metadata, input schema, output schema, policy checks, traceability links, confidence score, and escalation conditions.

**Rationale**  
Derived from SYS-0010 to enforce deterministic behavior and consistent evidence payloads across all skills.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
Unit tests SHALL validate required fields and schema rejection behavior for incomplete skill definitions. Inspection SHALL confirm contract documentation in code and docs.

---

### AGT-0101 — Skill Registry and Version Control

| Field | Value |
|-------|-------|
| **ID** | AGT-0101 |
| **Short Name** | Skill Registry and Version Control |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | SYS-0010 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 4 |
| **Trace: Test** | tests/unit/test_skill_registry.py (planned) |

**Requirement Text**  
The system SHALL maintain a runtime skill registry that supports unique skill identifiers, semantic versioning, activation status, and backward-compatible lookup by agent role and gate.

**Rationale**  
Derived from SYS-0010. Skills require explicit lifecycle control to avoid silent behavior drift.

**Verification Method(s)**  
Test

**Verification Statement**  
Unit tests SHALL verify registry add/get/deprecate operations, duplicate version rejection, and deterministic skill resolution for role and gate combinations.

---

### INT-0100 — Agent-Skill Binding and Execution Order

| Field | Value |
|-------|-------|
| **ID** | INT-0100 |
| **Short Name** | Agent-Skill Binding and Execution Order |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | SYS-0010, ARCH-0005 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 4-5 |
| **Trace: Test** | tests/integration/test_agent_skill_binding.py (planned) |

**Requirement Text**  
The supervisor workflow SHALL bind mandatory and optional skills to each agent invocation by phase and gate policy, and SHALL execute mandatory skills before gate readiness evaluation.

**Rationale**  
Derived from SYS-0010 to ensure required discipline logic is consistently applied before transition decisions.

**Verification Method(s)**  
Test, Analysis

**Verification Statement**  
Integration tests SHALL assert mandatory skills execute before readiness computation and that execution order is traceable in run artifacts.

---

### GOV-0101 — Mandatory Skill Evidence Gate Enforcement

| Field | Value |
|-------|-------|
| **ID** | GOV-0101 |
| **Short Name** | Mandatory Skill Evidence Gate Enforcement |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | SYS-0010, GOV-0001 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 5 |
| **Trace: Test** | tests/integration/test_gate_skill_evidence_blocking.py (planned) |

**Requirement Text**  
The gate validator SHALL fail CLOSED and set gate readiness to NOT_READY when any mandatory skill evidence artifact is missing, invalid, or below configured confidence threshold.

**Rationale**  
Derived from SYS-0010 and GOV-0001 to prevent silent phase advancement with incomplete discipline evidence.

**Verification Method(s)**  
Test

**Verification Statement**  
Integration tests SHALL intentionally omit mandatory skill outputs and assert gate transition is blocked with explicit blocker reasons in governance evidence.

---

### DATA-0100 — Skill Evidence Persistence and Traceability

| Field | Value |
|-------|-------|
| **ID** | DATA-0100 |
| **Short Name** | Skill Evidence Persistence and Traceability |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P2-High |
| **Source** | SYS-0010, SYS-0002, GOV-0002 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 5-6 |
| **Trace: Test** | tests/integration/test_skill_evidence_persistence.py (planned) |

**Requirement Text**  
The system SHALL persist skill outputs and their traceability links to requirements, risks, decisions, and tests in shared state and checkpoint storage for all gate-relevant runs.

**Rationale**  
Derived from SYS-0010 to support audit replay and independent verification.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
Integration tests SHALL resume from checkpoint and confirm skill evidence and links remain intact and queryable for gate package generation.

---

### PERF-0100 — Skills Execution Overhead Budget

| Field | Value |
|-------|-------|
| **ID** | PERF-0100 |
| **Short Name** | Skills Execution Overhead Budget |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P2-High |
| **Source** | SYS-0010, OBS-0400 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 6 |
| **Trace: Test** | tests/performance/test_skill_overhead.py (planned) |

**Requirement Text**  
The skills subsystem SHALL keep median end-to-end gate preparation overhead within an approved performance budget and SHALL emit per-skill execution telemetry for threshold monitoring.

**Rationale**  
Derived from SYS-0010. Additional capability must not make gate workflows operationally unusable.

**Verification Method(s)**  
Test, Analysis

**Verification Statement**  
Performance tests SHALL report median and P95 overhead and fail when configured thresholds are exceeded.

---

### TEST-0100 — Skills Integration Verification Suite

| Field | Value |
|-------|-------|
| **ID** | TEST-0100 |
| **Short Name** | Skills Integration Verification Suite |
| **Level** | L2-Subsystem |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | SYS-0010 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 5-6 |
| **Trace: Test** | tests/integration/test_skills_layer_end_to_end.py (planned) |

**Requirement Text**  
The project SHALL maintain automated unit and integration test suites that verify skill contracts, binding behavior, gate blocking logic, persistence, and telemetry coverage before release readiness declaration.

**Rationale**  
Derived from SYS-0010 to ensure skills behavior remains stable as new disciplines are added.

**Verification Method(s)**  
Test

**Verification Statement**  
CI SHALL execute skills test suites and fail when any required scenario is not covered or fails assertions.

---

### Individual Skill Requirements

### AGT-0110 — Requirements Quality Skill

| Field | Value |
|-------|-------|
| **ID** | AGT-0110 |
| **Short Name** | Requirements Quality Skill |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | SYS-0010, AGT-0002, AGT-0005 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 4 |
| **Trace: Test** | tests/unit/test_skill_requirements_quality.py (planned) |

**Requirement Text**  
The Requirements Quality Skill SHALL validate noun-SHALL-verb conformance, attribute completeness, and hierarchy integrity for all candidate requirements before Gate 2 readiness evaluation.

**Rationale**  
Derived from SYS-0010 to centralize requirements quality checks as reusable discipline logic.

**Verification Method(s)**  
Test

**Verification Statement**  
Unit and integration tests SHALL demonstrate that malformed or incomplete requirements trigger blockers and prevent READY declaration.

---

### AGT-0111 — Architecture Allocation Skill

| Field | Value |
|-------|-------|
| **ID** | AGT-0111 |
| **Short Name** | Architecture Allocation Skill |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | SYS-0010, ARCH-0004 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 5 |
| **Trace: Test** | tests/unit/test_skill_architecture_allocation.py (planned) |

**Requirement Text**  
The Architecture Allocation Skill SHALL produce a requirement-to-component allocation completeness report and identify unallocated requirements before Gate 3 readiness evaluation.

**Rationale**  
Derived from SYS-0010 to ensure architectural allocation evidence is consistent and reusable.

**Verification Method(s)**  
Test

**Verification Statement**  
Tests SHALL verify that at least one unallocated requirement triggers a NOT_READY blocker with explicit requirement identifiers.

---

### AGT-0112 — Threat and Hazard Skill

| Field | Value |
|-------|-------|
| **ID** | AGT-0112 |
| **Short Name** | Threat and Hazard Skill |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | SYS-0010, SEC-0100, SAF-0100, REL-0100 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 5 |
| **Trace: Test** | tests/unit/test_skill_threat_hazard.py (planned) |

**Requirement Text**  
The Threat and Hazard Skill SHALL generate threat, hazard, and reliability artifacts with linked mitigations and severity assessments before Gate 3 readiness evaluation.

**Rationale**  
Derived from SYS-0010 to consolidate safety and security artifact generation under one reusable skill.

**Verification Method(s)**  
Test

**Verification Statement**  
Tests SHALL verify required artifact fields and mitigation links are produced and included in governance evidence.

---

### AGT-0113 — Traceability Synthesis Skill

| Field | Value |
|-------|-------|
| **ID** | AGT-0113 |
| **Short Name** | Traceability Synthesis Skill |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P1-Critical |
| **Source** | SYS-0010, GOV-0002 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 4 |
| **Trace: Test** | tests/unit/test_skill_traceability_synthesis.py (planned) |

**Requirement Text**  
The Traceability Synthesis Skill SHALL generate forward and backward trace links across requirements, architecture elements, work items, and tests for gate evidence packaging.

**Rationale**  
Derived from SYS-0010 to make RTM and trace-rollup logic reusable across agents.

**Verification Method(s)**  
Test

**Verification Statement**  
Tests SHALL verify trace links are complete for configured scope and that missing links are reported as blockers.

---

### AGT-0114 — Test Design Skill

| Field | Value |
|-------|-------|
| **ID** | AGT-0114 |
| **Short Name** | Test Design Skill |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P2-High |
| **Source** | SYS-0010, VNV-0300 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 5 |
| **Trace: Test** | tests/unit/test_skill_test_design.py (planned) |

**Requirement Text**  
The Test Design Skill SHALL generate requirement-linked test case proposals and verification-method coverage summaries before Gate 5 readiness evaluation.

**Rationale**  
Derived from SYS-0010 to standardize verification artifact quality.

**Verification Method(s)**  
Test

**Verification Statement**  
Tests SHALL confirm each active requirement receives at least one mapped test case or an explicit exemption rationale.

---

### AGT-0115 — Configuration Baseline Skill

| Field | Value |
|-------|-------|
| **ID** | AGT-0115 |
| **Short Name** | Configuration Baseline Skill |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P2-High |
| **Source** | SYS-0010, CM-0200 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 5 |
| **Trace: Test** | tests/unit/test_skill_configuration_baseline.py (planned) |

**Requirement Text**  
The Configuration Baseline Skill SHALL generate baseline delta reports and change-control evidence for implementation and release gates.

**Rationale**  
Derived from SYS-0010 to standardize CM evidence across release cycles.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
Tests SHALL verify baseline and change-log artifacts are produced with version identifiers and impacted component references.

---

### AGT-0116 — Release Readiness Skill

| Field | Value |
|-------|-------|
| **ID** | AGT-0116 |
| **Short Name** | Release Readiness Skill |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P2-High |
| **Source** | SYS-0010, IRP-001 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 6 |
| **Trace: Test** | tests/integration/test_skill_release_readiness.py (planned) |

**Requirement Text**  
The Release Readiness Skill SHALL compile release checklist status, unresolved defect waivers, and approval records into a gate-ready release evidence package.

**Rationale**  
Derived from SYS-0010 to provide consistent, auditable release decisions.

**Verification Method(s)**  
Test

**Verification Statement**  
Integration tests SHALL verify that missing mandatory release evidence blocks readiness and lists unresolved checklist items.

---

### AGT-0117 — Data Governance Skill

| Field | Value |
|-------|-------|
| **ID** | AGT-0117 |
| **Short Name** | Data Governance Skill |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P3-Medium |
| **Source** | SYS-0010, DATA plan corpus |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 8 |
| **Trace: Test** | tests/unit/test_skill_data_governance.py (planned) |

**Requirement Text**  
The Data Governance Skill SHALL generate data inventory, data quality controls, and policy-control linkage evidence for gate packages where data constraints apply.

**Rationale**  
Derived from SYS-0010 to ensure data controls are explicit and auditable.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
Tests SHALL verify generation of required inventory and control-link fields with references to governed datasets or interfaces.

---

### AGT-0118 — Operational Reliability Skill

| Field | Value |
|-------|-------|
| **ID** | AGT-0118 |
| **Short Name** | Operational Reliability Skill |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P3-Medium |
| **Source** | SYS-0010, operations guidance |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 8 |
| **Trace: Test** | tests/integration/test_skill_operational_reliability.py (planned) |

**Requirement Text**  
The Operational Reliability Skill SHALL evaluate SLO readiness, rollback capability, and deployment risk indicators before deployment gate declaration.

**Rationale**  
Derived from SYS-0010 to support dependable deployment and operations decisions.

**Verification Method(s)**  
Test

**Verification Statement**  
Integration tests SHALL verify deployment readiness is blocked when rollback procedures or reliability thresholds are not satisfied.

---

### AGT-0119 — Compliance Packaging Skill

| Field | Value |
|-------|-------|
| **ID** | AGT-0119 |
| **Short Name** | Compliance Packaging Skill |
| **Level** | L3-Implementation |
| **Status** | DRAFT |
| **Priority** | P3-Medium |
| **Source** | SYS-0010, AC8-0610 |
| **Trace: Parent** | SYS-0010 |
| **Trace: Children** | NONE |
| **Trace: Work Item** | Sprint 8 |
| **Trace: Test** | tests/integration/test_skill_compliance_packaging.py (planned) |

**Requirement Text**  
The Compliance Packaging Skill SHALL assemble waivers, risk acceptances, policy checks, and approver signatures into an auditable compliance bundle for release and deployment reviews.

**Rationale**  
Derived from SYS-0010 to make compliance evidence assembly repeatable and reviewable.

**Verification Method(s)**  
Test, Inspection

**Verification Statement**  
Tests SHALL verify required compliance bundle fields and signatures are present and that missing approvals produce explicit blockers.
