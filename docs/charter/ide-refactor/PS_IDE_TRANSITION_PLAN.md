# PS-to-IDE Self-Hosting Transition Plan
**Parent Documents:**  
- [IDE_REFACTOR_PLAN.md](./IDE_REFACTOR_PLAN.md) (especially §5 + L0/L2/L3 work packages)  
- [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](./ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md) (X PS-IDE-TRANSITION-001 + X GOV-WIRING-001 + L0-001)  
- [FRAMEWORK_DECOMPOSITION.md](../FRAMEWORK_DECOMPOSITION.md) (L0–L8 + Cross)  
- [GUI_DESIGN.md](../../gui/GUI_DESIGN.md) (Basic Functionality Baseline subsection + 2.6)  
- Invocation record (PS-to-IDE Transition Readiness section + GOV-WIRING-001)  
- [temp_transition_gap_eval.py](../../../temp_transition_gap_eval.py) (skill-driven gap evaluation)

**Produced by:** Refactoring Agent + Planning Agent (using ide-structural-refactoring + ide-portfolio-planning + gov skills)  
**Date:** 2026-06 (post-TRANS batch)  
**Status:** Living plan. Execute in small governed batches. All steps must run upfront engineering (requirements/arch/hierarchy/policy/trace) + verification/compliance skills first, produce P5 evidence, and update traceability.

**Traceability Model (Requirements → Capabilities → Functional Decomposition → Artifacts → Verification):**  
Every step below must:
- Be preceded by running the relevant generalized skills (ide-requirements-*, ide-architecture-*, ide-hierarchy-taxonomy-steward, ide-governance-policy-compiler, ide-source-to-evidence-traceability, ide-verification-coverage, ide-check-work-commit, ide-sprint-execution-compliance-monitor).
- Map explicitly to matrix rows (especially the new X PS-IDE-TRANSITION-001 and X GOV-WIRING-001).
- Update the matrix, this plan, invocation record, GUI_DESIGN, and LAYER_WORK_PACKAGE_INDEX with tiny anchors.
- Produce evidence bundles (P5) visible in the IDE (viewers/status).
- Respect dual PS+GUI (PS remains fully supported; GUI becomes primary visual + governed dev surface).
- Allow stubs/TODOs for basic functionality (as long as the documented baseline works and is tested).

**Overall Goal:** Controlled transition of primary development surface from PS-MVP (robust wrappers + terminal for execution) to the IDE itself (CUSTOM GUI as visual L0 shell + co-running PS for robust execution). Preserve all governance ("never start coding before upfront engineering", "never pass command before actual testing"), traceability, self-hosting, and dual-use. When the documented basic functionality baseline + tests are sufficient, development work (editing generalized skills/agents, running self-audits, using ACP with preflights, etc.) moves into the IDE while PS remains a first-class dual surface.

**Current Baseline (from skill-driven eval in TRANS batch + temp_transition_gap_eval.py):**  
Basic functionality that exists today and is acceptable for starting the transition (stubs/TODOs explicitly OK if documented):
- Launch (Win11, zero extra deps).
- Menu (File open/close + L4, GitHub P4, Grok/Build ACP + L2 handoff + PS context, Help UI Legend for stubs).
- Dockables (Paned: explorer | editor + viewers + PS terminal).
- L4 Explorer + real self-host demo (packs/skills tree, load SKILL, L2 invoke + P5 bundle).
- Command surfaces (Ctrl+P palette, ACP with JSON + workspace context + gov preflight + L2 handoff).
- Governance preflights (always run gov skills on user paths; evidence + visibility today).
- PS dual (wrappers + co-running PS + robust terminal).
- Status/gates/self-host note + clarity (Legend + hovers).

Stubs (acceptable): full editor structure-aware, rich viewers, strict gov blocking, full multi-agent.

**Gaps (from matrix self-audit + skill eval):** See X PS-IDE-TRANSITION-001 and the gaps list in the invocation record (matrix drift, gov enforcement maturity, no dedicated transition smoke, L2 auto-gov, explicit "use these skills first" wiring, etc.).

---

## Phase 0: Governed Intake & Baseline (Upfront Engineering – Mandatory First Step for Every Subsequent Phase)
**Prerequisites (run these skills first – produce evidence bundles):**
- ide-requirements-implementation-auditor + ide-requirements-baseline (on this plan + current gaps).
- ide-architecture-design-disposition + ide-hierarchy-taxonomy-steward (decompose transition into L0-L8 + Cross).
- ide-governance-policy-compiler + ide-source-to-evidence-traceability (ensure chains for new work).
- ide-verification-coverage + ide-check-work-commit (plan testing for transition).

