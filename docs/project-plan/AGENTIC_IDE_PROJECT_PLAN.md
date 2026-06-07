# Agentic IDE Project Plan — Full-Featured Agentic AI IDE Platform

**Document ID:** PROJ-PLAN-IDE-001  
**Version:** 0.1 (post-reboot, layered)  
**Date:** 2026-06  
**Status:** Baseline — produced following execution of `ide-structural-refactoring` skill (reusability evaluation) + Planning Agent sequencing  
**Parents:** [REBOOT_CHARTER.md](../charter/REBOOT_CHARTER.md) · [FRAMEWORK_DECOMPOSITION.md](../charter/FRAMEWORK_DECOMPOSITION.md) · [IDE_REFACTOR_PLAN.md](../charter/IDE_REFACTOR_PLAN.md) (layered details) · [REUSABILITY_EVALUATION_REPORT.md](../charter/ide-refactor/REUSABILITY_EVALUATION_REPORT.md) · [LAYER_WORK_PACKAGE_INDEX.md](../charter/ide-refactor/LAYER_WORK_PACKAGE_INDEX.md)  
**Produced with:** Planning Agent (`ide-portfolio-planning`) for wave/epic structure + Refactoring Agent (`ide-structural-refactoring`) for reusability evaluation and structural recommendations.

**Traceability:** All waves/epics reference layers (L0-L8 + Cross), specific reusability findings from the evaluation report, work package prefixes from the index (WP-Lx-xxx, WP-XGEN-xxx), gates (G0/G1/G2/G4/G5), and owners (primarily the two new agents + composed imported ones). The plan is self-hosting: the IDE's own development uses the Planning/Refactoring Agents and skills being built.

---

## 1. Project Objective & Vision Alignment

Build a **thin, plugin-adaptable, full-featured agentic AI IDE platform** for assured systems/software engineering. 

Key characteristics (from layered IDE_REFACTOR_PLAN):
- Full suites of editors (code, .agent.md, SKILL.md, manifests, evidence, prompts) and viewers (markdown, mermaid, stix, icd-csv, graph-canonical, audit trails, agent/skill graphs).
- User interaction agents + ACP panels + slash commands.
- Skills as first-class (discoverable, editable, invocable procedurally or via Grok Build ACP, with PowerShell baked in).
- Hybrid orchestration (procedural skills / LangGraph / ACP).
- Windows PowerShell + GitHub native (shell default, gh skills, Actions as gate enforcers, PRs as work packages with evidence).
- Domain in severable packs (L7); platform owns process/gates/orchestration/plugin host/workspace (L2-L5 primarily).
- Agents/skills developed inside the IDE (self-hosting, meta).
- Strong governance: gate engine with maturity/HITL modes, evidence lineage, source-to-evidence traceability.

**Dogfooding Principle (updated for layers):** We prove the methodology by applying the Planning Agent, Refactoring Agent, `ide-portfolio-planning`, `ide-structural-refactoring`, and gates to the development of the IDE itself. Layer 1 work (implementing an editor or generalizing an imported skill) is governed by Layer 2 (this project plan, wave intake G0, EIRC G4, evidence).

**Reusability Foundation (from Refactoring Agent evaluation, Phases 0-2):**
- **High reusability (~80-90% of imported value):** MATM 24 agents + 26 skills (governance, audit, traceability, sprint lifecycle, architecture design change, hierarchy, kpi, repo-gov, independent review) + FarmRTK 17 platform skills (orchestrate, independent-review, check-work, traceability, program-metrics, requirements-mgmt, process-audit, repo-audit, technical-writer, decision-record, configuration-baseline, etc.). These map primarily to L2 (orchestration/planning), L3 (gates/HITL/audit/policy), L4 (plugin host + skill/agent elevation + loading), L5 (workspace/manifest-driven), and Cross (XGEN generalization, XDOC hygiene, XSELF self-hosting, policy/audit).
  - Action: All must be generalized (strip suffixes, manifest/gate/viewer-driven, add explicit IDE surface awareness for editors/viewers/agents/skills, PowerShell + gh examples, register in PLATFORM_AGENTS or packs, map to gates).
