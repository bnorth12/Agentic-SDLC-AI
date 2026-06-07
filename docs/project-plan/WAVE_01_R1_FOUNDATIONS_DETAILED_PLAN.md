# Detailed Plan — Wave 01: Foundations & First Generalization (R1)

**Wave ID:** WAVE-01-R1  
**Parent:** [AGENTIC_IDE_PROJECT_PLAN.md](./AGENTIC_IDE_PROJECT_PLAN.md) (high-level limited details) · [IDE_REFACTOR_PLAN.md](../charter/IDE_REFACTOR_PLAN.md) (layered) · [REUSABILITY_EVALUATION_REPORT.md](../charter/ide-refactor/REUSABILITY_EVALUATION_REPORT.md) · [LAYER_WORK_PACKAGE_INDEX.md](../charter/ide-refactor/LAYER_WORK_PACKAGE_INDEX.md)  
**Produced by:** Planning Agent (sequencing/intake via ide-portfolio-planning) + Refactoring Agent (structural/generalization via ide-structural-refactoring, following its full 5-phase procedure).  
**Status:** Ready for G0 charter + execution.  
**Traceability:** All tasks link to WP- IDs, layers, specific imported assets from reusability eval, gates, owners, cross-deps, and evidence requirements. Self-referential: Wave execution will use (and improve) the agents/skills being generalized.

**Reusability Foundation (from evaluation report Phase 0-1) + Current XGEN Progress:** Prioritize high-reusability items for XGEN1 in Requirements → Architecture/Design → Compliance → Verification order (per direction for max bang-for-buck before lower implementation layers). Generalized so far into ide-platform pack: requirements-baseline-steward, architecture-design-disposition-planner, governance-policy-compiler, verification-coverage-planner, source-to-evidence-traceability-auditor, independent-review-orchestrator, architecture-design-change-author, ide-architecture-design-traceability-auditor, ide-implementation-architecture-alignment-auditor, ide-kpi-drift-analyst, ide-architecture-document-surface-enforcer, ide-artifact-lineage-auditor, ide-hierarchy-conformance-auditor, ide-sprint-closeout-certifier, ide-remediation-readiness-strategist, ide-sprint-execution-compliance-monitor, ide-sprint-intake-gatekeeper, ide-traceability-blocker-planner, ide-multi-sprint-portfolio-planner, ide-architecture-contract-enforcer, ide-process-audit, ide-repo-audit, ide-traceability-audit. Self-hosted governance artifacts produced for repo structure (baseline + disposition + execution plan + verification coverage + compliance audit + process audit). These map to L2/L3/L4/Cross. Legacy decision (Phase 2) here. Low-reusability historical docs/legacy bulk → archive/legacy/. We remain fully open to circling back and refactoring as better architecture/designs emerge during execution. Functional decomp (hierarchy) is explicitly used in all artifacts. The structural refactor execution plan (governed by the new agents) is the direct output of using the prioritized procedures to plan the repo to the full IDE. New contract, process, repo, and traceability audits just added for deeper compliance during generalization and structure work. A process audit of the execution plan was produced using ide-process-audit.

**Wave Goal (from high-level plan):** Establish executable hybrid foundation (L2/L3), initial skill/agent loading (L4), starter surfaces (L0), first reusable imported assets generalized, doc/legacy hygiene started, packaging aligned. Enable first self-hosting smoke. All changes respect layers and pass gates with evidence.

**Scope Boundaries (per reusability eval + layered plan):** 
- In: L2/L3 foundations + first XGEN batch (planning/gov/audit core) + L4 loader basics + L0 starter editors/viewers + Cross XDOC first tranche + XLEG decision + XPACK alignment.
- Out: Bulk XGEN (later waves), full L0/L1 surfaces, L5/L6/L7 maturation, rich self-hosting (Wave 2+).
- Constraints: PowerShell primary for Windows examples/automation; all generalized artifacts get IDE surface awareness + gh where applicable; architecture/design disposition (Phase 3 of skill) on every structural slice with hierarchy metadata; no mixing of low-reusability legacy into new platform/ layers.

