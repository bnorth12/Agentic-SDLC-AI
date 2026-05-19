# Skills Backlog Decomposition

**Document ID**: SKILL-BKL-001  
**Date**: 2026-05-18  
**Status**: Draft — Pending Gate 2 requirement baseline update

---

## Purpose

Decompose the skills-layer requirements into sprint-executable backlog items with explicit acceptance criteria and traceability.

Primary requirement source: `docs/requirements/PRODUCT_REQUIREMENTS.md` (Skills Requirements Addendum).

Default execution workflow source: `docs/project-plan/ASYNC_STANDUP_WORKFLOW.md`.

---

## Backlog Rules

1. Every implementation item SHALL reference one or more approved L2/L3 requirement IDs.
2. Every item SHALL include at least one verification target (unit/integration/performance test).
3. Gate-relevant skill items SHALL include fail-closed checks when evidence is missing.
4. Skills are additive to agent roles and SHALL not alter existing authority ownership.

---

## Sprint 4 — Skills Foundation and First P0 Skills

Execution-ready stories, estimates, dependency order, and day-by-day plan are defined in `docs/project-plan/SPRINT_4_SKILLS_DETAILS.md`.

Sprint async standup board is tracked in `docs/project-plan/SPRINT_4_SKILLS_ASYNC_STANDUP_BOARD.md`.

### [IMPL] SKILL-4001 Skill Contract Schema and Model

**Trace to Requirements**: AGT-0100  
**Acceptance Criteria**:
- [ ] Add skill contract model in `src/skills/contracts.py` with required fields (metadata, input/output schema, policy checks, trace links, confidence, escalation)
- [ ] Add schema validation utilities for required/optional fields
- [ ] Add semantic version field and parser
- [ ] Add unit tests in `tests/unit/test_skill_contract_schema.py`

### [IMPL] SKILL-4002 Skill Registry and Resolution Engine

**Trace to Requirements**: AGT-0101  
**Acceptance Criteria**:
- [ ] Add registry implementation in `src/skills/registry.py`
- [ ] Support register/get/list/deprecate operations
- [ ] Resolve skill by `(agent_role, gate, discipline)` lookup
- [ ] Reject duplicate `(skill_id, version)` registration
- [ ] Add unit tests in `tests/unit/test_skill_registry.py`

### [IMPL] SKILL-4003 Agent-Skill Binding Hook in Supervisor

**Trace to Requirements**: INT-0100  
**Acceptance Criteria**:
- [ ] Add binding policy config in `src/config/skills.py`
- [ ] Integrate binding hook in supervisor flow before gate readiness assembly
- [ ] Execute mandatory skills first, optional skills second
- [ ] Record execution order in state evidence log
- [ ] Add integration test in `tests/integration/test_agent_skill_binding.py`

### [IMPL] SKILL-4004 Requirements Quality Skill

**Trace to Requirements**: AGT-0110  
**Acceptance Criteria**:
- [ ] Implement skill module in `src/skills/requirements_quality.py`
- [ ] Validate noun-SHALL-verb format, attributes, and hierarchy checks
- [ ] Emit structured violations with requirement IDs
- [ ] Add unit tests in `tests/unit/test_skill_requirements_quality.py`

### [IMPL] SKILL-4005 Traceability Synthesis Skill

**Trace to Requirements**: AGT-0113  
**Acceptance Criteria**:
- [ ] Implement skill module in `src/skills/traceability_synthesis.py`
- [ ] Generate forward/backward links across req-arch-work-test
- [ ] Emit missing-link blocker list for gate evidence
- [ ] Add unit tests in `tests/unit/test_skill_traceability_synthesis.py`

### [TEST] SKILL-4090 Sprint 4 Skills Smoke Suite

**Trace to Requirements**: TEST-0100  
**Acceptance Criteria**:
- [ ] Add smoke suite in `tests/integration/test_skills_smoke.py`
- [ ] Validate registry resolution + mandatory execution + evidence merge
- [ ] Verify no authority field mutation from skills execution

---

## Sprint 5 — Gate Enforcement and P0 Completion

Execution-ready stories, estimates, dependency order, and day-by-day plan are defined in `docs/project-plan/SPRINT_5_SKILLS_DETAILS.md`.

Sprint async standup board is tracked in `docs/project-plan/SPRINT_5_SKILLS_ASYNC_STANDUP_BOARD.md`.

### [IMPL] SKILL-5001 Mandatory Skill Evidence Fail-Closed Validator

**Trace to Requirements**: GOV-0101  
**Acceptance Criteria**:
- [ ] Extend gate validator to enforce mandatory skill artifacts
- [ ] Block READY transition if mandatory skill output missing/invalid
- [ ] Include blocker reason and failed skill IDs in governance output
- [ ] Add integration test in `tests/integration/test_gate_skill_evidence_blocking.py`

### [IMPL] SKILL-5002 Architecture Allocation Skill

**Trace to Requirements**: AGT-0111  
**Acceptance Criteria**:
- [ ] Implement `src/skills/architecture_allocation.py`
- [ ] Generate allocation completeness report
- [ ] Identify unallocated requirement IDs
- [ ] Add tests in `tests/unit/test_skill_architecture_allocation.py`

### [IMPL] SKILL-5003 Threat and Hazard Skill

