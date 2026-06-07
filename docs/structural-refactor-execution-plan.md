# Structural Refactor Execution Plan — IDE-Aligned Repo Layout

**Produced by:** Refactoring Agent (using `ide-structural-refactoring` skill) in collaboration with:
- Requirements Baseline Steward (`ide-requirements-baseline`)
- Architecture/Design Disposition Planner (`ide-architecture-design-disposition`)
- Governance Policy Compiler (`ide-governance-policy-compiler`)
- Source-to-Evidence Traceability Auditor (`ide-source-to-evidence-traceability`)
- Verification Coverage Planner (`ide-verification-coverage`)

**Date:** 2026-06 (initial execution plan, living document)  
**Parent Inputs:** 
- [ide-structure-requirements-baseline.md](./ide-structure-requirements-baseline.md)
- [ide-structure-architecture-disposition.md](./ide-structure-architecture-disposition.md)
- Reusability Evaluation Report
- LAYER_WORK_PACKAGE_INDEX.md (WP-XLEG-001, WP-XDOC-001, WP-XPACK-001, and related XGEN items)
- WAVE_01_R1_FOUNDATIONS_DETAILED_PLAN.md (E1.6 Cross XDOC/XLEG and supporting epics)
- IDE_REFACTOR_PLAN.md (layered, self-hosting focus)

**Gates:** G0 (intake for this plan), G1 (traceability of changes), G2 (structure contracts for editors/viewers/agents/skills), G4 (independent review of structural work), G5 (baseline after moves).

**Hierarchy Metadata (Functional Decomposition Applied):**
- Parent capability: Cross-layer Repo Structure + L5 Workspace (IDE as self-hosting workspace)
- Child function: Filesystem that enables L0 editors/viewers for agents/skills as first-class artifacts, L4 plugin host loading from packs, L7 ide-platform as home for platform process capabilities, clean separation of config vs. content, and functional decomp of L0-L8 layers.
- Decomposition level: 2–3
- Allocated component/module: root + platform/ (config only) + plugins/packs/ide-platform/ (content) + legacy/ + docs/archive/ + docs/ (living)
- Verification method: Traceability audit + compliance check + verification coverage + re-baseline post-execution

**Additional Traceability (per fleshed-out IDE_REFACTOR_PLAN.md §5):** This plan and its Tranche 2 execution trace to ide-structure-requirements-baseline.md (REQ-STRUCT-*) → L4/L5/Cross capabilities → detailed hierarchy on generalized artifacts and new L2 executor/tooling (see IDE_REFACTOR_PLAN.md and FRAMEWORK_DECOMPOSITION.md for full matrix and per-layer capabilities). All new ide-* agents/skills and tooling work packages carry Parent/Child/Level/Allocated/Verification fields.

---

## 1. Purpose and Scope
This plan executes the architecture/design disposition for an IDE-aligned repo structure. The goal is to make the filesystem itself a clean, discoverable, self-hosting example of the agentic IDE vision:
- Agents (.agent.md) and skills (SKILL.md) as first-class editable artifacts with natural homes that future IDE editors/viewers can open directly.
- Packs (L7) as the primary delivery mechanism for capabilities, including the platform's own process agents/skills in ide-platform.
- Clear separation of platform configuration (manifests, gates, schemas, temporary imports) from content.
- Functional decomposition of L0–L8 layers and cross-cuts visible in the layout.
- Legacy and historical material quarantined so it does not pollute active development or the "open as workspace" experience.
- Traceability, compliance, and verification hooks built in from the start (self-hosting the governance we are building).

**In scope (Wave 01 / R1 foundations):**
- Content moves for generalized assets (Requirements, Arch/Design, Governance/Compliance, Verification, and future ones).
- Legacy quarantine.
- Doc hygiene / archive.
- Reference and manifest updates.
- Evidence production for gates.

**Out of scope for this tranche:** Full L0/L1 surface implementation, bulk remaining XGEN, rich self-hosting demos (those come in later waves once the foundation is cleaner).

**Constraints:**
- All changes must preserve or improve source-to-evidence traceability (G1).
- Must pass compliance/policy check (ide-governance-policy-compiler).
- Must have verification coverage planned (ide-verification-coverage).
- PowerShell + GitHub native where possible for automation and evidence.
- Open to redlining: this plan will be fed back into the agents as better architecture emerges.

---

## 2. Architecture/Design Disposition Recap (from prior artifact)
**Chosen path:** Update architecture + controlled transition (rather than keep mixed state).

Key directives:
- Land generalized platform process content under `plugins/packs/ide-platform/agents/` and `plugins/packs/ide-platform/skills/`.
- Update ide-platform manifest and discovery.
- Quarantine bulk legacy `src/` (except runtime pieces we keep in `src/platform/`) to `legacy/src/`.
- Archive historical docs to `docs/archive/`.
- Keep `platform/` thin (config + staging only).
- Ensure the layout supports L0 editors/viewers, L4 loading, L7 packs, and self-hosting.

---

## 3. Detailed Execution Steps (with Agent/Skill Governance)

