# Sprint 5 Skills — Execution-Ready Stories

<!-- markdownlint-disable MD032 MD060 -->

Sprint Window: July 5 - July 18, 2026 (2 weeks)  
Sprint Goal: Complete P0 skills and add Gate fail-closed enforcement with integration validation through Gate 5.  
Scope Source: docs/project-plan/SKILLS_BACKLOG_DECOMPOSITION.md (Sprint 5 section)  
Async Standup Board: docs/project-plan/SPRINT_5_SKILLS_ASYNC_STANDUP_BOARD.md  
Default Workflow: docs/project-plan/ASYNC_STANDUP_WORKFLOW.md

---

## Sprint 5 Story Set

| Story ID | Type | Requirement Link(s) | Estimate (hours) | Owner | Priority |
|----------|------|---------------------|------------------|-------|----------|
| SKILL-5001 | IMPL | GOV-0101 | 12 | Developer | P1 |
| SKILL-5002 | IMPL | AGT-0111 | 8 | Developer | P1 |
| SKILL-5003 | IMPL | AGT-0112 | 8 | Developer | P1 |
| SKILL-5004 | IMPL | AGT-0114 | 8 | Developer | P2 |
| SKILL-5005 | IMPL | AGT-0115 | 8 | Developer | P2 |
| SKILL-5090 | TEST | TEST-0100, GOV-0101 | 10 | Developer | P1 |

Total Estimated Effort: 54 hours  
Planning Capacity Assumption: 60 hours  
Buffer: 6 hours

---

## Dependency Order

1. SKILL-5001 -> establishes mandatory evidence fail-closed enforcement.
2. SKILL-5002 and SKILL-5003 -> can execute in parallel after SKILL-5001 interface contract is stable.
3. SKILL-5004 and SKILL-5005 -> depend on stable registry and binding behavior from prior sprint; run parallel with mid-sprint merge cadence.
4. SKILL-5090 -> depends on SKILL-5001 through SKILL-5005 completion.

---

## Story Details

### Story SKILL-5001 - Mandatory Skill Evidence Fail-Closed Validator

Type: IMPL  
Requirement(s): GOV-0101  
Estimate: 12h  
Dependencies: Sprint 4 binding and skill evidence payload structure  
Status: Not Started

Scope:
- Enforce fail-closed gate behavior when mandatory skill artifacts are missing or invalid.

Out of Scope:
- Confidence threshold tuning policy beyond baseline enforcement.

Implementation Tasks:
- Extend governance validator to include mandatory skill checks.
- Add explicit blocker reason payload with failed skill IDs.
- Ensure READY transition downgrade behavior is deterministic.
- Add tests/integration/test_gate_skill_evidence_blocking.py.

Acceptance Criteria:
- Missing mandatory skill output blocks READY transition.
- Blocker reason includes failed skill IDs and validation rationale.
- Integration test covers pass and fail scenarios.

Verification Artifacts:
- tests/integration/test_gate_skill_evidence_blocking.py
- src/gates and supervisor validator integration updates

Done Criteria:
- Merged with green CI and no gate regression in existing suites.
- Requirement trace for GOV-0101 updated to SKILL-5001.

---

### Story SKILL-5002 - Architecture Allocation Skill

Type: IMPL  
Requirement(s): AGT-0111  
Estimate: 8h  
Dependencies: Sprint 4 skill contract and registry  
Status: Not Started

Scope:
- Produce requirement-to-component allocation completeness output and unallocated IDs.

Out of Scope:
- Full architecture optimization heuristics.

Implementation Tasks:
- Implement src/skills/architecture_allocation.py.
- Emit completeness ratio and missing-allocation list.
- Add tests/unit/test_skill_architecture_allocation.py.

Acceptance Criteria:
- Skill output includes completeness metrics.
- Unallocated requirements are listed with IDs.
- Unit tests pass with deterministic fixtures.

Verification Artifacts:
- tests/unit/test_skill_architecture_allocation.py
- src/skills/architecture_allocation.py

Done Criteria:
- Merged with green CI.
- Requirement trace for AGT-0111 updated to SKILL-5002.

---

### Story SKILL-5003 - Threat and Hazard Skill

Type: IMPL  
Requirement(s): AGT-0112  
Estimate: 8h  
Dependencies: Sprint 4 skill contract and binding path  
Status: Not Started

Scope:
- Emit threat, hazard, and reliability risk artifacts with mitigation linkage.

Out of Scope:
- Automated mitigation recommendation ranking.

Implementation Tasks:
- Implement src/skills/threat_hazard.py.
- Build output schema for threat/hazard/reliability artifacts.
- Add tests/unit/test_skill_threat_hazard.py.

Acceptance Criteria:
- Output includes severity, scenario IDs, and mitigation links.
- Unit tests cover normal and incomplete input cases.

Verification Artifacts:
- tests/unit/test_skill_threat_hazard.py
- src/skills/threat_hazard.py

Done Criteria:
- Merged with green CI.
- Requirement trace for AGT-0112 updated to SKILL-5003.

