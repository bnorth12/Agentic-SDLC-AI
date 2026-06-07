# Next Wave Charter — WAVE-02-R1-FOUNDATIONS-TOOLS-EXECUTOR

**Produced by:** Planning Agent (embodied via `ide-portfolio-planning` skill)  
**Date:** Current session (immediately following L2 executor + first core tools implementation and simulated matrix audit)  
**Parent Inputs:** 
- `agents/platform/invocations/remaining-xgen-refactoring-session.md` (Tranche 2 completion)
- `docs/charter/IDE_REFACTOR_PLAN.md` (new §5 Architecture Traceability, Capabilities & Functional Decomposition — **explicitly referenced throughout this charter**)
- `docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md` (the standalone matrix — **explicitly referenced**)
- `docs/structural-refactor-execution-plan.md` (Tranche 2 section)
- `docs/charter/ide-refactor/LAYER_WORK_PACKAGE_INDEX.md`
- `WAVE_01_R1_FOUNDATIONS_DETAILED_PLAN.md`

**Status:** Ready for G0 intake verdict and execution.

---

## Executive Summary

With the L2 procedural skill executor (`src/platform/orchestration/executor.py`) and first core IDE tools (`src/platform/tools/ide_core.py`: `read_ide_artifact`, `write_ide_artifact`, `validate_hierarchy_metadata`, `basic_generalize_stub`) now implemented and the router wired, we can move from manual simulation to executable self-hosting.

This wave enables the new runtime so the generalized Tranche 2 agents/skills (and future ones) can actually *run*, performs the first live self-hosted traceability audit on the architecture surface (matrix + §5), completes the next FarmRTK XGEN tranche using the new tools, and closes foundational G1/G2 evidence.

**Explicit references (per user request):**
- All scope, work packages, hierarchy, and evidence requirements in this charter are derived from **IDE_REFACTOR_PLAN.md §5** and the **IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md**.
- The matrix is the single source of truth for traceability during this wave.

---

## Wave Goal

Enable autonomous execution of the new IDE platform capabilities (L2 executor + tools) so that the Refactoring Agent and Planning Agent can continue generalization, audits, and structural work with minimal manual intervention.

---

## Scope Boundaries (from ide-portfolio-planning procedure + matrix)

**In scope:**
- Wiring, testing, and first live runs of the executor against real Tranche 2 SKILL.md files (start with `ide-hierarchy-taxonomy-steward` and `ide-requirements-implementation-auditor`).
- Integration of `ide_core.py` tools into the executor (support for "tool:" steps) and initial tool registry (L4).
- Live self-hosted traceability audit: invoke generalized skills on the matrix + IDE_REFACTOR_PLAN §5 + updated docs (see simulated audit file for baseline).
- Next FarmRTK priority XGEN batch using the new tools (repo-audit, process-audit, program-metrics, check-work-commit, configuration-baseline patterns).
- Structural content moves + reference cleanup for Tranche 2 items.
- Extension of the traceability matrix with live evidence rows + any additional visuals.
- Update of invocation records, layer index, and this charter with results.

**Out of scope (deferred):**
- Full L0/L1 surfaces (editors, ACP sessions).
- Complete remaining 17 FarmRTK (only priority governance/audit batch).
- Rich GitHub provider or installer work.
- Full tool permission model (basic registry only).

**Constraints:**
- All changes must update the matrix and reference IDE_REFACTOR_PLAN §5.
- PowerShell primary for execution examples.
- Hierarchy metadata required on all new or changed artifacts.
- Evidence must be consumable by the matrix.

---

## Detailed Epics & Tasks (tied to layers + matrix)

### E2.1 L2: Executor + Tool Integration (Highest Leverage)
**Layers:** L2 (primary), L4 (tool registry).
**Matrix rows:** L2-001, TOOL-001, L2-002.
**Tasks:**
1. Extend executor to support "tool:" steps that call functions from `ide_core.py`.
2. Add basic tool registry (dict of name → callable) in L4 or orchestration.
3. Test executor end-to-end on 2+ Tranche 2 skills; capture real evidence bundles.
4. Update matrix rows with live results.

**PowerShell example:**
```powershell
pwsh -File tools/executor/run-skill.ps1 -Skill ide-hierarchy-taxonomy-steward -Workspace . -Output evidence/live-run-hierarchy-$(Get-Date -Format yyyyMMdd).md
```

**Verification:** Executor produces evidence that passes `validate_hierarchy_metadata` from the new tools.

### E2.2 Cross XSELF: Live Self-Hosted Audit
**Layers:** Cross XSELF.
**Matrix rows:** XSELF-001.
**Tasks:**
1. Using the live executor + tools, invoke the four generalized audit skills on the matrix + §5.
2. Produce updated audit report (extend `docs/structural-refactor-traceability-audit-on-matrix.md`).
3. Close any remaining "Pending" legs in the matrix.

**Verification:** Full G1 chains confirmed in the matrix; evidence bundles attached.

### E2.3 Cross XGEN: Next FarmRTK Batch + Tool-Assisted Generalization
**Layers:** L7 + Cross XGEN.
**Matrix rows:** XGEN-001 (extended).
**Tasks:**
1. Generalize next 5-6 FarmRTK skills using `basic_generalize_stub` + manual Refactoring Agent pass (or live tools once wired).
2. Place in ide-platform.
3. Update matrix and invocation record.

---

## Gates & Evidence

- **G0:** This charter document (produced by Planning Agent).
- **G1:** Live traceability audit results updating the matrix.
- **G2:** Executor + tool interface contracts (new code + tests).
- **G4:** Recommended after live audit (preparatory evidence already in simulated audit file).

**Success Criteria (measurable):**
- Executor runs at least two real Tranche 2 SKILL.md procedures and returns structured evidence.
- At least one tool from `ide_core.py` is called from within an executed skill.
- Matrix has live evidence for L2-001 and TOOL-001 rows.
- Updated audit report + matrix committed.
- Next wave charter references §5 and the matrix (self-referential).

---

## Ownership & Escalation

- **Planning Agent:** Overall sequencing, this charter, portfolio balance.
- **Refactoring Agent:** Execution of wiring, live audit, generalization using new tools, structural moves.
- **Chief Engineer:** Architecture disposition for the executor + tool layer (hierarchy at L2/L4).

Escalation: Architecture misalignment on tool permissions → Chief Engineer + mandatory HITL. Legacy surface issues during FarmRTK work → Planning Agent re-sequencing.

---

## PowerShell / GitHub Native Emphasis

See examples in E2.1. All evidence will be attachable via `gh` (future L6 skills).

---

**This charter explicitly references IDE_REFACTOR_PLAN.md §5 and IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md as the authoritative sources for scope, capabilities, functional decomposition, and traceability requirements.**

**Status:** Charter complete. Ready for G0 and immediate execution of the follow-on wave.

**Related:** Update `WAVE_01_R1...` and layer index after this wave. Self-hosting loop: this charter was produced using the new matrix and §5. 

**End of Planning Agent charter document.**