**Phase 0: Pre-Execution Governance (burn through procedures)**
- Re-run `ide-requirements-baseline` on this execution plan (if changes since baseline).
- Run `ide-architecture-design-disposition` to confirm/ redline this plan against the disposition.
- Run `ide-governance-policy-compiler` for compliance check (strict profile for platform core structure changes).
- Run `ide-source-to-evidence-traceability` on the current generalized assets + proposed moves (establish baseline chains).
- Run `ide-verification-coverage` on the requirements + disposition + this plan (produce coverage report and verification backlog for the moves).

**Phase 1: Content Moves (Generalized Assets into ide-platform Pack)**
1. Create `plugins/packs/ide-platform/agents/` and `plugins/packs/ide-platform/skills/` (if not present).
2. Move generalized agents:
   - requirements-baseline-steward.agent.md
   - architecture-design-disposition-planner.agent.md
   - governance-policy-compiler.agent.md
   - verification-coverage-planner.agent.md
   - source-to-evidence-traceability-auditor.agent.md (and future ones)
3. Move generalized skills (with their directories):
   - ide-requirements-baseline/
   - ide-architecture-design-disposition/
   - ide-governance-policy-compiler/
   - ide-verification-coverage/
   - ide-source-to-evidence-traceability/
4. Update `plugins/packs/ide-platform/plugin.manifest.yaml` entry (skills_dir, agents_dir) to point locally.
5. Update PLATFORM_AGENTS.md to reflect new locations under ide-platform pack.
6. Run `ide-source-to-evidence-traceability` post-move to confirm chains are intact.

**Tranche 2: Remaining XGEN (Post-Interruption — Full Remaining Set) — Added 2026-06 by Refactoring Agent invocation**
See dedicated invocation record: `agents/platform/invocations/remaining-xgen-refactoring-session.md` (contains full Phase 0 findings on the 5 pending MATM agents + remaining skills + 17 FarmRTK, the tranche plan, and execution log).

**Tranche 2 Scope (WP-XGEN-008+ and related):**
- 5 pending MATM agents: hierarchy-taxonomy-steward, independent-review-history-rollup-orchestrator, kpi-drift-analyst (incl. creating the missing ide-kpi-drift-analyst.agent.md to fix broken parent reference in its skill), repo-governance-autoflow-orchestrator, requirements-implementation-auditor.
- Associated/remaining MATM skills (hierarchy-taxonomy-steward, requirements-implementation-auditor, independent-review variants).
- Priority FarmRTK platform skills generalization (governance/audit/writer/validation/metrics family first; concepts for orchestrate/traceability/requirements already partially absorbed into meta and early ide-*). Create or extend ide-* in ide-platform.
- IDE integration: registration in ide-platform manifest + PLATFORM_AGENTS.md (pack section), full source-to-evidence + hierarchy metadata for L0-L8 + IDE surfaces (agent/skill as first-class editable artifacts), PowerShell + gh native examples, updates to REFACTOR_TODO, LAYER_WORK_PACKAGE_INDEX (XGEN progress), WAVE_01 detailed plan, and this execution plan.
- Self-hosting hook: After creation, re-apply ide-requirements-baseline / ide-architecture-design-disposition / ide-governance-policy-compiler / ide-source-to-evidence-traceability / ide-verification-coverage + this skill on the new artifacts + plan updates.

**Tranche 2 Execution Steps (Refactoring Agent + ide-structural-refactoring Phase 1 + Phase 3 disposition):**
1. Generalize each pending MATM agent into rich IDE-native .agent.md (ide- prefix for tranche clarity) following the exact template pattern of source-to-evidence-traceability-auditor.agent.md (mission, responsibilities, IDE-specific extensions for editors/viewers/agents-as-artifacts/L0-L8 decomp, execution policy with manifest/gate drive, PS/gh, parents, gates, success criteria).
2. Generalize supporting skills into ide-platform/skills/ (rich procedure style of ide-source-to-evidence-traceability/SKILL.md).
3. Create/fix ide-kpi-drift-analyst.agent.md (resolves the self-reference gap noted in Phase 0).
4. For FarmRTK priority: generalize technical-writer-farmrtk → ide-technical-writer (for living docs/ADRs), validation-plan-farmrtk → ide-validation-plan, program-metrics-farmrtk / related → enhancements or ide-program-metrics, plus any missing audit/writer items. Route orchestrate remnants back to ide-portfolio-planning if not new files.
5. Update cross-references and manifests (see "IDE integration updates" in the invocation record).
6. Produce evidence: traceability chains (source in imports → this tranche/plan → file in ide-platform), policy compliance note, verification coverage for the new generalized surface.
7. Append results and any redlines back to the invocation record and this plan.

**PowerShell example for Tranche 2:**
```powershell
# Example for one item (to be turned into reusable skill fragment)
pwsh -File tools/refactor/generalize-remaining-xgen.ps1 -Batch "matm-pending-5" -Target "plugins/packs/ide-platform" -AddIdeSurfaces -Hierarchy "L0-L8 + Cross XGEN"
gh issue create --title "Complete remaining MATM XGEN + kpi agent fix + FarmRTK audit batch" --label refactor,xgen,ide-platform --body-file evidence/remaining-xgen-*.md
```