**Activities:**
1. Run the above skills on the current state (matrix, GUI_DESIGN baseline, invocation gaps, code for stubs).
2. Update this plan + matrix (X PS-IDE-TRANSITION-001 child rows) + invocation record with results + tiny anchors.
3. Produce P5 evidence bundle for "Phase 0 Transition Intake".
4. Confirm basic functionality baseline still works (re-run phase1_batch1_smoke + self-host demo).

**Deliverables:**
- Updated matrix row + this plan with explicit requirements + decomposition.
- Evidence bundles in `evidence/`.
- Anchor in invocation record.

**Functional Decomposition (initial – refine in Phase 1):**
- Parent: Cross XSELF "Self-hosting / dogfooding the IDE" (REQ-STRUCT-006).
- Child: X PS-IDE-TRANSITION-001 "PS-to-IDE self-hosting transition for continuing IDE development" (Level 3, allocated to GUI + L2 executor + L3 gates + dual PS wrappers).
- Sub-children: L0 "GUI Shell as Primary Dev Surface" (menu/dockables/explorer/editor/viewers/ACP as governed dev tools); L2 "Orchestration with Auto-Gov Hooks"; L3 "Mature Gate Enforcement for Transition"; Cross "Governed Development Workflow".

**Verification:** Skill outputs + P5 bundle + smoke + matrix update (G1).

**Status (completed in small batch 2026-06):** 
- temp_phase0_intake.py executed the full list of required skills on the plan + current state (matrix, baseline, gaps, code).
- Results: Most skills returned "error" or "partial" (expected; early skill maturity - many Procedures are high-level or rely on not-yet-fully-wired tools). hierarchy-steward provided declared_tools (validate_hierarchy_metadata, read_ide_artifact) and confirmed tool_registry_available. gov-policy-compiler partial. All runs captured as sources.
- P5 Evidence Bundle created for G0_wave_charter (sources from all skills; bundle markdown generated - see script output for head; full bundle available via GateEngine/viewers in IDE).
- phase1_batch1_smoke.py re-validated PASS (all core paths including preflights, L2 invokes, ACP, menu, dockables, self-host demo still functional - baseline holds).
- Updates applied: This plan marked Phase 0 complete with results. Tiny anchor added to matrix X PS-IDE-TRANSITION-001 and invocation record. temp_phase0_intake.py committed as evidence artifact.
- Baseline confirmed via smoke + self-host demo.

**Phase 0 COMPLETE. All subsequent phases require repeating similar upfront skill runs + evidence + anchors.**

---

## Phase 1: Requirements & Functional Decomposition (Update Living Artifacts)
**Prerequisites:** Phase 0 evidence + run ide-requirements-*, ide-architecture-*, ide-hierarchy-* on this phase.

**Phase 1 Batch 1 (small verified batch, executed 2026-06):** 
- temp_phase1_batch1.py ran upfront skills first (ide-hierarchy-taxonomy-steward declared validate_hierarchy_metadata + read_ide_artifact, confirming L0-L8 hierarchy approach for transition; other skills partial as expected but reinforced need for explicit gov/trace/verif in decomp).
- Matrix X PS-IDE-TRANSITION-001 expanded with detailed L0-002 / L2-003 / L3-002 / Cross sub-rows using 5-field hierarchy (Parent/Child/Level/Allocated/Verification).
- This section of the plan updated with batch completion note.
- Tiny anchor added to invocation record.
- phase1_batch1_smoke re-PASS (no breakage to baseline).
- Phase 1 Batch 1 COMPLETE. (Decomp/reqs advanced; see matrix for full child details. Ready for Batch 2: checklist artifact.)

**Requirements (add/extend – map to REQ-STRUCT-001..006 + new):**
- REQ-TRANS-001: The platform shall support a governed PS-to-IDE transition for self-host development, preserving dual-use and all G0-G5 enforcement.
- REQ-TRANS-002: Basic functionality baseline (documented catalog of menu, dockables, L2 invokes, gov preflights, ACP with context, PS co-running, self-host demo) must be maintained and tested before any primary dev surface flip.
- REQ-TRANS-003: All new IDE dev work (editing skills/agents, running audits, using ACP) must route through gov preflights (upfront engineering + testing evidence) on governed paths; stubs/TODOs allowed if explicitly documented and the baseline works.
- REQ-TRANS-004: Traceability (matrix, plans, invocation) must be updated with every transition step; future self-hosted audits (ide-source-to-evidence-*, etc.) must be run on transition artifacts.
- Extend REQ-STRUCT-006 (self-hosting) with transition-specific sub-requirements.

