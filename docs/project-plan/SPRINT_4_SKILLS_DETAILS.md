# Sprint 4 Skills — Execution-Ready Stories

<!-- markdownlint-disable MD032 MD060 -->

**Sprint Window**: June 21 - July 4, 2026 (2 weeks)  
**Sprint Goal**: Establish skills runtime foundation and deliver first P0 skills for requirements quality and traceability with runnable smoke coverage.  
**Scope Source**: docs/project-plan/SKILLS_BACKLOG_DECOMPOSITION.md (Sprint 4 section)
**Async Standup Board**: docs/project-plan/SPRINT_4_SKILLS_ASYNC_STANDUP_BOARD.md  
**Default Workflow**: docs/project-plan/ASYNC_STANDUP_WORKFLOW.md

---

## Sprint 4 Story Set

| Story ID | Type | Requirement Link(s) | Estimate (hours) | Owner | Priority |
|----------|------|---------------------|------------------|-------|----------|
| SKILL-4001 | IMPL | AGT-0100 | 10 | Developer | P1 |
| SKILL-4002 | IMPL | AGT-0101 | 10 | Developer | P1 |
| SKILL-4003 | IMPL | INT-0100 | 12 | Developer | P1 |
| SKILL-4004 | IMPL | AGT-0110 | 8 | Developer | P1 |
| SKILL-4005 | IMPL | AGT-0113 | 8 | Developer | P1 |
| SKILL-4090 | TEST | TEST-0100 | 6 | Developer | P1 |

**Total Estimated Effort**: 54 hours  
**Planning Capacity Assumption**: 60 hours  
**Buffer**: 6 hours

---

## Dependency Order

Execution dependency sequence:

1. SKILL-4001 -> foundational contract model
2. SKILL-4002 -> requires SKILL-4001 contract types
3. SKILL-4003 -> requires SKILL-4001 and SKILL-4002
4. SKILL-4004 -> requires SKILL-4001 (contract-compliant skill output)
5. SKILL-4005 -> requires SKILL-4001 and partial SKILL-4003 integration hooks
6. SKILL-4090 -> requires SKILL-4002, SKILL-4003, SKILL-4004, SKILL-4005

Parallelization guidance:
- SKILL-4004 can start once SKILL-4001 reaches stable interface.
- SKILL-4005 can start after SKILL-4003 binding hook reaches first passing integration test.

---

## Story Details

### Story SKILL-4001 - Skill Contract Schema and Model

**Type**: IMPL  
**Requirement(s)**: AGT-0100  
**Estimate**: 10h  
**Dependencies**: None  
**Status**: Not Started

**Scope**:
- Define skill contract model and schema validation behavior.
- Include metadata, input/output schema, policy checks, traceability links, confidence, escalation.

**Out of Scope**:
- Runtime registry behavior.
- Supervisor binding and execution order.

**Implementation Tasks**:
- Create src/skills/contracts.py.
- Add validators for mandatory fields and schema shape.
- Add semantic version field validation.
- Add tests/unit/test_skill_contract_schema.py.

**Acceptance Criteria**:
- Contract model rejects incomplete definitions.
- Version parsing validates expected pattern.
- Unit tests cover valid/invalid schemas.

**Verification Artifacts**:
- tests/unit/test_skill_contract_schema.py
- src/skills/contracts.py

**Done Criteria**:
- Merged with green CI.
- Trace: Work Item for AGT-0100 updated to SKILL-4001.

---

### Story SKILL-4002 - Skill Registry and Resolution Engine

**Type**: IMPL  
**Requirement(s)**: AGT-0101  
**Estimate**: 10h  
**Dependencies**: SKILL-4001  
**Status**: Not Started

**Scope**:
- Build runtime skill registry and deterministic resolution by role/gate/discipline.

**Out of Scope**:
- Supervisor invocation hooks.
- Gate fail-closed enforcement.