- **Selective/medium from legacy src/:** hitl.py, governance_validation, file_operations, state ideas, old contracts/registry patterns, supervisor routing concepts, review board logic. Port selectively to L1 (ACP runtime), L2 (orchestration/hitl), L3 (gates), L4 (tools/contracts). Bulk of 12+ agents, graphs/supervisor, boards, cli, old src/skills, observability/Streamlit → legacy/src/ or archive (low direct reusability for clean layers).
- **Low for historical docs bulk:** governance/ (25+), operations/, plans/ (old SPRINT boards), policies/, many project-plan/ entries, reviews/, references/ → archive (Cross XDOC). Selective policies as L7 examples.
- **High for new skeleton:** platform/ (evolve L3/L4/L5), agents/platform/ new (L2/L3), plugins/packs/ + ide-platform (L7 + L2-L4 process), gui/ (L0), workspace/ (L5), src/platform/ scaffold (evolve L2-L6), layered plan/index/evaluation report (Cross + L4 artifacts).
- Domain FarmRTK specifics (OpenSCAD etc.): L7 only (engineering-sdlc pack examples).
- Overall: The copied assets are the "governance seed" that makes the IDE assured. The reusability eval (see full report) directly drives XGEN work packages in every wave.

**Two-Layer Distinction (adapted):** 
- Layer 1 (Product/Implementation): Building the actual IDE surfaces, router, generalized skills/agents, packs (ends up in platform/, plugins/, gui/, src/platform/, agents/platform/).
- Layer 2 (Governance/Project): This plan, wave charters (G0), EIRC reviews (G4), evidence, reusability audits, self-hosting using the agents/skills (lives in docs/project-plan/, charter/ide-refactor/, gate evidence).

---

## 2. Overall Approach & Sequencing Principles

- **Layer-driven (abstraction-based):** All work respects L0-L8 from FRAMEWORK_DECOMPOSITION. Waves scope to 1-2 primary layers + cross-cuts for manageability (per reusability eval recommendation to avoid boiling the ocean).
- **Agent-driven execution:** Planning Agent (`ide-portfolio-planning`) owns wave intake, sequencing, portfolio balance, and limited-detail epics. Refactoring Agent (`ide-structural-refactoring`) owns generalization (Phase 1), structural reorg (Phase 2), architecture/design disposition (Phase 3), evidence/lineage (Phase 4), and validation (Phase 5) within waves.
- **Reusability-first:** Every wave includes XGEN tranches (generalize batches of high-reusability imported assets per the evaluation report). High-reusability items prioritized for early waves (L2/L3/L4/L5/Cross).
- **Gates & Traceability:** Every wave passes G0 (charter by Planning Agent), G1 (traceability to this plan + reusability report + imports + layers), G4 (independent review/EIRC on structural/generalization work), G5 (baseline for major increments). Work packages use traceable IDs from LAYER_WORK_PACKAGE_INDEX.
- **Hybrid + Native:** Procedural skills (new ide-* + generalized) for deterministic steps; ACP for interactive planning/refactoring; GitHub Actions + gh for enforcement/evidence; PowerShell primary on Windows.
- **Self-hosting & Dogfooding:** By Wave 3+, the platform's own increments are executed using the agents/skills/gates/editors being built.
- **Limited details in this plan:** High-level waves + 4-7 epics per wave (layer-mapped, owners, gates, key deps, reusability notes). Full task details in per-wave detailed plans (see first wave below) or the layered IDE_REFACTOR_PLAN + index.
- **Legacy handling (from eval):** Explicit "bridge vs archive" decision in early cross-cut; bulk src/ to legacy/; selective ports only.

**High-level phases (aligned to prior R0-R6 but wave-based and layered):**
- Foundation (Waves 1-2): L2/L3/L4/L5 core + first XGEN + L0 basics + XDOC/XLEG + packaging.
- Elevation (Waves 3-4): Full surfaces (L0/L1), bulk XGEN, L6/L7 maturation, self-hosting demos.
- Maturation & Distribution (Waves 5-6+): Polish, installer, external L8 examples, ongoing portfolio (XGEN/XSELF/XDOC).

---

## 3. Full Project Plan — Waves & Epics (Limited Details)

