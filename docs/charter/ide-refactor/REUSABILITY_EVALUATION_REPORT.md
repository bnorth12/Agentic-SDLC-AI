# Reusability Evaluation Report — Refactoring the Repo into Layered Agentic IDE Framework

**Produced by:** Refactoring Agent executing `ide-structural-refactoring` skill (Phases 0–2 primary for this evaluation)  
**Date:** 2026-06  
**Parent:** [ide-structural-refactoring/SKILL.md](../../../platform/skills/ide-structural-refactoring/SKILL.md) · [IDE_REFACTOR_PLAN.md](../IDE_REFACTOR_PLAN.md) · [FRAMEWORK_DECOMPOSITION.md](../FRAMEWORK_DECOMPOSITION.md)  
**Inputs (as per skill):** Full tree, all `platform/imports/matm/agents/*.agent.md` (24) + skills (26), `platform/imports/farmrtk/skills/` (17), legacy `src/` (agents 12+, graphs, boards, cli, config, gates, metrics, observability, platform scaffold, routing, skills old, state, tools, utils), docs/ (charter + heavy governance/operations/plans/policies/project-plan/reviews/references), gui/, workspace/, plugins/packs/ (incl. new ide-platform), docker/, scripts/, Examples/, pyproject.toml, Makefile, old README/validate_structure/etc., current layered IDE_REFACTOR_PLAN and LAYER_WORK_PACKAGE_INDEX.

**Gates applicable:** G1 (traceability of this evaluation), G2 (layer interface contracts), G4 (review of reusability dispositions), G5 (baseline of generalized inventory).

---

## Phase 0: Baseline & Audit (Executed)

1. **Generalized repo-audit (from repo-audit-farmrtk + process-audit-farmrtk patterns):** 
   - New platform skeleton strong (platform/, agents/platform/ new personas + 2 agents, plugins/packs/ with ide-platform stub, src/platform/ loaders, gui/ stubs, workspace/ templates, layered plan + index). Good README/AGENTS coverage for reboot.
   - Major hygiene issues: Raw imports with product suffixes and hard-coded paths; dominant legacy bulk in src/ + docs/; old sprint boards and duplicated governance (governance/, operations/, plans/, policies/ overlap ~25+ files); packaging/Makefile/scripts still describe pre-reboot LangGraph/Docker/Ollama world; on-disk egg-info/pycache (gitignored but present); validate_structure.py and NEXT_STEPS/IMPLEMENTATION_SUMMARY/PHASE_0_COMPLETE are orphaned Phase 0 artifacts.
   - Manifests and gate registry present and partially IDE-aware but missing editor/viewer/skill-pub gates.

2. **Source-to-evidence traceability audit (focused on reboot artifacts):**
   - Strong for new items: The 2 new agents + 2 skills have explicit composition links to specific imported .agent.md/SKILL.md + charter + layered plan. PLATFORM_AGENTS.md, IMPORT_MANIFEST, ide-platform manifest updated. Layered IDE_REFACTOR_PLAN has explicit mappings.
   - Weak/missing for: Most raw imports (no IDE surface awareness yet); legacy src/ (no linkage to L0-L8 reboot); heavy historical docs (orphaned from current vision); old src/skills contracts and supervisor (weak or no architecture/design disposition for the layer model).
   - New .agent.md/SKILL.md/gates/schemas have good but incomplete hierarchy metadata (need more for editor contracts etc.).

3. **Artifact-lineage audit:**
   - Orphaned: Old sprint execution boards (SPRINT_4/5/6/8 etc.), PHASE_*_COMPLETE, IMPLEMENTATION_SUMMARY, many reviews/references, old Examples/governance samples, Streamlit dashboard, Ubuntu bootstrap scripts.
   - Generated vs source drift: Evidence packets and logs reference pre-reboot flows; new plan/index are well linked but not yet "baselined" via G5.
   - Positive: .gitignore handles pyc/egg; new platform/ and agents/platform/ have clean lineage to imports.

4. **Governance-policy-compiler (generalized) on current state:**
   - Gate registry (L3) is a solid starting point with maturity modes — reusable core.
   - Policy profiles need extension for IDE surfaces (strict for platform/L2-L4 core, advisory for example packs/L7).
   - Hierarchy conformance good in some MATM imports but not yet applied to new IDE concepts (editors, viewers, skill execution modes).