**Implementation Tasks**:
- Create src/skills/registry.py.
- Add register/get/list/deprecate operations.
- Enforce duplicate id/version rejection.
- Add deterministic lookup strategy and tie-break behavior.
- Add tests/unit/test_skill_registry.py.

**Acceptance Criteria**:
- Duplicate id/version registration is blocked.
- Lookup by role/gate/discipline returns deterministic result.
- Deprecation state changes are reflected in lookup/list results.

**Verification Artifacts**:
- tests/unit/test_skill_registry.py
- src/skills/registry.py

**Done Criteria**:
- Merged with green CI.
- Trace: Work Item for AGT-0101 updated to SKILL-4002.

---

### Story SKILL-4003 - Agent-Skill Binding Hook in Supervisor

**Type**: IMPL  
**Requirement(s)**: INT-0100  
**Estimate**: 12h  
**Dependencies**: SKILL-4001, SKILL-4002  
**Status**: Not Started

**Scope**:
- Bind mandatory and optional skills in supervisor flow prior to gate readiness assembly.
- Record execution order into evidence log.

**Out of Scope**:
- Confidence threshold fail-closed enforcement (Sprint 5).

**Implementation Tasks**:
- Create src/config/skills.py policy map for gate/role requirements.
- Integrate binding and invocation in supervisor orchestration path.
- Implement ordered execution (mandatory then optional).
- Persist ordered execution metadata in run evidence.
- Add tests/integration/test_agent_skill_binding.py.

**Acceptance Criteria**:
- Mandatory skills run before readiness assembly.
- Optional skills run after mandatory set.
- Execution order appears in evidence payload.
- Integration test validates ordering and no authority mutation.

**Verification Artifacts**:
- tests/integration/test_agent_skill_binding.py
- src/config/skills.py
- src/graphs/supervisor.py updates

**Done Criteria**:
- Merged with green CI.
- Trace: Work Item for INT-0100 updated to SKILL-4003.

---

### Story SKILL-4004 - Requirements Quality Skill

**Type**: IMPL  
**Requirement(s)**: AGT-0110  
**Estimate**: 8h  
**Dependencies**: SKILL-4001  
**Status**: Not Started

**Scope**:
- Implement reusable requirements quality checks (format, mandatory attributes, hierarchy consistency checks).

**Out of Scope**:
- Gate fail-closed policy decisions.

**Implementation Tasks**:
- Create src/skills/requirements_quality.py.
- Validate noun-SHALL-verb and mandatory fields.
- Return structured violation records with requirement IDs and rule references.
- Add tests/unit/test_skill_requirements_quality.py.

**Acceptance Criteria**:
- Invalid requirement format generates violation output.
- Missing mandatory attributes generate violation output.
- Hierarchy anomaly detection returns violation list structure.

**Verification Artifacts**:
- tests/unit/test_skill_requirements_quality.py
- src/skills/requirements_quality.py

**Done Criteria**:
- Merged with green CI.
- Trace: Work Item for AGT-0110 updated to SKILL-4004.

---

### Story SKILL-4005 - Traceability Synthesis Skill

**Type**: IMPL  
**Requirement(s)**: AGT-0113  
**Estimate**: 8h  
**Dependencies**: SKILL-4001, SKILL-4003 (partial)  
**Status**: Not Started

**Scope**:
- Generate forward and backward trace links for requirements, architecture artifacts, work items, and tests.

**Out of Scope**:
- Final Gate 5+ coverage enforcement.

**Implementation Tasks**:
- Create src/skills/traceability_synthesis.py.
- Generate trace bundle and unresolved-link blocker list.
- Add tests/unit/test_skill_traceability_synthesis.py.

**Acceptance Criteria**:
- Trace bundle includes forward and backward links.
- Missing-link blockers are explicit and structured.
- Unit tests validate expected link structure and blocker behavior.

**Verification Artifacts**:
- tests/unit/test_skill_traceability_synthesis.py
- src/skills/traceability_synthesis.py

