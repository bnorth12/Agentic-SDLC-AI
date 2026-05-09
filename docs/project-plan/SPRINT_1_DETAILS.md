# Sprint 1 — Details and Work Items

**Sprint Dates**: May 9 – May 23, 2026 (2 weeks)  
**Sprint Goal**: Establish planning baseline, development infrastructure, and architecture decomposition framework

---

## Sprint Summary

Sprint 1 transitions from Phase 0 (foundation) to Phase 1 (MVP completion). Focus areas:

| Area | Goal | Outcome |
|------|------|---------|
| **Planning** | Finalize backlog and architecture structure | Backlog complete, architecture decomposed into layers |
| **Infrastructure** | CI/CD and test harness | GitHub Actions pipeline operational with 80% coverage gate |
| **Engineering** | Layout L2 requirements for Sprint 2 | Roadmap for agent development clear and prioritized |

---

## Definition of Done

A work item is done when:
1. Code (if `[IMPL]`) merged to main and CI passes
2. Tests written and passing (≥80% coverage for changed modules)
3. Requirement traced (`Trace: Work Item` field updated in PRODUCT_REQUIREMENTS.md)
4. Documentation updated (if applicable)
5. All acceptance criteria met (listed below per item)

---

## Sprint 1 Backlog

### [GOV] Planning Item: Architecture Decomposition Structure

**Requirement**: ARCH-0001  
**Status**: Not Started  
**Priority**: P1-Critical  
**Acceptance Criteria**:
- [ ] Create `docs/architecture/` folder with structured decomposition documents
- [ ] Document all planned layers: Hardware Environment, Software Framework, Agent Subsystem, HITL/HMI, Governance
- [ ] For each layer, list sub-components (e.g., Agents under Agent Subsystem)
- [ ] Create Hardware Decomposition document (ARCH-0002) covering constraints/configuration
- [ ] Create Software Decomposition document (ARCH-0003) with Framework/Agents/HITL/Governance breakdown
- [ ] Create Component-to-Requirement Mapping matrix (ARCH-0004) showing which component implements each L2/L3 requirement
- [ ] Run inspection verification: confirm all L2/L3 requirements have assigned components, no requirement is unallocated
- [ ] Update PRODUCT_REQUIREMENTS.md: mark ARCH-0001 → ARCH-0004 as APPROVED (they are now planning baseline)

**Assigned To**: Developer  
**Est. Effort**: 8 hours  
**Trace to Requirements**: ARCH-0001, ARCH-0002, ARCH-0003, ARCH-0004  
**Deliverables**:
- `docs/architecture/DECOMPOSITION_STRUCTURE.md` (index and overview)
- `docs/architecture/HARDWARE_LAYERS.md` (hardware sub-layers and constraints)
- `docs/architecture/SOFTWARE_LAYERS.md` (software layers and sub-components)
- `docs/architecture/REQUIREMENT_COMPONENT_MAP.md` (bidirectional mapping matrix)
- Updated PRODUCT_REQUIREMENTS.md with ARCH requirements marked APPROVED

---

### [INFRA] Setup Task: CI/CD Pipeline Foundation

**Requirement**: INFRA-0001, INFRA-0010  
**Status**: Not Started  
**Priority**: P1-Critical  
**Acceptance Criteria**:
- [ ] Create `.github/workflows/ci.yml` with GitHub Actions job
- [ ] CI job runs: `ruff check src/ tests/`, `mypy src/`, `pytest tests/ --cov=src --cov-fail-under=80`
- [ ] Confirm linting rules in `pyproject.toml` (Ruff) and `mypy.ini` configured
- [ ] Add coverage badge to README.md
- [ ] Create a test branch deliberately reducing coverage below 80% and confirm CI job fails/blocks merge
- [ ] Document CI process in `docs/development-guide.md` (update existing doc)
- [ ] Update PRODUCT_REQUIREMENTS.md: mark INFRA-0001 and INFRA-0010 as APPROVED

**Assigned To**: Developer  
**Est. Effort**: 6 hours  
**Trace to Requirements**: INFRA-0001, INFRA-0010  
**Deliverables**:
- `.github/workflows/ci.yml` (working CI pipeline)
- Updated `pyproject.toml` with Ruff, mypy configs
- Test PR demonstrating coverage gate working
- Updated `docs/development-guide.md`

---

### [INFRA] Setup Task: Mock LLM Test Harness