---

### Story SKILL-5004 - Test Design Skill

Type: IMPL  
Requirement(s): AGT-0114  
Estimate: 8h  
Dependencies: Skill registry resolution and traceability skill interfaces  
Status: Not Started

Scope:
- Generate requirement-linked test case proposals and verification method mapping.

Out of Scope:
- Full execution of generated test cases.

Implementation Tasks:
- Implement src/skills/test_design.py.
- Emit mapped test proposals and coverage summary.
- Add tests/unit/test_skill_test_design.py.

Acceptance Criteria:
- Each active requirement maps to test proposal or explicit exemption rationale.
- Output structure is schema-valid and deterministic in tests.

Verification Artifacts:
- tests/unit/test_skill_test_design.py
- src/skills/test_design.py

Done Criteria:
- Merged with green CI.
- Requirement trace for AGT-0114 updated to SKILL-5004.

---

### Story SKILL-5005 - Configuration Baseline Skill

Type: IMPL  
Requirement(s): AGT-0115  
Estimate: 8h  
Dependencies: Traceability evidence formats from Sprint 4  
Status: Not Started

Scope:
- Emit baseline delta and change-control artifacts for gate packaging.

Out of Scope:
- Full release manifest generation.

Implementation Tasks:
- Implement src/skills/configuration_baseline.py.
- Emit version tags, component impact list, and change summary.
- Add tests/unit/test_skill_configuration_baseline.py.

Acceptance Criteria:
- Baseline artifact includes version and impacted components.
- Unit tests validate schema and required fields.

Verification Artifacts:
- tests/unit/test_skill_configuration_baseline.py
- src/skills/configuration_baseline.py

Done Criteria:
- Merged with green CI.
- Requirement trace for AGT-0115 updated to SKILL-5005.

---

### Story SKILL-5090 - Gate 2-5 Skills Integration Suite

Type: TEST  
Requirement(s): TEST-0100, GOV-0101  
Estimate: 10h  
Dependencies: SKILL-5001 through SKILL-5005  
Status: Not Started

Scope:
- Validate end-to-end behavior for gates requiring mandatory skills.

Out of Scope:
- Performance threshold analysis (Sprint 6).

Implementation Tasks:
- Add tests/integration/test_skills_layer_end_to_end.py.
- Validate blocked transition on missing mandatory evidence.
- Validate pass transition with complete evidence bundle.

Acceptance Criteria:
- Integration suite passes and asserts both fail and pass paths.
- Evidence payload includes expected skill outputs and blocker metadata.

Verification Artifacts:
- tests/integration/test_skills_layer_end_to_end.py

Done Criteria:
- Merged with green CI.
- Requirement trace for TEST-0100 and GOV-0101 updated to SKILL-5090.

---

## Day-by-Day Sprint Execution Plan

### Week 1

#### Day 1 (Jul 5)

- Sprint kickoff and dependency confirmation.
- Start SKILL-5001 validator extension skeleton.

#### Day 2 (Jul 6)

- Continue SKILL-5001 and add first fail-path tests.
- Start SKILL-5002 scaffolding.

#### Day 3 (Jul 7)

- Complete SKILL-5001 core behavior.
- Continue SKILL-5002 and start SKILL-5003.

#### Day 4 (Jul 8)

- Complete SKILL-5002 tests and merge readiness.
- Continue SKILL-5003 artifact schema and tests.

#### Day 5 (Jul 9)

- Complete SKILL-5003.
- Start SKILL-5004 and SKILL-5005 scaffolding.

### Week 2

#### Day 6 (Jul 12)

- Continue SKILL-5004 implementation and tests.
- Continue SKILL-5005 implementation.

#### Day 7 (Jul 13)

- Complete SKILL-5004.
- Complete SKILL-5005 and unit tests.

#### Day 8 (Jul 14)

- Start SKILL-5090 integration suite with fail-path assertions.

#### Day 9 (Jul 15)

- Complete SKILL-5090 pass-path coverage and stabilize fixtures.

#### Day 10 (Jul 16)

- Buffer for defects and integration regressions.
- Update trace fields for Sprint 5 requirement IDs.

#### Day 11 (Jul 17)

- Sprint close-out checks and evidence review.

#### Day 12 (Jul 18)

- Gate readiness review and retrospective notes.

---

## Sprint 5 Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Fail-closed logic causes unexpected gate regressions | Medium | High | Add regression assertions early on Day 2 |
| Integration suite fixture instability | Medium | Medium | Reuse deterministic fixtures and explicit setup builders |
| Parallel skill implementation merge conflicts | Medium | Medium | Merge SKILL-5002 and SKILL-5003 separately before Day 5 |

---

## Sprint 5 Definition of Done

1. SKILL-5001 through SKILL-5005 and SKILL-5090 are merged.
2. Integration suite validates fail and pass gate behavior.
3. Requirement Trace: Work Item updates are complete for linked IDs.
4. Async standup board reflects final status and evidence links.