Waves are time-boxed increments (e.g. 2-4 weeks conceptually). Epics are layer-focused with limited scope. Owners reference agents from PLATFORM_AGENTS (new + composed imported). Reusability notes reference the evaluation report.

### Wave 1: Foundations & First Generalization (R1 — Current Focus)
**Goal:** Establish executable hybrid foundation (L2/L3), initial skill/agent loading (L4), starter surfaces (L0), first reusable imported assets generalized (per eval), doc/legacy hygiene started, packaging aligned. Enable first self-hosting smoke.
**Primary Layers/Cross:** L2 + L3 (core), L4 (basics), L0 (starter), Cross (XGEN batch 1, XDOC start, XLEG decision, XPACK).
**Duration/Owner:** Planning Agent sequences; Refactoring Agent executes structural/XGEN.
**Key Gates:** G0 (this wave charter), G1 (traceability of generalized items + this plan), G4 (on first XGEN tranche + structural decisions).
**Reusability Notes (from eval):** Prioritize high-reusability MATM planning/governance/audit (multi-sprint-portfolio-planner, sprint-*, kpi-drift, repo-governance-autoflow, governance-policy-compiler, hierarchy-*, independent-review-*, source-to-evidence/artifact-lineage) + FarmRTK orchestrate/process/audit/repo/technical/decision (first 5-7). These fit L2/L3/L4/Cross. Legacy decision here (Phase 2 of skill). Low-reusability docs bulk archived.

**Limited Epics (high-level):**
- E1.1 L2/L3: Procedural skill executor + basic hybrid router (invoke ide-* skills + generalized imports; LangGraph adapter stub). (WP-L2-001, WP-L2-003)
- E1.2 L3: Extend gate registry with initial IDE gates (editor contract, skill publication); apply policy profiles. (WP-L3-001)
- E1.3 L4: Skill/agent loader extension (discover from platform/skills/ + packs); basic viewer registration. (WP-L4-001, WP-L4-002)
- E1.4 L0: Basic agent/skill editors + 1-2 viewers (markdown, mermaid) in Zed + shell integration. (WP-L0-001, WP-L0-002)
- E1.5 Cross XGEN1: Generalize first batch of high-reusability imports (Planning family + audit core) per Phase 1 of skill; move stable to platform/skills/ or ide-platform; update registries + add IDE surfaces/PowerShell. (WP-XGEN-001 to WP-XGEN-007)
- E1.6 Cross XDOC/XLEG: First doc archive tranche (old sprint boards, duplicated governance); legacy `src/` decision record + initial move of bulk (keep src/platform/ evolving). (WP-XDOC-001, WP-XLEG-001)
- E1.7 Cross XPACK: Update pyproject/Makefile for new layers + skill invocation targets; platform health + smoke tests aligned to layered plan. (WP-XPACK-001)

**Dependencies:** Reusability eval (this report) complete. New agents/skills already added.
**Success (limited):** Router can invoke at least the 2 new skills + 1-2 generalized imports; first editors/viewers usable; 5+ imports generalized with evidence; legacy decision recorded; G0/G1/G4 passed on wave artifacts; self-hosting smoke (use agents to plan a tiny slice).

### Wave 2: Agent/Skill Elevation & Core Surfaces (R2)
**Goal:** Bulk elevation of agents/skills as first-class (L4/L5), richer surfaces (L0/L1), more XGEN, first GitHub provider work (L6), packaging mature.
**Primary Layers:** L4 + L5 (bulk), L0 + L1 (editors/viewers/interaction), L2/L3 (mature), L6 start, Cross XGEN2 + XSELF start.
**Limited Epics:**
- E2.1 L4/L5: Full skill/agent elevation (generalize remaining high-reusability MATM/FarmRTK into loadable units; workspace schema extensions for surfaces; loader complete). (WP-L4-003, WP-L5-001 etc.)
- E2.2 L0/L1: Agent editor with preview, multiple viewers (graph, source-to-evidence), basic interaction agents/HITL panel, ACP host + permissions. (WP-L0-003, WP-L1-001)
- E2.3 L2/L3: Full router (procedural + ACP primary); IDE gates enforcement; evidence bundles in viewers.
- E2.4 Cross XGEN2: Next batch of imports (architecture-design family, sprint lifecycle, requirements/traceability) + update this project plan with lessons.
- E2.5 L6 + Cross: GitHub provider basics + gh skills (PR evidence); first self-hosting demo (execute small wave slice using current surfaces/agents).
- E2.6 Cross XDOC/XPACK: More archive; full test alignment + CI for layers.