**Primary Layers + Cross-Cuts:** L2 + L3 (foundations), L4 (basics), L0 (starter), Cross (XGEN1, XDOC start, XLEG decision, XPACK).
**Owners:** Planning Agent (overall sequencing, G0 intake, portfolio balance, wave evidence prep). Refactoring Agent (Phase 0-5 execution on structural/XGEN items, disposition, evidence). Composed: Use generalized sprint-*/kpi/repo-gov items for planning/audit sub-tasks; architecture-design-* for dispositions.
**Gates for this Wave:** G0 (charter + intake verdict), G1 (traceability of all generalized items + this detailed plan back to reusability report + imports + layers), G4 (EIRC/independent review on XGEN tranche + structural decisions + legacy disposition), G5 (baseline of post-wave state for foundations).
**Dependencies (from matrix):** Reusability evaluation complete (this report). New Planning/Refactoring agents + ide-* skills already added and registered. Current layered plan + index as inputs. Cross-layer: XGEN1 depends on Phase 1 generalization procedure; XLEG on Phase 2 reorg.
**Risks (from skill escalation + high-level plan):** Legacy surface too large (mitigate with explicit decision + Planning Agent sequencing); no real executor yet (mitigate by building procedural runner in E1.1 as first deliverable); over-generalizing in one wave (scope XGEN1 to 7-8 high-reusability items only).
**Success Criteria (measurable, per high-level + skill Phase 5):**
- Router (L2) can invoke at least the 2 new ide-* skills + 2-3 generalized imports as procedural steps; returns evidence.
- Gate engine (L3) extended with 1-2 IDE gates; policy profiles applied.
- Loader (L4) discovers from platform/skills/ + ide-platform; basic viewer reg.
- Starter editors/viewers (L0) usable in Zed for .agent.md/SKILL.md + 1 gate evidence type.
- 6-8 high-reusability imports generalized (names stripped, manifest-driven, IDE surfaces added, PowerShell/gh examples, registered, mapped to gates) per Phase 1. (Prioritized per Requirements → Arch/Design → Compliance/Verification order.)
- Legacy `src/` decision recorded + initial bulk move executed (Phase 2); first doc archive tranche complete (XDOC).
- Packaging updated; platform smoke tests pass for new layers.
- All artifacts have source-to-evidence linkage + hierarchy metadata where structural (Phase 3); evidence bundle for G4/G5.
- Wave passes G0/G1/G4; self-hosting smoke (use Planning Agent + one generalized skill to plan a 1-2 task slice of Wave 2).
- Re-audit (Phase 5) shows critical findings closed or accepted.

---

## Detailed Epics & Tasks

Each epic expands a limited epic from the high-level plan. Tasks follow refactoring skill phases where applicable (especially for XGEN/Cross). Include owners, estimated effort (conceptual), deps, gates, reusability notes, verification, PowerShell/gh examples, and evidence.

### E1.1 L2/L3: Procedural Skill Executor + Basic Hybrid Router Foundations
**Layers:** L2 (primary), L3 (integration).  
**WP References:** WP-L2-001, WP-L2-003, WP-L3-010 (partial).  
**Goal:** First working procedural executor that can run SKILL.md steps (new ide-* + early generalized). Basic router integration. Evidence return.  
**Tasks (follow skill where structural):**
1. (Refactoring Agent, Phase 2/3) Design & implement minimal procedural executor in src/platform/orchestration/ (parse frontmatter, execute PowerShell/bash steps or Python fragments, capture outputs as evidence). Disposition: Update L2 architecture view. Hierarchy: parent=L2 Orchestration, child=procedural executor.
2. Wire basic router to call executor for skills tagged "procedural" (start with ide-portfolio-planning and ide-structural-refactoring). Add scaffold for ACP handoff.
3. Extend gate engine (src/platform/gates/) to accept evidence from executor; basic viewer hook for evidence bundles (L3).
4. Add unit/smoke tests (style of test_platform_scaffold.py) for executor + router on new skills. (Verification: run pytest on L2 bits.)
5. PowerShell example (per skill): `pwsh -File tools/executor/run-skill.ps1 -Skill ide-portfolio-planning -Workspace workspace/templates/example-farmrtk.workspace.yaml -Output evidence/`.
6. gh integration stub: Script to attach executor output as PR comment (for later L6).