**Severity-ranked findings (Phase 0 output):**
- High: Generalization debt (all 24+17 assets still raw/product-specific; no IDE surfaces declared). Legacy mixing (src/ bulk pollutes clean layer boundaries). Doc bloat (historical governance/plans dominate tree, low reusability for new vision).
- Medium: Packaging/bootstrap misalignment (cross-layer reorg needed). Limited execution path for new SKILL.md/.agent.md (L2/L4).
- Low: New skeleton (platform/ + layered plan) is highly reusable/evolvable. Some legacy tools (hitl, governance_validation, file ops, state) have selective high value.

Recommended refactor work packages (fed into layered plan): Prioritize XGEN (generalize via Phase 1), XLEG (legacy decision), XDOC (archive), L2/L3/L4 foundations, with architecture disposition (Phase 3) on all structural slices.

---

## Phase 1: Generalize Imported Agents & Skills — Reusability Evaluation

For every imported item (following exact skill steps: strip suffixes, manifest-driven paths, add IDE surface awareness, PowerShell/gh examples, update registries, map "used by" + gates):

**MATM Agents (24) — Reusability: Very High (core to L2/L3/L4/L5 + Cross/XGEN)**
- multi-sprint-portfolio-planner, sprint-intake-gatekeeper, sprint-execution-compliance-monitor, sprint-closeout-certifier, remediation-readiness-strategist, kpi-drift-analyst: Extremely reusable for L2 (orchestration/planning paths in router) + L5 (workspace/portfolio) + Cross (XGEN sequencing, metrics for debt reduction). Already synthesized into Planning Agent + ide-portfolio-planning.
- repo-governance-autoflow-orchestrator, requirements-baseline-steward, traceability-blocker-planner, source-to-evidence-traceability-auditor, artifact-lineage-auditor, governance-policy-compiler, hierarchy-conformance-auditor, hierarchy-taxonomy-steward: Very high for L3 (gate engine, policy, HITL) + L4 (loading/registration of generalized units) + Cross (audit, policy, generalization procedure itself). Core of Refactoring Agent + ide-structural-refactoring.
- architecture-design-change-author, architecture-design-disposition-planner, architecture-design-traceability-auditor, implementation-architecture-alignment-auditor, architecture-contract-enforcer, architecture-document-surface-enforcer: High for L3 (architecture gates) + L4 (contracts for editors/viewers/skills) + Phase 3 disposition on all refactor work. Map to new "editor contract" / "skill pub" gates.
- independent-review-orchestrator, independent-review-history-rollup-orchestrator, requirements-implementation-auditor, verification-coverage-planner: High for L3 (EIRC/G4) + L4 (review workflows) + L7 (as example assured flows in packs).
- Others (e.g. multi-sprint-portfolio-planner already used): All can be generalized to platform or ide-platform pack (L2/L3/L4). Product assumptions (threat-specific) → treat as L7 pack examples or drop/wrap.

**MATM Skills (26) — Reusability: Very High (parallel to agents above)**
- Same families as agents. Generalize names (drop MATM specifics), add IDE surface language ("this skill also supports refactoring editors, viewers, agent definitions, skill contracts"), PowerShell/gh where GitHub-native, map to gates (G0/G1/G4/G5). High fit for L2 (procedural execution), L3 (enforcement), L4 (discoverable units), Cross (the generalization procedure itself is self-referential).

**FarmRTK Platform Skills (17) — Reusability: High (L2/L3/L4/L5 + Cross + L7 examples)**
- orchestrate-farmrtk, independent-review-farmrtk, check-work-commit-farmrtk, traceability-audit-farmrtk, program-metrics-farmrtk, requirements-management-farmrtk, test-authoring-farmrtk, validation-plan-farmrtk, risk-register-farmrtk, process-audit-farmrtk, repo-audit-farmrtk, technical-writer-farmrtk, decision-record-farmrtk, configuration-baseline-farmrtk, icd-maintenance-farmrtk, data-storage-farmrtk, bom-procurement-farmrtk:
  - Core planning/audit/orchestrate ones (orchestrate, independent-review, check-work, traceability, program-metrics, requirements-management, process-audit, repo-audit, technical-writer): Very high reuse for L2 (procedural planning in router), L3 (gates), L4 (loading), L5 (manifest-driven), Cross (XGEN, XDOC, XSELF). Already partially in Planning/Refactoring Agents + ide-* skills.
  - SE-specific (configuration-baseline, icd-maintenance, decision-record, validation-plan, test-authoring, risk-register, data-storage, bom-procurement): High as L7 pack content (engineering-sdlc examples of "assured development" flows inside the IDE) + selective L3/L4 (baselines, ICDs as viewer contracts).