**Gates:** G0/G1/G2/G4/G5 on major increments.
**Reusability:** Continue Phase 1 generalization on remaining high-reusability items; selective legacy ports (hitl, tools) to L1-L3.

### Wave 3: Hybrid Maturation & Pack Integration (R3)
**Goal:** Complete hybrid (L2), viewer expansion, pack maturation (L7), self-hosting as norm, first external L8 example.
**Limited Epics:** L2 full (LangGraph adapter mature); L7 (ide-platform + engineering-sdlc generalized, threat-modeling wrapper + viewer); L0/L1/L3/L4/L5 polish + more XGEN (remaining MATM/FarmRTK); Cross XSELF (dogfood major increment); L8 start (sample workspace for external product).

### Wave 4: GitHub-Native & Advanced Surfaces (R4/R5)
**Goal:** Deep GitHub integration (L6), advanced editors/viewers/interaction (L0/L1), full L7 toolchains, installer evolution.
**Limited Epics:** L6 (rich gh + Actions enforcement for all layers); L0 (full editor suite for manifests/evidence/prompts); L7 (toolchain plugins + CI templates); Cross XGEN complete for high-reusability; packaging/distribution updates.

### Wave 5-6+: Distribution, Polish & Ongoing Portfolio (R6+)
**Goal:** Full installer, living docs, public L8 examples (embedded + service), ongoing XGEN/XSELF/XDOC as portfolio items (Planning Agent maintains), G5 baselines.
**Limited Epics:** L0/L7 polish + contribution guides; external product adoption; continuous generalization of any remaining + new packs; self-hosting as default development mode.

**Ongoing Cross-Cut Portfolio Items (across all waves, tracked by Planning Agent):**
- XGEN backlog (all imports per reusability eval; ~30 packages).
- XSELF (self-hosting coverage metrics).
- XDOC (doc hygiene waves).
- XPACK (packaging/CI evolution).
- Measured via kpi-drift-analyst patterns (planning quality, generalization %, legacy debt reduction, self-hosting %).

---

## 4. Success Criteria & Metrics

- 100% of high-reusability imported assets (per evaluation report) generalized, layer-mapped, and registered by end of Wave 3.
- All waves pass required gates with evidence (G0/G1/G4/G5).
- Self-hosting: At least 50% of Wave 3+ increments executed using the IDE's own agents/skills/gates/surfaces.
- Clean layer boundaries: No legacy mixing in platform/ or core L2-L5 after Wave 1 decision.
- Living docs: Historical bloat archived; concise "how to add X" guides for all layers/surfaces.
- External adoption: At least one L8 product workspace using the IDE by Wave 6.
- Metrics (tracked in waves via generalized kpi/program-metrics + drift analyst): Per-layer completion, XGEN %, evidence lineage coverage, planning quality on this plan itself.

---

## 5. Governance & Execution of This Plan

- This plan is a living Layer 2 artifact. Re-plan at start of each wave by invoking Planning Agent with `ide-portfolio-planning` (scope to layers + remaining XGEN from reusability report).
- Structural work in waves executed by Refactoring Agent with `ide-structural-refactoring` (follow all 5 phases per skill, including self-update of this skill/report).
- Detailed per-wave plans (see first wave below) expand the limited epics.
- Evidence from every wave attached to GitHub (via L6) and reviewed (G4).
- Escalation per skill: Large legacy or new surface needs → Planning Agent; architecture misalignment → Chief Engineer + HITL.

**Related artifacts:** Layered IDE_REFACTOR_PLAN.md (deep per-layer), LAYER_WORK_PACKAGE_INDEX.md (WP catalog), REUSABILITY_EVALUATION_REPORT.md (this eval), new agents/skills, ide-platform pack.

This is the governing project plan. Future waves will reference and update it.

**End of high-level project plan (limited details).** See detailed first wave plan for expanded tasks on Wave 1.