**Requirement**: INFRA-0002  
**Status**: Not Started  
**Priority**: P1-Critical  
**Acceptance Criteria**:
- [ ] Update `tests/conftest.py` with pytest fixture `mock_ollama` that stubs ChatOllama
- [ ] Mock returns deterministic outputs (e.g., fixed JSON responses for agents)
- [ ] Set environment variable `MOCK_LLM=1` to enable mock mode in tests
- [ ] Run full unit test suite (`pytest tests/unit/`) with mock mode enabled; confirm all tests pass
- [ ] Measure execution time; confirm full suite completes in under 60 seconds
- [ ] Update CI job to use `MOCK_LLM=1` so CI tests don't require Ollama
- [ ] Document mock mode in `NEXT_STEPS.md`

**Assigned To**: Developer  
**Est. Effort**: 4 hours  
**Trace to Requirements**: INFRA-0002  
**Deliverables**:
- Updated `tests/conftest.py` with mock harness
- Updated `.env.example` documenting `MOCK_LLM`
- Updated `.github/workflows/ci.yml` to set `MOCK_LLM=1`
- Updated `NEXT_STEPS.md` with mock mode documentation

---

### [GOV] Planning Item: Sprint 2–3 Backlog Refinement

**Requirement**: AGT-0002, AGT-0003, AGT-0004, AGT-0005  
**Status**: Not Started  
**Priority**: P2-High  
**Acceptance Criteria**:
- [ ] Decompose AGT-0002 (Requirements Noun-SHALL-Verb Elicitation) into Sprint 2 tasks:
  - [ ] `[IMPL]` Add format validation to Requirements Agent (references AGT-0010)
  - [ ] `[TEST]` Unit tests for noun-SHALL-verb parser (references AGT-0010)
- [ ] Decompose AGT-0003 (Unique ID Assignment) into Sprint 2 tasks:
  - [ ] `[IMPL]` Add ID registry and uniqueness check to Requirements Agent
  - [ ] `[TEST]` Unit tests for ID collision detection (references AGT-0011)
- [ ] Decompose AGT-0004 (Full Attribute Population) into Sprint 2 tasks:
  - [ ] `[IMPL]` Update `Requirement` Pydantic model with Level and Trace:Children fields
  - [ ] `[IMPL]` Add validation that rejects APPROVED transition if attributes absent
- [ ] Decompose AGT-0005 (Hierarchy Decomposition) into Sprint 2 tasks:
  - [ ] `[IMPL]` Add orphan detection logic to Requirements Agent
  - [ ] `[IMPL]` Add decomposition gap reporting
  - [ ] `[TEST]` Unit tests for hierarchy validation (references AGT-0012)
- [ ] Create `docs/project-plan/SPRINT_2_DETAILS.md` with estimated tasks and dependencies
- [ ] Create `docs/project-plan/SPRINT_3_DETAILS.md` (high-level outline)

**Assigned To**: Developer  
**Est. Effort**: 6 hours  
**Trace to Requirements**: AGT-0002, AGT-0003, AGT-0004, AGT-0005  
**Deliverables**:
- `docs/project-plan/SPRINT_2_DETAILS.md` (detailed Sprint 2 backlog)
- `docs/project-plan/SPRINT_3_DETAILS.md` (outline Sprint 3)
- Updated PRODUCT_REQUIREMENTS.md: L2 requirements (AGT-0002 → AGT-0005) marked APPROVED with Sprint 2 work items linked

---

### [DOC] Documentation: Governance Requirements Authoring Guide

**Requirement**: AGT-0002 (supporting), RMP-PLAN-001  
**Status**: Not Started  
**Priority**: P2-High  
**Acceptance Criteria**:
- [ ] Create `docs/requirements/AUTHORING_GUIDE.md` with examples:
  - [ ] Good/bad requirement statements
  - [ ] L0/L1/L2/L3 examples from PRODUCT_REQUIREMENTS.md
  - [ ] Derivation statement patterns
  - [ ] Trace field population rules
  - [ ] Rollup verification for L0/L1
- [ ] Link from `docs/plans/requirements-management-plan.md` to new guide
- [ ] Update README.md with link to requirements guide

**Assigned To**: Developer  
**Est. Effort**: 3 hours  
**Trace to Requirements**: RMP-PLAN-001  
**Deliverables**:
- `docs/requirements/AUTHORING_GUIDE.md` (requirements authoring guide)
- Updated `docs/plans/README.md` with link
- Updated README.md

---

### [TEST] Expand Governance Test Suite

**Requirement**: GOV-0001, AGT-0001  
**Status**: Not Started  
**Priority**: P2-High  
**Acceptance Criteria**:
- [ ] Review existing governance tests (`tests/unit/test_governance_validation.py`, etc.)
- [ ] Add test cases for edge cases:
  - [ ] Missing policy_compliance field (should fail validation)
  - [ ] Empty evidence_links array (should fail validation)
  - [ ] Orphan risks_or_blockers without mitigations (should warn)