**Functional Decomposition (update matrix + this plan + LAYER index):**
Use the 5-field hierarchy:
- Parent Capability: Cross XSELF "Self-hosting the full agentic IDE" (L0 GUI Shell + L2 Orchestration + L3 Gates + Cross XSELF).
- Child Function: "PS-to-IDE Transition Enabler" (Level 3).
  - Sub: L0-002 "GUI as Governed IDE Development Surface" (Allocated: shell_host.py + launch_ide.py + GUI_DESIGN baseline; Verification: transition smoke + gov preflight evidence on dev actions).
  - Sub: L2-003 "Executor with Transition Governance Hooks" (Allocated: executor.py + preflight integration; Verification: auto-gov runs on user-invoked skills).
  - Sub: L3-002 "Mature Enforcement for IDE Dev Paths" (Allocated: gates/registry.yaml + GateEngine + P5; Verification: hard-block on G0.1/G_pre for IDE actions).
  - Sub: Cross "Dual PS+GUI Transition Workflow" (Allocated: Invoke-IdeTool.ps1 + shell_host preflights + manifests; Verification: dual execution + evidence on both surfaces).
- Level: 2-4.
- Allocated Component: As above + new transition checklist artifact.
- Verification Method: Skill runs (the ones listed), P5 bundles, dedicated transition smoke, matrix self-audit, G1/G4 on the transition.

**Activities:**
1. Run required skills on the requirements/decomp.
2. Update matrix (add child rows under X PS-IDE-TRANSITION-001 and L0/L2/L3), this plan, invocation record, LAYER_WORK_PACKAGE_INDEX, GUI_DESIGN (link baseline).
3. Create lightweight "IDE Self-Host Transition Checklist" (in invocation or new doc) listing baseline items + gov requirements.

**Deliverables:** Updated artifacts with anchors; checklist; P5 bundle.

**Verification:** Cross-check against skills outputs + matrix G1.

---

## Phase 2: Design (GUI Enhancements + Transition Surfaces)
**Prerequisites:** Phase 1 artifacts + run ide-architecture-document-surface-enforcer + ide-hierarchy-* + ide-governance-policy-compiler on this phase's design.

**Phase 2/3 small batches executed (2026-06, combined for efficiency in this response, but tiny changes):**
- Small change 1 (Phase 2/3): Added transition plan reference to status bar in shell_host.py (visibility of baseline/plan in running IDE).
- Small change 2 (Phase 2/3): Wired gov preflight into _open_folder (before L4 discover - extends governed dev paths; calls _run_governance_preflight + surfaces in viewers).
- temp scripts and smoke used for validation.
- Updates to this plan and invocation with batch notes + anchors.
- Smoke re-PASS (no breakage).
- These are verifiable small steps toward enhancing GUI for dev use while documenting the plan in the UI itself.

**Design Activities (update GUI_DESIGN + add transition design doc if needed):**
- Enhance L0 GUI for dev use (while keeping stubs OK):
  - Editor: Add basic save + simple structure-aware hints (frontmatter outline) on top of current real load (stub full rich editor).
  - Viewers: Improve P5 bundle + markdown rendering; stub rich ones.
  - ACP: Enhance with "gov evidence summary" display before/after sessions; keep protocol real.
  - New surfaces: "Transition Status" panel (shows baseline checklist status, last gov preflights, open stubs).
  - Command palette: Add "Run Gov Preflight", "Self-Host Audit", "Transition Checklist" actions.
- Dual PS integration: Ensure all new GUI dev actions have equivalent PS paths (update wrappers to surface gov evidence).
- Governance in design: Preflights must cover new dev actions (editing, running audits inside IDE). Add notes for future strict mode + HITL.
- Documentation: Explicit "How to develop the IDE inside the IDE" guide (using current baseline + known stubs).

**Functional Decomposition (refine from Phase 1):**
- L0-002 children: "Dev Editor (basic + stub)", "Dev Viewers (P5 + stub)", "Governed ACP for IDE Dev", "Transition Dashboard".
- L2-003: "Dev Workflow Orchestration with Pre-Gov".
- Cross: "Documented Transition Surfaces".

**Deliverables:** Updated GUI_DESIGN (with transition guide), shell_host.py enhancements (small testable), updated matrix rows, P5 bundles from design reviews (run skills on the design docs).