**Done Criteria**:
- Merged with green CI.
- Trace: Work Item for AGT-0113 updated to SKILL-4005.

---

### Story SKILL-4090 - Sprint 4 Skills Smoke Suite

**Type**: TEST  
**Requirement(s)**: TEST-0100  
**Estimate**: 6h  
**Dependencies**: SKILL-4002, SKILL-4003, SKILL-4004, SKILL-4005  
**Status**: Not Started

**Scope**:
- Validate Sprint 4 minimum integration path for registry resolution, execution order, and evidence merge.

**Out of Scope**:
- Missing mandatory evidence fail-closed behavior (Sprint 5).

**Implementation Tasks**:
- Add tests/integration/test_skills_smoke.py.
- Validate end-to-end invocation of selected mandatory skills.
- Assert authority fields remain unchanged by skill execution.

**Acceptance Criteria**:
- Smoke suite passes in CI.
- Evidence payload includes execution order and skill outputs.
- No authority ownership fields are mutated by skills.

**Verification Artifacts**:
- tests/integration/test_skills_smoke.py

**Done Criteria**:
- Merged with green CI.
- Trace: Work Item for TEST-0100 updated to SKILL-4090.

---

## Day-by-Day Sprint Execution Plan

### Week 1

#### Day 1 (Jun 21)

- Sprint kickoff, confirm scope and dependencies.
- Start SKILL-4001 (contract model skeleton and tests scaffold).

#### Day 2 (Jun 22)

- Complete SKILL-4001 and open PR.
- Start SKILL-4002 registry structure.

#### Day 3 (Jun 23)

- Continue SKILL-4002 lookup/deprecation logic.
- Start SKILL-4003 binding policy config skeleton in parallel.

#### Day 4 (Jun 24)

- Complete SKILL-4002 tests and merge readiness.
- Continue SKILL-4003 supervisor integration.

#### Day 5 (Jun 25)

- Complete core SKILL-4003 ordering behavior and integration test draft.
- Start SKILL-4004 requirements quality skill.

### Week 2

#### Day 6 (Jun 28)

- Complete SKILL-4004 and unit tests.
- Start SKILL-4005 traceability synthesis module.

#### Day 7 (Jun 29)

- Continue SKILL-4005 and tests.
- Stabilize SKILL-4003 integration test assertions.

#### Day 8 (Jun 30)

- Complete SKILL-4005.
- Start SKILL-4090 smoke suite and fixture alignment.

#### Day 9 (Jul 1)

- Complete SKILL-4090.
- Full regression run for Sprint 4 touched modules.

#### Day 10 (Jul 2)

- Buffer for defects, review fixes, documentation updates.
- Update Trace: Work Item fields for AGT-0100, AGT-0101, INT-0100, AGT-0110, AGT-0113, TEST-0100.

#### Day 11 (Jul 3)

- Sprint close-out checklist, governance evidence check, demo prep.

#### Day 12 (Jul 4)

- Gate readiness review and Sprint 4 retrospective notes.

---

## Sprint 4 Execution Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Contract churn delays downstream stories | Medium | High | Freeze contract interface at end of Day 2 |
| Supervisor integration complexity in SKILL-4003 | High | High | Add integration test scaffolding early on Day 3 |
| Smoke suite instability due to fixtures | Medium | Medium | Reuse deterministic test fixtures and mock outputs |
| Traceability skill scope creep | Medium | Medium | Keep Sprint 4 scope to link generation + blocker reporting only |

---

## Sprint 4 Definition of Done

1. SKILL-4001 through SKILL-4005 and SKILL-4090 are merged.
2. CI passes for unit and integration suites touched by these stories.
3. Requirement Trace: Work Item fields are updated for all Sprint 4 linked requirements.
4. Skills evidence appears in sprint demo output and includes execution ordering metadata.
5. No authority ownership mutation occurs due to skill execution.
