# Sprint 6 Skills — Execution-Ready Stories

<!-- markdownlint-disable MD032 MD060 -->

Sprint Window: July 19 - August 1, 2026 (2 weeks)  
Sprint Goal: Harden skill persistence and observability, and deliver release readiness skill with verification evidence continuity.  
Scope Source: docs/project-plan/SKILLS_BACKLOG_DECOMPOSITION.md (Sprint 6 section)  
Async Standup Board: docs/project-plan/SPRINT_6_SKILLS_ASYNC_STANDUP_BOARD.md  
Default Workflow: docs/project-plan/ASYNC_STANDUP_WORKFLOW.md

---

## Sprint 6 Story Set

| Story ID | Type | Requirement Link(s) | Estimate (hours) | Owner | Priority |
|----------|------|---------------------|------------------|-------|----------|
| SKILL-6001 | IMPL | DATA-0100 | 12 | Developer | P1 |
| SKILL-6002 | IMPL | PERF-0100 | 12 | Developer | P1 |
| SKILL-6003 | IMPL | AGT-0116 | 10 | Developer | P2 |

Total Estimated Effort: 34 hours  
Planning Capacity Assumption: 60 hours  
Buffer: 26 hours

---

## Dependency Order

1. SKILL-6001 -> state schema and checkpoint persistence path.
2. SKILL-6002 -> depends on stable persistence fields from SKILL-6001 for telemetry continuity.
3. SKILL-6003 -> can run in parallel after SKILL-6001 schema stabilizes.

---

## Story Details

### Story SKILL-6001 - Skill Evidence Persistence Integration

Type: IMPL  
Requirement(s): DATA-0100  
Estimate: 12h  
Dependencies: Sprint 5 evidence payload format stability  
Status: Not Started

Scope:
- Persist skill evidence payloads and trace links through checkpoint lifecycle.

Out of Scope:
- Long-term archival pipeline externalization.

Implementation Tasks:
- Extend state schema with skill evidence structures.
- Ensure checkpoint resume restores skill evidence and links.
- Add tests/integration/test_skill_evidence_persistence.py.

Acceptance Criteria:
- Checkpoint restore includes skill outputs and trace links.
- Integration tests validate resume behavior and evidence integrity.

Verification Artifacts:
- tests/integration/test_skill_evidence_persistence.py
- src/state schema and persistence updates

Done Criteria:
- Merged with green CI.
- Requirement trace for DATA-0100 updated to SKILL-6001.

---

### Story SKILL-6002 - Skills Performance and Telemetry Instrumentation

Type: IMPL  
Requirement(s): PERF-0100  
Estimate: 12h  
Dependencies: SKILL-6001  
Status: Not Started

Scope:
- Instrument per-skill latency, confidence, escalation, and failure counters.

Out of Scope:
- Automated adaptive optimization actions.

Implementation Tasks:
- Add telemetry capture hooks in skill execution pipeline.
- Expose metric rollups for KPI report path.
- Add tests/performance/test_skill_overhead.py.

Acceptance Criteria:
- Telemetry includes latency and escalation indicators per skill run.
- Performance test reports median and P95 overhead values.
- Failing threshold behavior is testable.

Verification Artifacts:
- tests/performance/test_skill_overhead.py
- metrics and observability path updates

Done Criteria:
- Merged with green CI.
- Requirement trace for PERF-0100 updated to SKILL-6002.

---

### Story SKILL-6003 - Release Readiness Skill

Type: IMPL  
Requirement(s): AGT-0116  
Estimate: 10h  
Dependencies: SKILL-6001 evidence schema stable  
Status: Not Started

Scope:
- Build release readiness evidence package skill.

Out of Scope:
- Final deployment automation orchestration.

Implementation Tasks:
- Implement src/skills/release_readiness.py.
- Aggregate checklist status, waivers, and approvals.
- Add tests/integration/test_skill_release_readiness.py.

Acceptance Criteria:
- Output package includes required checklist and waiver structures.
- Missing required release evidence generates explicit blockers.
- Integration tests verify pass and fail conditions.

Verification Artifacts:
- tests/integration/test_skill_release_readiness.py
- src/skills/release_readiness.py

Done Criteria:
- Merged with green CI.
- Requirement trace for AGT-0116 updated to SKILL-6003.

---

## Day-by-Day Sprint Execution Plan

### Week 1

#### Day 1 (Jul 19)

- Sprint kickoff and schema change review.
- Start SKILL-6001 state model updates.

#### Day 2 (Jul 20)

- Continue SKILL-6001 and add checkpoint tests.

#### Day 3 (Jul 21)

- Complete SKILL-6001 baseline integration.
- Start SKILL-6002 telemetry hook scaffolding.

#### Day 4 (Jul 22)

- Continue SKILL-6002 metric rollup implementation.
- Start SKILL-6003 module skeleton.

#### Day 5 (Jul 23)

- Continue SKILL-6002 performance test scaffolding.
- Continue SKILL-6003 package schema and tests.

### Week 2

#### Day 6 (Jul 26)

- Complete SKILL-6002 and calibrate thresholds.

#### Day 7 (Jul 27)

- Complete SKILL-6003 fail-path and pass-path checks.

#### Day 8 (Jul 28)

- Cross-story integration validation run.

#### Day 9 (Jul 29)

- Defect fixes and stabilization.

#### Day 10 (Jul 30)

- Update requirement trace fields and evidence links.

#### Day 11 (Jul 31)

- Sprint close-out and governance artifact review.

#### Day 12 (Aug 1)

- Phase review and retrospective notes.

---

## Sprint 6 Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Schema changes break existing checkpoints | Medium | High | Add backward-compatible migration and resume tests first |
| Telemetry noise obscures useful signals | Medium | Medium | Keep required metrics minimal and stable in Sprint 6 |
| Release readiness package misses required gate evidence fields | Low | High | Validate package schema with integration tests early |

---

## Sprint 6 Definition of Done

1. SKILL-6001, SKILL-6002, and SKILL-6003 are merged.
2. Checkpoint resume validates preserved skill evidence.
3. Telemetry/performance outputs are available and test-covered.
4. Requirement Trace: Work Item updates are complete.
5. Async standup board includes final evidence and blocker status.