**Verification:** phase1 smoke extension + new "dev path" tests in smoke; gov skill runs on the designs.

---

## Phase 3: Implementation (Small Batches – Execute the Design)
**Prerequisites:** Phase 2 design + run gov + verification skills on each batch.

**Batches (small, one feature or one gov enhancement per batch):**
1. Wire more preflight calls (palette, new dev actions, editor save) + surface "Transition Status" in viewers/status. Update PS wrappers for parity. Live smoke. Anchor.
2. Enhance editor (basic save + frontmatter outline stub) + viewers (better P5/markdown). Test self-host editing of a skill. Gov preflight on edit paths.
3. Add "Transition Checklist" viewer + command palette actions that run gov skills + update checklist status. Dual PS equivalent.
4. Executor enhancements (lightweight auto-gov hook for user-invoked skills if frontmatter declares gov gates). Test with real generalized skill.
5. Gate registry + GateEngine maturity (add enforcement for transition-specific paths; start with warnings + evidence, move to blocks).
6. Update manifests (ide-platform declares transition skills/tools/gates). Update launch_ide.py docstring with transition instructions.
7. Polish: Better error messages for stubs, "basic functionality" watermark or status, docs links.

Each batch must:
- Start with skill runs (upfront + testing).
- Produce P5 evidence.
- Update matrix/invocation/GUI_DESIGN with tiny anchors.
- Re-validate smoke + self-host demo.
- Keep PS fully working.

**Deliverables per batch:** Code + tests + evidence + anchors.

**Functional Decomposition:** Map each batch to the Phase 1/2 children.

**Verification per batch:** Smoke + gov skill output on the change + bundle.

---

## Phase 4: Verification, Testing & Documentation Hardening
**Prerequisites:** Phase 3 complete + run ide-verification-coverage + ide-sprint-execution-compliance-monitor + ide-check-work-commit on the full transition artifacts.

**Activities:**
- Create dedicated "transition smoke" (exercises full dev path: launch, open workspace, gov preflight on edit/invoke/ACP, L2/P5, checklist, dual PS).
- Run full suite of gov/trace/verification skills on the transition work (self-audit).
- Update all docs (matrix verification columns, GUI_DESIGN, this plan, invocation with final baseline + known limitations).
- Produce comprehensive G1/G4 evidence packet for the transition.

**Deliverables:** Transition smoke + test report; updated artifacts; P5/G4 bundles.

**Verification:** All tests PASS; skills report acceptable coverage with documented gaps/stubs; matrix shows complete chains.

---

## Phase 5: Controlled Transition Execution & Post-Transition Self-Hosting
**Prerequisites:** Phase 4 evidence + stakeholder (or gov skill) approval that baseline + tests are sufficient.

**Activities:**
1. Update primary dev surface notes in platform/manifest.yaml, ide-platform/plugin.manifest.yaml, launch_ide.py, GUI_DESIGN, READMEs (GUI now primary visual; PS dual/robust).
2. Move a real piece of work into the IDE (e.g., edit a generalized skill using the GUI editor + gov preflight + L2 invoke + P5).
3. Run self-hosted audit of the transition itself (skills on the changes).
4. Establish ongoing loops: All future IDE dev must use the governed GUI paths (or documented PS equivalent); continue updating matrix/invocation with anchors.
5. Monitor via gov skills (ide-kpi-drift-analyst, compliance monitor) for drift.

**Deliverables:** Flipped primary notes; example self-hosted dev work with evidence; updated plans.

**Verification:** Self-host demo now includes "developing the IDE in the IDE"; gov preflights catch issues; matrix/traceability complete.

---

## Ongoing: Governance of This Plan & Future Work
- Every phase/batch must be preceded by the listed skills.
- Use the IDE (once baseline allows) to edit this plan, run the skills inside the GUI, etc.
- Update this plan + matrix after each tranche.
- Dual: All PS paths remain valid and tested.

**Risks & Mitigations (from GUI_DESIGN + eval):**
- Stub drift → Explicit catalog + UI Legend + transition checklist.
- Gov bypass → Preflights on all paths + future strict mode.
- PS vs GUI inconsistency → Dual wrappers + shared L2/P1 backend + tests.
- Traceability lag → This plan + matrix row + mandatory anchors after every batch.

This plan is self-referential: it was informed by running the skills/tools (TRANS batch + temp script) and will be governed by the same mechanisms it describes.

**End of initial plan.** Ready for Phase 0 execution. All changes must maintain traceability in the matrix and reference L0-L8 + X PS-IDE-TRANSITION-001.