**Gates for Tranche 2:** G1 (full chains for new items), G2 (editor/viewer contracts for the new .agent.md/SKILL.md), G4 (recommended on completion of this tranche + registration), G5 (post-tranche baseline).

**Owner:** Refactoring Agent (primary execution). Planning Agent (intake/sequencing via ide-portfolio-planning recommended immediately after this invocation). Collaborators: existing generalized ide-* agents/skills for the audits during creation.

**Status:** Plan section added. Execution of generalization and updates in progress in the linked invocation record. Open to redline from better architecture or self-host re-audit.

**Phase 2: Legacy Quarantine (XLEG)**
1. Create `legacy/src/` (mirror structure as needed).
2. Move bulk of `src/` (everything except `src/platform/`) to `legacy/src/`.
3. Move old top-level artifacts (PHASE_0_COMPLETE.md, IMPLEMENTATION_SUMMARY.md, NEXT_STEPS.md, QUICK_REFERENCE.md, validate_structure.py, old Examples/, non-essential old scripts, etc.) to `legacy/` or `docs/archive/` as appropriate.
4. Update pyproject.toml, Makefile, tests, README, and invocation records to reference legacy where needed and new structure for active development.
5. Add `legacy/README.md` explaining the quarantine and bridge strategy (selective ports of hitl, governance_validation, state ideas, etc., into L1/L2/L3/L4 as decided in disposition).
6. Run `ide-verification-coverage` and `ide-governance-policy-compiler` on the quarantine changes.

**Phase 3: Doc Hygiene / Archive (XDOC)**
1. Create/expand `docs/archive/`.
2. Move:
   - docs/governance/ (entire, except any living policy pieces)
   - docs/operations/ (entire)
   - docs/plans/ (old sprint boards, SPRINT_0/1/4/5/6/8 material, etc.)
   - docs/policies/ (entire)
   - Most of docs/project-plan/ (keep only AGENTIC_IDE_PROJECT_PLAN.md, WAVE_01_*, and living items)
   - docs/reviews/ (old items)
   - docs/references/ (historical)
3. Keep living/current near root of docs/ and under docs/charter/ (including ide-refactor/ artifacts).
4. Update root README, getting-started, and any "living docs" pointers.
5. Add `docs/archive/README.md` with index and pointers from living docs.
6. Run traceability and compliance audits on the archive moves.

**Phase 4: Thin platform/ + Reference Updates (XPACK + Polish)**
1. Ensure `platform/` contains only: manifest.yaml, gates/, schemas/, imports/ (raw staging + IMPORT_MANIFEST), README.
2. Move any remaining generalized content out (if any).
3. Update all references (plans, index, invocation records, manifests, etc.) to new locations.
4. Update ide-platform manifest and any future loader/discovery code.
5. Add root or workspace/ note: "This repo is intended to be opened as an example IDE workspace. See plugins/packs/ide-platform/ for platform process agents/skills."
6. Run full governance procedures (all five generalized skills) on the final state.

**Phase 5: Evidence, Compliance, Verification, and Closeout**
- Produce before/after structure snapshots.
- Full chain traceability report (`ide-source-to-evidence-traceability`).
- Compliance/policy status (`ide-governance-policy-compiler`).
- Verification coverage report + backlog (`ide-verification-coverage`).
- Evidence bundles for G1/G4/G5.
- Re-baseline requirements and re-disposition if redlines occurred.
- Update WAVE_01 plan, LAYER_WORK_PACKAGE_INDEX, and this plan itself with lessons (iteration loop).
- Hand off to G5 baseline for the foundation tranche.

---

## 4. Functional Decomposition of Changes (Hierarchy Applied)
- L4 (Plugin Host): ide-platform pack becomes primary home for platform process content.
- L5 (Workspace): Layout now supports opening repo as clean IDE workspace example.
- L7 (Packs): ide-platform demonstrates pack-delivered capabilities (including self-governance).
- Cross (Repo Structure + Legacy): Quarantine enables clean active surfaces; archive enables living docs.
- L0/L1/L2/L3: Future editors/viewers/orchestration/gates will have natural content to operate on without legacy noise.
- Verification hooks: Every phase has traceability + compliance + verification steps using the new skills.

---

## 5. Risks, Iteration, and Redline Plan
- Risk: Over-quarantine breaks something useful (mitigate with selective ports documented in legacy/README).
- Risk: References missed (mitigate with systematic search + re-run of traceability skill).
- Iteration: After each phase, feed results back into Requirements Baseline Steward and Architecture/Design Disposition Planner. Redline this plan and the baseline/disposition as needed.
- Self-hosting: The very agents/skills being used to govern this refactor are the first content benefiting from the new layout.

**Next burn through procedure after execution:** Re-run `ide-verification-coverage` on the post-move state and update the backlog. Use results to inform Wave 2 prioritization.

This plan is governed by the prioritized procedures and is itself subject to the same Requirements → Arch/Design → Compliance → Verification cycle. We remain fully open to refactoring loops as clearer designs emerge.