- Generalization steps (per skill): Replace .farmrtk/ / Tools/ / SYS-DOC-10 / specific PS1s with workspace.repos + packs entry + gate.registry + runtime.shell (powershell) + viewer.*. Add explicit "supports IDE editor/viewer/skill surfaces". Update PLATFORM_AGENTS and ide-platform manifest.

**FarmRTK Domain Skills (5 in engineering-sdlc/imports) — Reusability: Low for platform layers, High for L7**
- OpenSCAD-Parametric-FarmRTK, firmware-build-farmrtk, integration-bench-farmrtk, electronics-wiring-farmrtk, rf-antenna-farmrtk: Treat as examples of domain packs (L7). Generalize non-product parts (e.g. firmware-build toolchain integration) but keep product flavor inside the pack. Not core to L0-L6.

**Overall Phase 1 Verdict:** ~80-90% of imported governance/process assets have high reusability for L2 (orchestration/planning), L3 (gates/HITL/audit), L4 (plugin/skill/agent host + elevation), L5 (workspace context), and Cross (XGEN, policy, lineage, self-hosting). They are the "seed" for making the IDE "assured" rather than vibe. Low for pure domain (L7 only). All must go through full generalization (strip, manifest-driven, IDE surfaces added, PowerShell/gh, registry updates, gate mapping) before promotion out of imports/. New agents/skills we added are the first successful examples.

---

## Phase 2: Structural Repo Reorganization — Reusability Fit to Layers

Apply severable decomposition (per skill + FRAMEWORK_DECOMPOSITION):

**High reusability / Evolve in place (core to layers):**
- platform/ (manifest, gates, schemas, imports staging → generalized skills, new ide-refactor/ reports): L3 (gates), L4 (host), L5 (schemas), Cross (staging for XGEN).
- plugins/packs/ (engineering-sdlc, threat-modeling, github-devops, new ide-platform): L7 primary. ide-platform for L2/L3/L4 process skills/agents.
- agents/platform/ (PLATFORM_AGENTS + 2 new agents): L2/L3 (process/governance personas).
- src/platform/ (gates/engine, orchestration/router, plugins/loader, providers, workspace/loader, gui/shell_host): High — evolve as the runtime for L2, L3, L4, L5, L6. The "new" part of legacy src/.
- gui/ (installer PS1, shell/zed, viewers/): L0 (shell + viewers). Expand here.
- workspace/ (templates, future settings schema): L5.
- The layered IDE_REFACTOR_PLAN + LAYER_WORK_PACKAGE_INDEX + this report + ide-platform manifest: Cross (living planning artifacts) + L4 (as loadable "plans" via skills).

**Medium/Selective reusability (port or bridge):**
- Legacy src/ non-platform: 
  - agents/ (12+ chief_*, program_manager, requirements_agent, architecture_agent, software_*, etc.), boards/, graphs/supervisor.py: Low for direct L2/L3 (old monolithic LangGraph org). Decision: Move bulk to legacy/src/. Selective port of patterns (supervisor routing ideas → L2 adapter; review board concepts → L3 gates or L4 workflows). Old BaseAgent + prompts/config may inform new ACP interaction (L1).
  - skills/ (old contracts.py, registry, requirements_quality, traceability_synthesis): Medium — bridge old Pydantic contracts to new skill contract schema (L4). The new SKILL.md style supersedes for IDE.
  - state/ (persistence, schema): Medium-high for L2 (stateful) or L5 (workspace context).
  - tools/ (file_operations, code_analysis, governance_validation, memory_tools): High selective — port governance_validation + file ops to L2/L3/L4 tools; code_analysis as L7 example or L0 LSP complement.
  - utils/ (hitl.py, logging, tracing): High — hitl core for L1/L3; logging/tracing for cross + L2.
  - cli/, config/, metrics/, routing/, observability/ (Streamlit): Low (cli/config/routing/metrics patterns may inform L2 router or L4; Streamlit → L0 legacy viewer or archive).
