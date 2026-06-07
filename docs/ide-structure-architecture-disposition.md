# IDE Structure — Architecture/Design Disposition

**Produced by:** Architecture/Design Disposition Planner (using `ide-architecture-design-disposition` skill)  
**Date:** 2026-06  
**Parent Input:** [ide-structure-requirements-baseline.md](./ide-structure-requirements-baseline.md)  
**Gates:** G1 (traceability), G2 (contracts for new surfaces/structure).  
**Hierarchy:** Parent = Cross-layer Repo Structure + L5 Workspace; Child = Filesystem layout supporting L0 editors, L4 plugin host content, L7 ide-platform pack, self-hosting; Decomposition level = 2; Allocated = root + platform/ + plugins/packs/ide-platform/ + agents/ + docs/ (living) + legacy/ + docs/archive/; Verification = compliance audit + re-baseline after changes.

---

## 1. Workpack Summary (from requirements baseline)

The baseline identified three high-severity structural requirements:
- REQ-STRUCT-001: Separate platform configuration from content (agents, skills, pack-delivered capabilities).
- REQ-STRUCT-002: First-class IDE artifacts (agents/skills/manifests/evidence) must live in discoverable, editable locations aligned with the pack model.
- REQ-STRUCT-003: Legacy and historical material must be quarantined.

Additional medium requirements around functional decomposition of L0-L8, packaging alignment, and explicit traceability from structure decisions back to IDE requirements (editors for agents/skills, self-hosting, etc.).

## 2. Analysis of Current State vs. Targets

Current state (as of this session):
- Good direction: `plugins/packs/ide-platform/` now holds the generalized Requirements, Arch/Design, and Governance agents/skills. `platform/` is starting to look more like config + staging. New plans live under `docs/project-plan/`.
- Problems:
  - Generalized skills still referenced in the old `ide-platform` manifest pointing to `../../../platform/skills` (we updated the manifest in this session, but the physical move of content happened only for the three we just generalized).
  - `agents/` only contains the platform subdir (good start, but not yet under the pack).
  - `platform/skills/` still exists with the two we moved conceptually.
  - Heavy legacy (`src/` full monolith, root-level old docs, `docs/governance/`, old `docs/project-plan/` sprint boards, `Examples/`, scripts focused on old Docker/Ollama flow) still mixed in the active tree.
  - `src/platform/` (the runtime) is inside the legacy `src/` tree, which is confusing for an IDE that will edit both content and some platform runtime.

## 3. Disposition Decision

**Chosen Path: Update Architecture/Design (and implementation) to match the target IDE model, with controlled transition.**

Rationale:
- The requirements are solid and directly support the core vision (agents/skills as first-class editable artifacts, packs as the delivery mechanism, clean self-hosting workspace, L0-L8 decomposition visible in the filesystem).
- Keeping the current mixed state will make future editor/viewer/compliance work harder and will pollute any "open this repo as a workspace" experience.
- We are still early (R1 foundations). Better to make the structural decision now, while the amount of generalized content is small, than after we have burned through dozens of XGEN items.
- Iteration is expected and planned (per current direction): we will redline this disposition and the resulting structure as we exercise more procedures and gain clearer architecture understanding.

**Explicit Disposition Path:**
- Move generalized platform process content (agents + skills for Requirements, Arch/Design, Governance/Compliance, and future Verification/Planning) fully under `plugins/packs/ide-platform/agents/` and `plugins/packs/ide-platform/skills/`.
- Update the `ide-platform` manifest (already partially done) and any discovery code to point at the pack-local directories.
- Create `legacy/` for the bulk of the old `src/` (everything except the runtime pieces we decide to keep in `src/platform/` for now) + old root docs/scripts/Examples that are not part of the living IDE.
- Create/expand `docs/archive/` for historical governance, old sprint boards, PHASE_0/IMPLEMENTATION_SUMMARY material, etc. Keep only living/current docs near the root of `docs/` and under `docs/charter/`.
- Re-home the two new Planning and Refactoring agents (and their skills) cleanly under the ide-platform pack (they were the first "content" we created; they belong with the other process capabilities).
- Leave `platform/` as thin config + schemas + temporary raw imports staging only.
- Keep `gui/`, `workspace/`, `plugins/packs/` (other packs), and the new `docs/project-plan/` (the living IDE plans) as active development surfaces.
- Add a small root-level or `workspace/` note that this repo is intended to be opened as an example IDE workspace.

**Trade-offs accepted:**
- Short-term churn of moving files and updating a handful of references (manifests, index, plans, invocation record).
- Some old tests and the full old `src/` will be broken until we decide what (if anything) to port or bridge (this is acceptable in R1; we are not claiming the legacy path still runs).
- We may discover better conventions once we have the actual agent/skill editors and structure viewers (we will redline this disposition then).

## 4. Implementation Directives (for Refactoring Agent)

1. Perform the content moves into `plugins/packs/ide-platform/`.
2. Quarantine legacy material.
3. Archive historical docs.
4. Update the ide-platform manifest, LAYER_WORK_PACKAGE_INDEX, WAVE_01 detailed plan, invocation record, and any "open as workspace" docs.
5. Produce evidence (before/after structure, updated manifests, new living docs pointers).
6. Re-run the requirements baseline and this disposition after the changes (self-hosting loop).

## 5. Verification & Compliance Follow-up

- This disposition must be reviewed under G4 (independent review / EIRC) as part of Wave 01.
- Compliance check (ide-governance-policy-compiler) of the changes against current policies and the layered model.
- After execution, produce an updated requirements baseline and re-verify traceability (G1).
- Any new requirements discovered during the move become input to the next baseline cycle.

---

**Status:** Disposition chosen and recorded. Ready for Refactoring Agent execution under compliance/verification.

This is a living document. As we burn through more procedures (especially once we generalize verification and additional compliance assets), we will redline and adapt both this disposition and the resulting structure. Hardware benchmarks remain deferred until the procedures are exercised and hardware is available.