**Owners:** Refactoring Agent (impl + disposition); Planning Agent (defines usage in this wave).  
**Effort:** Medium (core foundation).  
**Deps:** New ide-* skills exist; current router scaffold.  
**Gates:** G1 (traceability of executor code to L2 section of layered plan + reusability eval), G2 (executor interface contract), G4 (review of router changes).  
**Reusability Notes:** Directly enables execution of high-reusability imports (orchestrate-farmrtk patterns, multi-sprint-portfolio-planner, governance-policy-compiler). Port any useful legacy supervisor routing ideas here (selective from src/graphs).
**Verification & Evidence:** Executor successfully runs `ide-structural-refactoring` procedure stub on a sample import; evidence bundle produced and viewable; smoke test passes; decision record for any LangGraph adapter choice.
**Deliverables:** Updated src/platform/orchestration/router.py + new executor module; test; example PS1; evidence packet for G4.

### E1.2 L3: Gate Registry Extensions + Policy for IDE Surfaces
**Layers:** L3 (primary).  
**WP References:** WP-L3-001, WP-L3-002.  
**Goal:** Add first IDE-specific gates (editor contract, skill publication); apply generalized policy compiler.  
**Tasks:**
1. (Refactoring Agent, Phase 1/4) Extend platform/gates/registry.yaml with 1-2 new gates (e.g. G-EDITOR-CONTRACT, G-SKILL-PUB). Map executors to generalized skills/agents (e.g. ide-structural-refactoring for pub). Add viewer.* for evidence.
2. Invoke generalized governance-policy-compiler (from MATM import) against registry + workspace overrides; produce policy status report. Add IDE profiles (strict for L2-L4 core).
3. Update gate engine code to handle new gates + maturity for IDE dev workspaces.
4. Architecture disposition (Phase 3): Record for new gates (hierarchy: parent=L3 Gate Engine, child=IDE surface gates).
5. PowerShell: Script to validate a skill against new G-SKILL-PUB before "publication".

**Owners:** Refactoring Agent (extensions + compiler invocation); Planning Agent (intake of new gates into wave).  
**Effort:** Medium-low.  
**Deps:** E1.1 (evidence from executor).  
**Gates:** G1, G2 (new gate contracts), G4.  
**Reusability Notes:** Directly generalizes governance-policy-compiler + hierarchy-* + independent-review-orchestrator. High from eval.
**Verification:** New gates load; policy report generated; sample skill "passes" G-SKILL-PUB stub; evidence for G4.
**Deliverables:** Updated registry.yaml + engine.py; policy report; PS validation script; ADR for gate extensions.

### E1.3 L4: Skill/Agent Loader Basics + Viewer Registration
**Layers:** L4 (primary).  
**WP References:** WP-L4-001, WP-L4-002.  
**Goal:** Loader discovers from platform/skills/ and ide-platform pack; basic viewer registration contract.
**Tasks:**
1. (Refactoring Agent, Phase 2/4) Extend src/platform/plugins/loader.py (or add parallel skill/agent loader) to scan for SKILL.md + .agent.md (frontmatter parsing, manifest-driven paths).
2. Implement simple viewer registry (yaml or code) consumable by gate engine and shell (L0).
3. Register the 2 new ide-* skills + early generalized ones; update ide-platform manifest.
4. Phase 3 disposition on loader changes.
5. Test: Discovery smoke for current platform/skills/ + agents/platform/.

**Owners:** Refactoring Agent (loader + registration); Planning Agent (portfolio of what gets loaded).  
**Effort:** Medium.  
**Deps:** E1.1/E1.2 (things to load/enforce).  
**Gates:** G1, G2 (loader/viewer contracts), G4.  
**Reusability Notes:** Enables Phase 1 output (generalized imports) to be loaded. Core to L4 per eval.
**Verification:** Loader finds ide-portfolio-planning + 1 generalized import; viewer reg works for markdown; tests pass.
**Deliverables:** Updated loader; viewer registry stub; registration updates; discovery test.

