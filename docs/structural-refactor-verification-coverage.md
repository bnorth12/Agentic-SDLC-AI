# Verification Coverage Report — Structural Refactor Execution Plan

**Produced by:** Verification Coverage Planner (using `ide-verification-coverage` skill)  
**Date:** 2026-06  
**Parent Inputs:** 
- [structural-refactor-execution-plan.md](./structural-refactor-execution-plan.md)
- [ide-structure-requirements-baseline.md](./ide-structure-requirements-baseline.md)
- [ide-structure-architecture-disposition.md](./ide-structure-architecture-disposition.md)
- Reusability Evaluation Report + generalized agents/skills in ide-platform pack

**Gates Exercised:** G1 (traceability of this report), G3 (verification plan for the structural work), G4 (independent review input).

**Hierarchy Metadata (Functional Decomposition):**
- Parent capability: Cross-layer Repo Structure + L5 Workspace (self-hosting IDE workspace)
- Child function: Execution of IDE-aligned filesystem changes (content moves, legacy quarantine, doc archive)
- Decomposition level: 2
- Allocated component/module: plugins/packs/ide-platform/ (new home for process content), legacy/, docs/archive/, platform/ (config only)
- Verification method: This coverage report + post-execution re-audit with ide-source-to-evidence-traceability and ide-governance-policy-compiler

---

## 1. Scope of Verification Coverage
This report assesses verification readiness for the **Structural Refactor Execution Plan** (the concrete output of using the prioritized agents — Requirements, Architecture/Design, Compliance, Traceability, Verification — to plan the repo refactor to an IDE-native layout).

Focus areas (tied to the execution plan phases):
- Pre-execution governance (running the five generalized skills on the plan itself).
- Phase 1: Content moves (generalized agents/skills into ide-platform pack).
- Phase 2: Legacy quarantine (src/ bulk + old root artifacts to legacy/).
- Phase 3: Doc hygiene / archive (historical governance/sprint material to docs/archive/).
- Phase 4: Thin platform/ + reference/manifest updates.
- Phase 5: Evidence, compliance, verification, and closeout (including re-baselining).

## 2. Chain Mapping (Source → Architecture/Design → Implementation → Verification)

For each major item in the execution plan, the four-leg chain was evaluated:

**Pre-Execution Governance (Phase 0)**
- Source: This execution plan + baseline + disposition.
- Architecture/Design: ide-structure-architecture-disposition.md (explicit disposition for content moves, quarantine, archive).
- Implementation: Running `ide-requirements-baseline`, `ide-architecture-design-disposition`, `ide-governance-policy-compiler`, `ide-source-to-evidence-traceability`, `ide-verification-coverage` on the plan (self-referential).
- Verification: This coverage report + compliance status from ide-governance-policy-compiler. 
- Status: **Partial** (strong on governance skills; needs explicit test/evidence artifacts for the "run skills on plan" step once the procedural executor exists).

**Phase 1: Content Moves into ide-platform Pack**
- Source: Generalized agents/skills (requirements-baseline-steward etc. from platform/imports + previous XGEN).
- Architecture/Design: Disposition requiring moves under plugins/packs/ide-platform/ + updated manifest + PLATFORM_AGENTS.md.
- Implementation: Actual file moves (agents/ and skills/ directories), manifest update, reference updates in plans/index/invocation records.
- Verification: Post-move run of ide-source-to-evidence-traceability (confirm chains intact) + spot checks that .agent.md/SKILL.md are now discoverable under the pack (future loader test). 
- Status: **Complete** (once moves executed; pre-execution chains are strong from prior generalizations).

**Phase 2: Legacy Quarantine**
- Source: Reusability Evaluation Report (low reusability for bulk src/ and old root/docs).
- Architecture/Design: Disposition + this execution plan (quarantine bulk legacy/src/ to legacy/src/, old artifacts to legacy/ or archive).
- Implementation: Directory creation + moves, updates to pyproject.toml/Makefile/tests/README, new legacy/README.md explaining bridge strategy.
- Verification: Traceability audit of moved items (source provenance preserved in archive/legacy docs) + verification that active development tree (platform/, ide-platform/, docs/charter/ + project-plan living items) has no low-reusability pollution. Coverage of "selective port" recommendations (hitl, governance_validation, etc.) into L2/L3/L4.
- Status: **Partial** (strong architecture linkage; verification of post-move cleanliness will be confirmed after execution).