- src/ overall: The platform/ subdir is the reusable bridge; rest is legacy decision (Phase 2 of skill recommends legacy/src/ + selective port + update all references/tests/docs).

**Low reusability (archive or L7/L8 examples only):**
- docs/governance/ (25+ files incl. PHASE_1_COMPLETE, detailed gates, RACI, etc.), operations/, plans/ (many old SPRINT_* boards, SPRINT_0/1/4/5/6/8), policies/, project-plan/ (old execution boards, SKILLS_BACKLOG etc.), reviews/ (INDEPENDENT_REVIEW_1, SPRINT_4_*), references/ (AEROSPACE etc.): Mostly low for new IDE vision. Archive to docs/archive/ (cross-layer XDOC). Selective reuse of policies as L7 examples or living "how we govern the IDE".
- Other docs (old agent-roles, architecture, development-guide, getting-started, roadmap, testing-strategy, PRODUCT_REQUIREMENTS, hardware): Selective generalize for living docs (L0/cross): "how to add editor/skill/agent/pack", updated getting-started (PowerShell + Zed first), architecture aligned to layers.
- charter/ (REBOOT, REFACTOR_TODO, FRAMEWORK_DECOMPOSITION, IDE_REFACTOR_PLAN, new ide-refactor/): High — evolve in place (cross + L4 as "plan artifacts").
- docker/, scripts/ (bootstrap_ubuntu.sh, health_check, pull_models, setup_db, validate_governance_evidence), Examples/ (incl. governance/), validate_structure.py, NEXT_STEPS.md, IMPLEMENTATION_SUMMARY.md, PHASE_0_COMPLETE.md, old requirements.txt, pyproject (old src focus), Makefile (old targets): Low for platform layers. Cross-layer reorg: Make Docker/legacy optional; evolve Makefile for layer smoke tests + "plan" / "refactor" invocations (using new skills); archive old examples/summaries or move to L7/L8; update packaging to support new layers + platform/skills discovery.
- gui/installer and shell (current): Evolve (L0); not discard.

**Phase 2 Verdict & Disposition (Phase 3 start):** 
- The "everything" breaks cleanly: ~60-70% of value (governance/process from imports + selective legacy utils + new skeleton) is highly reusable when generalized and mapped to L2/L3/L4/L5 + Cross. Pure legacy monolith and historical docs are low-reusability for the layer framework → legacy/ tree + archive/.
- Architecture/design disposition for this evaluation: Update architecture view (L2/L3/L4 core platform runtime + L7 packs) to match implementation (current mixed tree). Record in ADR (see Phase 4). Keep new platform/ evolving in place; do not mix legacy into it.
- Hierarchy metadata applied: Every major reorg item (e.g. legacy move, doc archive, import generalization tranche) requires parent capability (e.g. "L2 Orchestration"), child function (e.g. "procedural skill executor"), etc.

This evaluation feeds directly into the layered IDE_REFACTOR_PLAN and the project plan below. All high-reusability items are already partially mapped in the LAYER_WORK_PACKAGE_INDEX (XGEN work packages).

---

## Phase 3–5 Notes (for Ongoing Execution)
- Phase 3: All structural decisions in this report (and the project plan waves) require explicit disposition + hierarchy + sync with implementation (e.g. update src/platform/ code, manifests, tests, the SKILL.md itself).
- Phase 4: Add IDE gates (editor, skill-pub) to registry; expand github-devops for layer PR enforcement; produce ADRs for legacy decision and generalization strategy; baseline via G5.
- Phase 5: Re-audit after each wave; EIRC/G4 on major generalization tranches; self-update this report and the refactoring skill.

**PowerShell/GitHub emphasis (examples from skill):** Use for generalize-imports.ps1, gh issue creation for XGEN items, Actions calling the refactoring skill or agent via ACP.

**Escalation:** Large legacy surface → Planning Agent for sequencing. New surfaces needed → feed Planning Agent.

This report is self-referential (the skill updated itself conceptually) and will be generalized further in future waves.

**Next:** This evaluation directly informs the full project plan (waves limited-detail) and detailed first wave below. All recommended work packages align to the existing LAYER_WORK_PACKAGE_INDEX and IDE_REFACTOR_PLAN.