### E1.4 L0: Starter Editors + Viewers in Shell
**Layers:** L0 (primary).  
**WP References:** WP-L0-001, WP-L0-002.  
**Goal:** Usable basic editors for .agent.md/SKILL.md + 1-2 viewers in Zed config + shell.
**Tasks:**
1. Update gui/shell/zed-agent-servers.json + add editor/viewer snippets for agent/skill files (outline + invoke).
2. Basic viewer integration (markdown for plans/evidence; mermaid for any graphs from generalized skills).
3. Wire "run skill" action to call the new executor (E1.1) via ACP or PS.
4. Disposition for new surface contracts (Phase 3, using architecture-design-* patterns from imports).
5. PowerShell: Wrapper to launch Zed with platform workspace + open a sample SKILL.md.

**Owners:** Refactoring Agent (structural surfaces); Planning Agent (sequencing L0 rollout). Composed from technical-writer-farmrtk (docs) + architecture-design-auditors.
**Effort:** Medium (UI stubs).  
**Deps:** E1.1 (executor to invoke), E1.3 (loader for discovery in editor).
**Gates:** G2 (editor/viewer interface contracts), G4.  
**Reusability Notes:** Low direct from imports (new surfaces); some from technical-writer + architecture-document-surface-enforcer for docs/graphs.
**Verification:** Can open/edit a .agent.md in Zed, see outline, "invoke" a skill stub, view markdown evidence.
**Deliverables:** Updated Zed config + snippets; basic viewers; PS launch wrapper; surface contract ADR.

### E1.5 Cross XGEN1: First Batch Generalization of High-Reusability Imports
**Layers:** Cross (XGEN primary), feeding L2/L3/L4.  
**WP References:** WP-XGEN-001 to WP-XGEN-007 (planning/gov/audit core).  
**Goal:** Generalize 6-8 high-reusability items per skill Phase 1; produce usable generalized versions.
**Tasks (strictly follow ide-structural-refactoring Phase 1 for each):**
1. (Refactoring Agent) For selected batch (e.g. multi-sprint-portfolio-planner + orchestrate-farmrtk equivalents, kpi-drift, repo-governance-autoflow, governance-policy-compiler, 2-3 sprint-*, source-to-evidence-auditor):
   - Strip suffixes → IDE or -sdlc ids.
   - Replace hard paths with manifest/gate/viewer equivalents.
   - Add IDE surface language (editors, viewers, agent/skill defs, hybrid exec).
   - Add PowerShell-first + gh examples (e.g. gh issue for generalization tasks).
   - Update PLATFORM_AGENTS.md or ide-platform manifest; map "used by" (Planning/Refactoring Agents, EIRC) + gates.
2. Move stable generalized SKILL.md/.agent.md out of imports/ to platform/skills/ or ide-platform.
3. For each: Architecture/design disposition (Phase 3) with hierarchy metadata.
4. Self-update: Apply lessons to this detailed plan + reusability report.
5. Evidence: Lineage from original import to generalized + test run via new executor.

**Owners:** Refactoring Agent (all Phase 1 execution + disposition); Planning Agent (selects batch + intake).  
**Effort:** High (core of wave per eval).  
**Deps:** E1.1 (to test execution of generalized), E1.3 (to load them).  
**Gates:** G1 (full traceability per item), G4 (on tranche).  
**Reusability Notes:** Directly from eval Phase 1 — these are the "very high" items for L2/L3/L4/Cross. Prioritize planning family first.
**Verification (Phase 5 style):** Generalized items load/run via executor; have IDE surfaces + PowerShell; pass G1/G4 with bundles; re-audit shows progress on generalization %.
**Deliverables:** 6-8 generalized files (with references); updated manifests/registries; dispositions/ADRs; evidence packets; updated this plan/report with lessons.

### E1.6 Cross XDOC + XLEG: Doc Hygiene Start + Legacy Decision
**Layers:** Cross (primary).  
**WP References:** WP-XDOC-001, WP-XLEG-001.  
**Goal:** First archive tranche + explicit legacy `src/` decision + initial move (Phase 2 of skill).
**Tasks:**
1. (Refactoring Agent, Phase 2) Create docs/archive/ (or history/); move first batch of low-reusability (old SPRINT_* boards from project-plan/, PHASE_1_COMPLETE etc. from governance/, duplicated ops/plans/policies files per eval).
2. Produce index for archive + pointers from living docs (charter/ + new project-plan/).
3. Legacy decision (Phase 2/3): ADR recommending legacy/src/ for bulk (agents/ graphs/ boards/ etc.), selective ports (hitl, governance_validation, state, contracts to L4), keep/evolve src/platform/. Execute initial move of 1-2 high-bulk dirs; update references in tests/docs/Makefile.
4. Disposition for reorg decisions with hierarchy (parent=Cross Doc/Legacy Hygiene).
5. Update root README/getting-started to point to new layered plan + living docs.