**Trace to Requirements**: AGT-0112  
**Acceptance Criteria**:
- [ ] Implement `src/skills/threat_hazard.py`
- [ ] Emit threat, hazard, reliability artifacts with mitigation links
- [ ] Add tests in `tests/unit/test_skill_threat_hazard.py`

### [IMPL] SKILL-5004 Test Design Skill

**Trace to Requirements**: AGT-0114  
**Acceptance Criteria**:
- [ ] Implement `src/skills/test_design.py`
- [ ] Generate requirement-linked test proposals with coverage map
- [ ] Add tests in `tests/unit/test_skill_test_design.py`

### [IMPL] SKILL-5005 Configuration Baseline Skill

**Trace to Requirements**: AGT-0115  
**Acceptance Criteria**:
- [ ] Implement `src/skills/configuration_baseline.py`
- [ ] Emit baseline delta and change-control artifacts
- [ ] Add tests in `tests/unit/test_skill_configuration_baseline.py`

### [TEST] SKILL-5090 Gate 2-5 Skills Integration Suite

**Trace to Requirements**: TEST-0100, GOV-0101  
**Acceptance Criteria**:
- [ ] Add `tests/integration/test_skills_layer_end_to_end.py`
- [ ] Validate gate blocking for missing skills
- [ ] Validate gate pass when mandatory evidence complete

---

## Sprint 6 — Persistence and Telemetry Hardening

Execution-ready stories, estimates, dependency order, and day-by-day plan are defined in `docs/project-plan/SPRINT_6_SKILLS_DETAILS.md`.

Sprint async standup board is tracked in `docs/project-plan/SPRINT_6_SKILLS_ASYNC_STANDUP_BOARD.md`.

### [IMPL] SKILL-6001 Skill Evidence Persistence Integration

**Trace to Requirements**: DATA-0100  
**Acceptance Criteria**:
- [ ] Extend state schema for skill evidence payloads and trace links
- [ ] Persist skill evidence through checkpoint resume
- [ ] Add tests in `tests/integration/test_skill_evidence_persistence.py`

### [IMPL] SKILL-6002 Skills Performance and Telemetry Instrumentation

**Trace to Requirements**: PERF-0100  
**Acceptance Criteria**:
- [ ] Capture per-skill latency, confidence, escalation, and failure counters
- [ ] Surface telemetry in KPI report path
- [ ] Add performance tests in `tests/performance/test_skill_overhead.py`

### [IMPL] SKILL-6003 Release Readiness Skill

**Trace to Requirements**: AGT-0116  
**Acceptance Criteria**:
- [ ] Implement `src/skills/release_readiness.py`
- [ ] Compile release checklist, waivers, and approvals into package
- [ ] Add integration tests in `tests/integration/test_skill_release_readiness.py`

---

## Sprint 8 — Advanced Skills

Execution-ready stories, estimates, dependency order, and day-by-day plan are defined in `docs/project-plan/SPRINT_8_SKILLS_DETAILS.md`.

Sprint async standup board is tracked in `docs/project-plan/SPRINT_8_SKILLS_ASYNC_STANDUP_BOARD.md`.

### [IMPL] SKILL-8001 Data Governance Skill

**Trace to Requirements**: AGT-0117  
**Acceptance Criteria**:
- [ ] Implement `src/skills/data_governance.py`
- [ ] Emit inventory and data-control linkage artifacts
- [ ] Add tests in `tests/unit/test_skill_data_governance.py`

### [IMPL] SKILL-8002 Operational Reliability Skill

**Trace to Requirements**: AGT-0118  
**Acceptance Criteria**:
- [ ] Implement `src/skills/operational_reliability.py`
- [ ] Evaluate SLO readiness, rollback readiness, deployment risk
- [ ] Add integration tests in `tests/integration/test_skill_operational_reliability.py`

### [IMPL] SKILL-8003 Compliance Packaging Skill

**Trace to Requirements**: AGT-0119  
**Acceptance Criteria**:
- [ ] Implement `src/skills/compliance_packaging.py`
- [ ] Assemble waivers, risk acceptances, signatures into bundle
- [ ] Add integration tests in `tests/integration/test_skill_compliance_packaging.py`

---

## Cross-Sprint Governance and Documentation

### [GOV] SKILL-9001 Gate Checklist Updates

**Trace to Requirements**: GOV-0101, TEST-0100  
**Acceptance Criteria**:
- [ ] Update gate checklists to include mandatory skills per gate
- [ ] Document fail-closed behavior and HITL evidence expectations

### [DOC] SKILL-9002 Skills Authoring and Integration Guide

**Trace to Requirements**: AGT-0100, AGT-0101, INT-0100  
**Acceptance Criteria**:
- [ ] Add `docs/development-guide.md` section for skill authoring contract
- [ ] Add examples for registering and binding a new skill
- [ ] Add troubleshooting guidance for missing-evidence blockers

---

## Readiness to Move into Active Sprint Board

The backlog can be promoted to active sprint planning when:
- [ ] SYS-0010 and all referenced L2/L3 skills requirements are approved at Gate 2 baseline update
- [ ] Requirement-to-work-item trace links are copied into `Trace: Work Item` fields
- [ ] At least one verification artifact path exists for every item in this file
