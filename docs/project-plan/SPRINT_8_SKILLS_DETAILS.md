# Sprint 8 Skills — Execution-Ready Stories

<!-- markdownlint-disable MD032 MD060 -->

Sprint Window: August 16 - August 29, 2026 (2 weeks)  
Sprint Goal: Deliver advanced skills for data governance, operational reliability, and compliance packaging to complete forward skill set coverage.  
Scope Source: docs/project-plan/SKILLS_BACKLOG_DECOMPOSITION.md (Sprint 8 section)  
Async Standup Board: docs/project-plan/SPRINT_8_SKILLS_ASYNC_STANDUP_BOARD.md  
Default Workflow: docs/project-plan/ASYNC_STANDUP_WORKFLOW.md

---

## Sprint 8 Story Set

| Story ID | Type | Requirement Link(s) | Estimate (hours) | Owner | Priority |
|----------|------|---------------------|------------------|-------|----------|
| SKILL-8001 | IMPL | AGT-0117 | 10 | Developer | P2 |
| SKILL-8002 | IMPL | AGT-0118 | 10 | Developer | P2 |
| SKILL-8003 | IMPL | AGT-0119 | 10 | Developer | P2 |

Total Estimated Effort: 30 hours  
Planning Capacity Assumption: 60 hours  
Buffer: 30 hours

---

## Dependency Order

1. SKILL-8001 -> data inventory/control artifacts used by compliance packaging.
2. SKILL-8002 -> reliability readiness artifacts used by compliance packaging.
3. SKILL-8003 -> depends on SKILL-8001 and SKILL-8002 outputs.

---

## Story Details

### Story SKILL-8001 - Data Governance Skill

Type: IMPL  
Requirement(s): AGT-0117  
Estimate: 10h  
Dependencies: Existing skill contract and traceability structures  
Status: Not Started

Scope:
- Generate data inventory and data-control linkage artifacts for gate evidence.

Out of Scope:
- End-to-end data lineage automation beyond inventory/control links.

Implementation Tasks:
- Implement src/skills/data_governance.py.
- Emit inventory objects, control mappings, and policy references.
- Add tests/unit/test_skill_data_governance.py.

Acceptance Criteria:
- Skill output includes inventory and control mappings.
- Missing mandatory data controls generate explicit blockers.
- Unit tests cover schema-valid output and missing-control paths.

Verification Artifacts:
- tests/unit/test_skill_data_governance.py
- src/skills/data_governance.py

Done Criteria:
- Merged with green CI.
- Requirement trace for AGT-0117 updated to SKILL-8001.

---

### Story SKILL-8002 - Operational Reliability Skill

Type: IMPL  
Requirement(s): AGT-0118  
Estimate: 10h  
Dependencies: Existing deployment and metrics structures  
Status: Not Started

Scope:
- Evaluate SLO readiness, rollback readiness, and deployment risk indicators.

Out of Scope:
- Autonomous remediation orchestration.

Implementation Tasks:
- Implement src/skills/operational_reliability.py.
- Emit readiness indicators and blocker reasons.
- Add tests/integration/test_skill_operational_reliability.py.

Acceptance Criteria:
- Output includes SLO and rollback readiness fields.
- Gate blocking occurs when reliability criteria are not met.
- Integration tests validate pass/fail behavior.

Verification Artifacts:
- tests/integration/test_skill_operational_reliability.py
- src/skills/operational_reliability.py

Done Criteria:
- Merged with green CI.
- Requirement trace for AGT-0118 updated to SKILL-8002.

---

### Story SKILL-8003 - Compliance Packaging Skill

Type: IMPL  
Requirement(s): AGT-0119  
Estimate: 10h  
Dependencies: SKILL-8001 and SKILL-8002  
Status: Not Started

Scope:
- Assemble waivers, risk acceptances, approvals, and policy checks into auditable compliance bundles.

Out of Scope:
- External export pipeline to non-local compliance systems.

Implementation Tasks:
- Implement src/skills/compliance_packaging.py.
- Build compliance bundle schema and signature checks.
- Add tests/integration/test_skill_compliance_packaging.py.

Acceptance Criteria:
- Compliance bundle includes required waiver and approval fields.
- Missing approvals or required signatures produce explicit blockers.
- Integration tests validate pass/fail conditions.

Verification Artifacts:
- tests/integration/test_skill_compliance_packaging.py
- src/skills/compliance_packaging.py

Done Criteria:
- Merged with green CI.
- Requirement trace for AGT-0119 updated to SKILL-8003.

---

## Day-by-Day Sprint Execution Plan

### Week 1

#### Day 1 (Aug 16)

- Sprint kickoff and dependency confirmation.
- Start SKILL-8001 data inventory schema.

#### Day 2 (Aug 17)

- Continue SKILL-8001 and add unit tests.

#### Day 3 (Aug 18)

- Complete SKILL-8001.
- Start SKILL-8002 reliability skill scaffolding.

#### Day 4 (Aug 19)

- Continue SKILL-8002 integration checks.

#### Day 5 (Aug 20)

- Complete SKILL-8002 fail/pass integration assertions.

### Week 2

#### Day 6 (Aug 23)

- Start SKILL-8003 compliance packaging module.

#### Day 7 (Aug 24)

- Continue SKILL-8003 schema and validation rules.

#### Day 8 (Aug 25)

- Complete SKILL-8003 and integration tests.

#### Day 9 (Aug 26)

- Regression run and defect fixes.

#### Day 10 (Aug 27)

- Update requirement trace fields and evidence links.

#### Day 11 (Aug 28)

- Sprint close-out and governance evidence review.

#### Day 12 (Aug 29)

- Final phase review and retrospective notes.

---

## Sprint 8 Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Compliance bundle schema drift across stories | Medium | High | Freeze schema contract at start of Week 2 |
| Reliability criteria ambiguity | Medium | Medium | Document explicit thresholds in story notes before Day 4 |
| Data control mapping incompleteness | Medium | Medium | Add mandatory control checklist in SKILL-8001 tests |

---

## Sprint 8 Definition of Done

1. SKILL-8001, SKILL-8002, and SKILL-8003 are merged.
2. Integration tests validate advanced-skill fail/pass gate scenarios.
3. Requirement Trace: Work Item fields updated for AGT-0117 through AGT-0119.
4. Async standup board finalized with evidence and blocker status.