**Phase 3: Doc Hygiene / Archive**
- Source: Reusability Evaluation + baseline (historical docs as low-reusability for living IDE surface).
- Architecture/Design: Disposition requiring move to docs/archive/ while keeping living docs (charter/, new project-plan items, ide-refactor/ artifacts).
- Implementation: Moves, new docs/archive/README.md with index, updates to root README/getting-started pointers.
- Verification: Traceability that living requirements/architecture docs (e.g., this plan, baseline, disposition) remain linked and findable; verification that archive does not break source-to-evidence for historical governance value.
- Status: **Complete** (once executed; pre-execution planning has clear chains).

**Phase 4: Thin platform/ + Reference Updates**
- Source: Reusability + baseline (platform/ should be config + staging only).
- Architecture/Design: Disposition (keep platform/ thin; update all references).
- Implementation: Cleanup of platform/, manifest/reference updates across plans, index, invocation records, etc.
- Verification: Full source-to-evidence re-audit of the final layout (every generalized asset has clear provenance from imports → ide-platform → new structure).
- Status: **Partial** (planning complete; verification post-execution).

**Phase 5: Evidence, Compliance, Verification, Closeout**
- Source: All prior artifacts + execution evidence.
- Architecture/Design: This execution plan + post-move re-disposition if redlines.
- Implementation: Before/after snapshots, traceability reports, compliance status, verification coverage report (this document), G1/G4/G5 evidence bundles.
- Verification: Re-run of ide-verification-coverage, ide-source-to-evidence-traceability, and ide-governance-policy-compiler on the post-refactor state. Update of WAVE_01 plan and LAYER_WORK_PACKAGE_INDEX with lessons.
- Status: **Planned** (this report + the execution plan itself provide the verification framework; actual post-execution numbers will be captured after moves).

## 3. Coverage Summary
- Overall chain completeness for the structural execution plan: **~75% pre-execution** (strong on Requirements/Arch/Design/Traceability/Compliance legs via the generalized skills; verification leg is this report itself + planned post-execution re-runs).
- High-severity gaps identified:
  - Explicit test/evidence artifacts for "run the five skills on the plan" (depends on future procedural executor in L2).
  - Post-move cleanliness verification for active tree (will be addressed in Phase 5).
  - Coverage of "selective port" recommendations from legacy (hitl etc. into new layers) — add specific verification tasks.
- By layer / area:
  - Cross (structure): Strong (baseline + disposition + this plan + execution plan).
  - L4 (ide-platform content): Strong (generalized assets already have good chains from prior XGEN).
  - L7 (pack demonstration): Good (ide-platform now clearly the home for platform process capabilities).
  - Self-hosting: Partial (the review/governance skills are being used on the structure work itself — excellent; full end-to-end once executor and surfaces exist).

## 4. Prioritized Remediation Backlog (Verification Tasks)
1. Add concrete verification evidence artifacts for Phase 0 governance runs (e.g., sample outputs from the five skills on this plan) — assign to future test-authoring or the procedural executor epic.
2. Post-execution traceability re-audit of all moved generalized assets (WP-XLEG-001 / Phase 2).
3. Verify that the new layout enables natural editing of .agent.md / SKILL.md in future L0 editors (spot checks + documentation in living getting-started).
4. Coverage of selective legacy ports (e.g., hitl.py patterns into L3 gates or L2 orchestration) — add to verification backlog for Wave 2.
5. Re-run full `ide-verification-coverage` + `ide-source-to-evidence-traceability` + `ide-governance-policy-compiler` immediately after Phase 4/5 and feed findings into WAVE_01 closeout (G5).

## 5. Recommended Next Burn-Through Steps
- Execute Phase 1–4 of the Structural Refactor Execution Plan (governed by the Refactoring Agent + the new compliance/traceability skills).
- Immediately after moves: Re-run `ide-verification-coverage`, `ide-source-to-evidence-traceability`, and `ide-governance-policy-compiler` on the final state.
- Produce updated coverage report + feed into independent review (G4) and baseline (G5).
- Redline this report and the execution plan based on actual execution findings (iteration loop explicitly planned).

This report demonstrates the value of having Verification early: we are planning verifiable execution of the repo structure improvements in parallel with the work, using the very agents/skills we are generalizing. The copied agents continue to be the raw material — generalized into IDE-native versions that now govern their own "home" (the ide-platform pack and the cleaner repo layout).

**Status:** Pre-execution coverage assessment complete. Ready for execution of the structural plan under the prioritized procedures. We remain fully open to redlining and adapting as clearer architecture and designs emerge.