- [ ] Expand supervisor hook tests to cover multiple agents' outputs
- [ ] Add integration test for full Gate 1 → Gate 2 transition with governance validation
- [ ] Ensure coverage remains ≥80%

**Assigned To**: Developer  
**Est. Effort**: 4 hours  
**Trace to Requirements**: GOV-0001, AGT-0001  
**Deliverables**:
- Expanded `tests/unit/test_governance_validation.py`
- New test: `tests/integration/test_gate_transitions.py`
- All tests passing with ≥80% coverage

---

## Sprint 1 Rollup & Gate 1 Readiness

### Definition of Sprint 1 Success

| Criterion | Target | Status |
|-----------|--------|--------|
| All work items completed | ✓ | In Progress |
| Architecture decomposition approved by Chief Engineer | ✓ | Pending |
| CI/CD pipeline operational and coverage gate active | ✓ | In Progress |
| L2 requirements approved and Sprint 2 tasks decomposed | ✓ | Pending |
| Requirements authoring guide complete | ✓ | Pending |
| Test suite ≥80% coverage | ✓ | Pending |
| All blockers and risks documented | ✓ | Pending |

### Blockers / Risks to Monitor

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Architecture decomposition becomes politicized (HW/SW layers unclear) | Low | High | Involve Chief Engineer early; use reference architecture standards |
| CI/CD setup blocked by environment issues (Ruff/mypy config conflicts) | Medium | Medium | Test CI setup in isolated container early |
| Mock LLM harness reduces test realism, misses integration issues | Medium | Medium | Maintain separate integration test suite with live Ollama (lower frequency) |
| Sprint 2 Requirements Agent implementation more complex than estimated | High | High | Plan buffer time; break AGT-0002 into smaller tasks if needed |

### Approved Requirements at Sprint 1 Close

The following requirements transition to APPROVED status upon Sprint 1 completion:

- **ARCH-0001** — Architecture Decomposition Structure
- **ARCH-0002** — Hardware Decomposition
- **ARCH-0003** — Software Decomposition
- **ARCH-0004** — Component-to-Requirement Mapping
- **INFRA-0001** — CI/CD Pipeline
- **INFRA-0010** — Coverage Threshold Enforcement
- **INFRA-0002** — Mock LLM Mode

All L1 requirements (SYS-0001 → SYS-0006) remain APPROVED.  
All L2 requirements (AGT-0002 → AGT-0005, etc.) transition to APPROVED with Sprint 2 work items linked.

---

## Sprint 1 Effort Estimate

| Item | Est. Hours |
|------|-----------|
| Architecture Decomposition | 8 |
| CI/CD Pipeline | 6 |
| Mock LLM Harness | 4 |
| Sprint 2–3 Refinement | 6 |
| Requirements Authoring Guide | 3 |
| Governance Test Expansion | 4 |
| **Total** | **31 hours** |

**Calendar Capacity** (2 weeks, assuming 20 hours dev time per week): 40 hours  
**Buffer**: 40 − 31 = 9 hours (contingency for blockers, integration work)

---

## Sprint 1 Dependencies & Sequencing

```
Day 1–2   → Architecture Decomposition (blocking: planning for rest of sprint)
Day 2–3   → CI/CD Pipeline Setup (depends: completed architecture to know scope)
Day 3–4   → Mock LLM Harness (depends: CI pipeline to integrate with)
Day 4–5   → Governance Test Expansion (depends: infrastructure ready)
Day 5–10  → Sprint 2–3 Refinement (depends: Sprint 1 tasks complete)
Day 10    → Requirements Authoring Guide (low dependency)
```

**Critical Path**: Architecture → CI/CD → Mock LLM → Tests → Sprint Planning  
**Slack**: Authoring Guide can slip to Day 11 if needed

---

## Exit Criteria (Gate 1 Sprint Review)

To transition Sprint 1 to **VERIFIED** status and proceed to Sprint 2 gate, **all** of the following must be true:

1. ✓ Architecture decomposition reviewed and approved by Chief Engineer
2. ✓ All backlog items COMPLETED and merged to main
3. ✓ CI pipeline green on main (all tests passing, coverage ≥80%)
4. ✓ Sprint 2 backlog formally decomposed and Sprint 2 tasks linked to L2 requirements
5. ✓ No open P1 blockers (P2/P3 blockers acceptable with documented mitigation)
6. ✓ Risk register updated with Sprint 2 risks
7. ✓ All changed modules have updated documentation
8. ✓ PRODUCT_REQUIREMENTS.md updated with Sprint 1 work item traces

**Gate 1 HITL Sign-Off**: Developer and Chief Engineer review above criteria; Chief Engineer approves sprint exit or requests additional work.