**Owners:** Refactoring Agent (archive + decision + move); Planning Agent (sequencing in wave).  
**Effort:** Medium-high (hygiene debt).  
**Deps:** Reusability eval (identifies low-reusability items).  
**Gates:** G1 (traceability of moves), G4 (on decisions).  
**Reusability Notes:** Directly addresses low-reusability historical docs + legacy bulk from eval Phase 0/2. High value for clean layers.
**Verification:** Archive present with index; legacy/ tree started; no broken links in active tree for moved items; decision ADR; living docs updated.
**Deliverables:** docs/archive/ + index; legacy/src/ initial; ADR for legacy decision; updated README/docs pointers; evidence for G4.

### E1.7 Cross XPACK: Packaging, Bootstrap & Test Alignment
**Layers:** Cross (primary), enabling all.  
**WP References:** WP-XPACK-001.  
**Goal:** Packaging supports new layers + skill invocation; tests aligned; legacy optional.
**Tasks:**
1. (Refactoring Agent + Planning) Update pyproject.toml (include platform/skills data, new src/platform focus, mark old cli legacy).
2. Evolve Makefile: Targets for "plan" (invoke ide-portfolio-planning), "refactor" (ide-structural-refactoring), layer smoke tests (pytest on src/platform/ + new generalized), archive-docs, clean.
3. Make docker/ + old scripts (health, pull_models) optional/legacy profile.
4. New platform health check + validate script focused on layers + reusability progress.
5. Update validate_structure.py or replace with layer-aware version.

**Owners:** Refactoring Agent (structural packaging changes); Planning Agent (targets for agent invocation).  
**Effort:** Medium.  
**Deps:** E1.1 (invocation targets).  
**Gates:** G1, G4 (on packaging changes affecting all layers).  
**Reusability Notes:** Addresses medium packaging misalignment from eval. Enables future XGEN/XSELF.
**Verification:** `pip install -e .` works for new bits; `make plan` / `make refactor` stubs invoke skills; layer tests pass; old Docker is optional.
**Deliverables:** Updated pyproject/Makefile; optional legacy profile; new health/validate scripts; evidence.

---

## Wave Execution & Closeout (per Skill Phases 4-5)

- **During wave:** Planning Agent maintains intake/sequencing (use ide-portfolio-planning on this detailed plan). Refactoring Agent runs full phases on XGEN/Cross items (baseline re-audits, generalization, disposition, evidence, GitHub stubs via gh).
- **Evidence & GitHub:** All deliverables produce bundles (G1). Use gh (L6 stub) to create issues/PRs with evidence for XGEN items. Actions (future) will call skills/agents.
- **Self-hosting smoke (end of wave):** Invoke Planning Agent (via current generalized skill or manual) to produce a tiny "Wave 2 planning slice" using the new surfaces/executor. Capture as evidence; run through G4 stub.
- **Validation & Closeout (Phase 5):** Re-run Phase 0 audits (repo-audit, source-to-evidence, lineage, policy). All critical findings closed/accepted. EIRC/G4 on wave artifacts + XGEN tranche. Update this detailed plan, the high-level project plan, reusability report, and ide-structural-refactoring skill with lessons. Hand evidence to G5 baseline. Bump versions in manifests. Produce release note for foundations.

**Post-Wave 1:** Updated layered plan + index with progress. Wave 2 charter ready (Planning Agent). Bulk XGEN + L0/L1 elevation next.

**End of detailed first wave plan.** This is executable by the Refactoring Agent following its skill procedure, sequenced by the Planning Agent. All tasks are traceable to layers, reusability eval, WP index, gates, and the high-level project plan.