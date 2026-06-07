# IDE Refactor Plan — Full-Featured Agentic AI IDE (Layered by Abstraction)

**Produced by:** Planning Agent + Refactoring Agent  
**Primary Skills:** `ide-portfolio-planning` (sequencing & intake) and `ide-structural-refactoring` (structural generalization, architecture disposition, evidence)  
**Date:** 2026-06 (initial layered revision)  
**Parent:** [REBOOT_CHARTER.md](./REBOOT_CHARTER.md) · [FRAMEWORK_DECOMPOSITION.md](./FRAMEWORK_DECOMPOSITION.md) · [REFACTOR_TODO.md](./REFACTOR_TODO.md)  
**Status:** Living, abstraction-layered plan. Executed in waves via hybrid orchestration (procedural skills, LangGraph subgraphs, Grok Build ACP interactive sessions). The plan and all layer work are governed by G0 (wave charter), G1 (traceability), G4 (independent review / EIRC), and G5 (baseline).

**Traceability Note:** Every section explicitly references:
- Specific imported agents/skills being generalized (from `platform/imports/matm/agents/`, `platform/imports/matm/skills/`, `platform/imports/farmrtk/skills/`).
- The new Planning Agent / Refactoring Agent and their skills.
- Applicable gates from `platform/gates/registry.yaml`.
- Work package IDs (e.g. `WP-L2-003`, `WP-XGEN-010`).
- Cross-layer dependencies.
- Hierarchy metadata requirements for architectural changes.

**Full Traceability Model (Requirements → Capabilities → Functional Decomposition → Artifacts → Verification):**
This plan (and all layer work) maintains explicit chains:
- **Requirements**: Linked to ide-structure-requirements-baseline.md (REQ-STRUCT-*) and, where relevant, the broader PRODUCT_REQUIREMENTS.md (historical SDLC) or WAVE_01 success criteria.
- **Capabilities per Layer**: Defined in the expanded table below and in the enhanced FRAMEWORK_DECOMPOSITION.md.
- **Functional Decomposition**: Consistent hierarchy metadata (Parent Capability, Child Function, Decomposition Level, Allocated Component/Module, Verification Method) applied to work packages, generalized artifacts (e.g. ide-hierarchy-taxonomy-steward, ide-kpi-drift-analyst, procedural executor), and structural decisions. See LAYER_WORK_PACKAGE_INDEX.md for catalog and examples in ide-structure-* and structural-refactor-execution-plan.md.
- **Artifacts**: Concrete files (generalized .agent.md/SKILL.md in ide-platform, src/platform/orchestration/executor, manifests, plans, invocation records).
- **Verification/Evidence**: G1 traceability audits (ide-source-to-evidence-traceability), G4 independent review packets, compliance (ide-governance-policy-compiler), verification coverage (ide-verification-coverage), re-baselines, and this invocation record (remaining-xgen-refactoring-session.md) for Tranche 2.

Recent Tranche 2 generalized agents/skills (ide-hierarchy-taxonomy-steward, ide-repo-governance-autoflow-orchestrator, ide-requirements-implementation-auditor, ide-independent-review-history-rollup-orchestrator, ide-kpi-drift-analyst.agent.md fix) and the new tooling/executor foundation (E1.1) are decomposed at L2 (executor/router), L3 (policy/gates), L4 (pack loading + tool registry), and Cross (XGEN). See updated sections below and the Tranche 2 plan in structural-refactor-execution-plan.md.

---

## 1. Executive Summary & Current State (Joint Agent Baseline)

The repo is in R0 reboot-scaffold state. The target is a **thin, plugin-adaptable agentic IDE** with full editor/viewer suites, first-class skills and agents (editable inside the IDE), hybrid orchestration, PowerShell + GitHub baked in from the start, and strong governance (gates + HITL by policy + evidence).

**Key problems identified by the Refactoring Agent audit (see also the procedure in `ide-structural-refactoring`):**
- Strong new skeleton (`platform/`, `plugins/packs/`, `agents/platform/`, `src/platform/`, `gui/`, `workspace/`) mixed with dominant legacy (`src/` monolith, old scripts, docker, packaging, examples).
- Raw imports: 24 MATM `.agent.md` + 26 skills + 17 FarmRTK platform skills — still product-suffixed and hard-coded.
- Severe doc bloat/duplication (governance/, operations/, plans/, policies/, many historical sprint boards).
- No real execution path yet for the new Grok-style `SKILL.md` + `.agent.md` assets.
- GitHub and PowerShell integration aspirational only.

**Conclusion:** The copied agents and skills are excellent raw material for governance, planning, traceability, and assured process. They must all be generalized through the new `ide-*` skills into IDE-native components (editors, viewers, interaction models, skills, and agents as first-class work products). The plan is deliberately broken into **abstraction layers** (directly following [FRAMEWORK_DECOMPOSITION.md](./FRAMEWORK_DECOMPOSITION.md) L0–L8) so work is scoped, severable, and manageable while remaining fully cohesive and traceable.

The **Planning Agent** owns overall portfolio sequencing, wave intake, and cross-layer balance.  
The **Refactoring Agent** owns structural changes, import generalization, architecture/design disposition, evidence/lineage, and doc/legacy hygiene within and across layers.

---

## 2. Master Vision & Cross-Cutting Principles (Cohesion Rules)

**Vision (unchanged):** A coherent experience where users open workspaces, edit agents/skills/manifests/evidence with dedicated editors, view outputs with rich viewers, interact with agents via ACP panels and slash commands, develop new capabilities inside the IDE, and have everything pass through the gate engine with auditable evidence. PowerShell and GitHub are native. Platform is thin; domain lives in packs.

**Cross-cutting principles that apply to every layer (enforced by the two new agents):**
- **Abstraction discipline:** Changes respect severable layer boundaries. Work in one layer must declare explicit contracts to adjacent layers.
- **Generalization first:** Every use of an imported agent or skill must be made workspace-manifest-driven, gate-registry-driven, pack-manifest-driven, and IDE-surface-aware (editors/viewers/agents/skills as primary artifacts). Remove all FarmRTK/MATM product assumptions.
- **Traceability & lineage:** All work produces or updates source → architecture/design → implementation → verification → gate-evidence chains (using the imported auditors). Hierarchy metadata required for significant changes.
- **PowerShell + GitHub native:** Default procedures and examples use PowerShell (Windows primary) and `gh` CLI / GitHub Actions / PR evidence attachments.
- **Hybrid orchestration:** Every capability declares whether it is procedural (SKILL.md steps), LangGraph (stateful), or ACP (interactive).
- **Self-hosting & dogfooding:** Platform development itself uses the Planning Agent, Refactoring Agent, `ide-*` skills, gates, and (eventually) the IDE surfaces being built.
- **Gates by policy:** G0 (planning), G1 (traceability), G2 (interfaces/contracts), G4 (independent review), G5 (baseline) apply across layers with maturity gating.

**Ownership model (Planning + Refactoring Agents):**
- Planning Agent + `ide-portfolio-planning` → intake, sequencing, portfolio balance, wave charters.
- Refactoring Agent + `ide-structural-refactoring` → structural work, generalization, disposition decisions, evidence hygiene, legacy decisions.
- Both collaborate on cross-layer items and feed the Chief Engineer / EIRC as required.

---

## 3. Layered Refactor Map (Abstraction Breakdown)

This directly follows the L0–L8 model in FRAMEWORK_DECOMPOSITION.md.

| Layer | Responsibility | IDE Target Capabilities | Current State Gap | Primary Drivers (Agents + Skills) | Key Imported Assets to Generalize | Core Gates |
|-------|----------------|-------------------------|-------------------|-----------------------------------|-----------------------------------|------------|
| **L0** | GUI Shell (editors, terminals, layout, viewers) | Agent editor, Skill editor, Manifest editor, Evidence viewer, Mermaid/Graph viewers, Agent panel, PowerShell terminal integration | Only Zed json + minimal PS1 installer + viewer README stubs | Refactoring Agent (structural), Planning Agent (sequencing of surfaces) | N/A (new surfaces); technical-writer-farmrtk for docs | G2 (interfaces), G4 |
| **L1** | Agent Runtime (ACP, Grok Build, permissions) | ACP stdio host, tool permission model for IDE surfaces, interactive multi-agent sessions | Minimal `src/platform/orchestration/` scaffold | Refactoring Agent + Planning Agent | MATM independent-review-orchestrator family (for interaction governance) | G3/G4 (HITL) |
| **L2** | Orchestration (router: procedural / LangGraph / ACP) | **Capabilities**: Procedural SKILL.md executor (parse frontmatter, run pwsh/bash/Python steps, return evidence); hybrid dispatch (procedural + LangGraph + ACP); invocation of Planning/Refactoring Agents and all generalized ide-* skills; evidence aggregation for L3. | Router only returns "scaffold" | Refactoring Agent (wiring + generalization) + Planning Agent (usage in plans) | orchestrate-farmrtk, multi-sprint-portfolio-planner, sprint-* family; new E1.1 executor + tooling | G0, G1, G4 |
| **L3** | Gate Engine + HITL + Evidence | **Capabilities**: Registry-driven enforcement of all gates (incl. new IDE surface gates: editor-contract, skill-pub, agent-rra); maturity profiles; evidence bundle production/validation/viewer integration; policy compilation for strict platform core. | Basic engine exists; no IDE-specific gates yet | Refactoring Agent (schema + policy) + Planning Agent (intake) | governance-policy-compiler, hierarchy-*, independent-review-orchestrator, sprint-closeout-certifier | All gates (especially G0, G1, G4, G5) |
| **L4** | Plugin Host (packs, providers, viewers, toolchains, skill/agent loading) | **Capabilities**: Discovery/loading/registration of SKILL.md + .agent.md (first-class editable artifacts); viewer & tool registry with permissions; pack loader for ide-platform (Tranche 1/2 generalized agents/skills) + other packs; manifest-driven resolution. | Only basic pack manifest loader | Refactoring Agent (elevation of skills/agents) | All 24 MATM agents + 17 FarmRTK platform skills (generalize into loadable units); new tool registry & ide-specific tools | G1, G2, G4 |
| **L5** | Workspace (manifests, maturity, context) | Workspace-driven everything (packs, gates, shell, providers, repos); maturity affects gate modes | One example-farmrtk.workspace.yaml | Planning Agent (intake against manifests) + Refactoring | requirements-baseline-steward, traceability-blocker-planner | G0, G1, G5 |
| **L6** | Providers (LLM + GitHub + secrets) | GitHub provider as first-class (PRs, Actions, gh CLI skills); Grok Build as primary interactive | github-devops pack is skeleton | Refactoring Agent + github-devops collaboration | repo-governance-autoflow-orchestrator (for GitHub context) | G4 (merge), G5 |
| **L7** | Packs (domain + ide-platform) | `ide-platform` pack (planning, refactoring, core process), generalized engineering-sdlc, threat-modeling as viewer+wrapper | engineering-sdlc still points at raw imports; ide-platform stub just created | Refactoring Agent (generalization into packs) + Planning Agent (portfolio) | All FarmRTK platform skills + MATM governance skills; threat A1–A9 stay wrapped | G1, G4, G5 |
| **L8 + Cross** | Product repos + Legacy migration + Doc hygiene + Overall generalization | External workspaces consume the IDE; legacy `src/` decided (bridge/archive); docs normalized to living IDE-focused set | Heavy legacy + raw imports + doc bloat | Refactoring Agent (primary) + Planning Agent (sequencing) | All remaining imported agents/skills + legacy `src/agents`, `src/graphs`, old docs | G1, G4, G5 |

**Cross-layer concerns** (owned jointly, sequenced by Planning Agent, executed structurally by Refactoring Agent):
- Continuous generalization of the 24+ imported assets.
- Doc archive + living documentation.
- Legacy `src/` handling.
- Packaging, bootstrap, test, and CI alignment.
- Self-hosting / dogfooding the layered plan using the agents and skills themselves.

---

## 4. Detailed Layer Plans (Abstraction-Based Parts)

Each subsection is a self-contained but linked part of the plan. Work packages use layer-prefixed IDs for traceability.

### L0 + L1 — GUI Shell, Editors, Viewers, Interaction Agents, Agent Runtime

**Target for full IDE:** Users edit `.agent.md`, `SKILL.md`, manifests, and evidence with structure-aware editors. Rich viewers (mermaid, graph-canonical, source-to-evidence, audit trails) appear in panels. Agent interaction happens in ACP-powered panes with PowerShell terminal. Tool permissions are explicit.

**Key work packages (WP-L0/L1-xxx):**
- WP-L0-001: Basic agent + skill editors (markdown + outline + "invoke skill" action) in Zed config + future shell host.
- WP-L0-002: Viewer registry + first viewers (viewer.markdown, viewer.mermaid, viewer.graph-canonical) wired to gate `viewer` fields.
- WP-L0-003: Agent panel + multi-agent ACP session support (L1).
- WP-L1-001: ACP stdio host + permission model scoped to IDE surfaces (editors, skills, viewers, evidence).
- WP-L0-010: Interaction agent patterns (HITL panel, command router, chat-with-agent) — generalize interaction governance from MATM independent-review-orchestrator family.

**Imported assets:** Primarily new surfaces; pull interaction governance patterns from MATM independent-review-* and sprint-intake-gatekeeper.

**Dependencies:** Needs L2 (router to invoke skills from editors) and L3 (gate evidence visible in viewers).  
**Gates:** G2 (interface contracts for editors/viewers), G4.  
**Owner:** Refactoring Agent leads structural work; Planning Agent sequences surface rollout.  
**Traceability:** Every new editor/viewer must have architecture/design disposition with hierarchy metadata.

### L2 + L3 — Orchestration Router, Gate Engine, HITL, Planning & Refactoring Agents

**Target:** A real hybrid router that can execute `ide-portfolio-planning`, `ide-structural-refactoring`, and all future generalized skills. Gate engine extended with IDE-specific gates (editor contract, skill publication, agent RRA review). The Planning and Refactoring Agents are first-class invocable participants.

**Key work packages:**
- WP-L2-001: Procedural skill executor (parse SKILL.md frontmatter + steps, support PowerShell entrypoints, return evidence).
- WP-L2-002: LangGraph adapter bridge (for stateful legacy patterns that are worth keeping).
- WP-L2-003: Full integration of Planning Agent + Refactoring Agent into the router (as ACP or procedural targets).
- WP-L3-001: Extend `platform/gates/registry.yaml` with IDE surface gates (editor, viewer, skill-pub, agent-rra).
- WP-L3-002: Policy compiler + maturity logic applied to IDE development profiles (strict for platform core).
- WP-L3-010: Evidence bundle format and viewer integration (generalize from artifact-lineage-auditor + source-to-evidence-traceability-auditor).

**Imported assets:** orchestrate-farmrtk + multi-sprint-portfolio-planner → L2 planning paths; governance-policy-compiler + hierarchy-* + independent-review-orchestrator family → L3; sprint-closeout-certifier, remediation-readiness-strategist.

**Dependencies:** L4 (plugin host must load the skills/agents the router invokes); L5 (workspace provides gate overrides and maturity).  
**Gates:** G0, G1, G3, G4 (the plan itself and all layer work pass these).  
**Owner:** Refactoring Agent (wiring + generalization); Planning Agent (defines usage in waves).

### L4 + L5 — Plugin Host, Skill/Agent Elevation, Workspace Manifests

**Target:** Skills and agents are loadable first-class artifacts (`.agent.md` + `SKILL.md` discoverable from platform/skills/ and packs). Workspace manifests drive packs, gates, shell, providers, and IDE surface availability. `ide-platform` pack is mature.

**Key work packages:**
- WP-L4-001: Extend plugin loader (or add platform skill/agent loader) to discover `SKILL.md` and `.agent.md`.
- WP-L4-002: Viewer registration contract + loader.
- WP-L4-003: Generalize all 24 MATM agents + 17 FarmRTK platform skills into loadable, registered units (move out of `imports/` when stable).
- WP-L4-010: `ide-platform` pack maturation (skills_dir, agents_dir, IDE-specific entrypoints for editors/viewers).
- WP-L5-001: Workspace schema extensions (editor/viewer slots, skill execution modes, agent RRA profiles).
- WP-L5-002: Workspace loader + validation used by router, gate engine, and shell.

**Imported assets:** The entire set — every agent and skill must be processed by `ide-structural-refactoring` Phase 1 (generalize) + Phase 3 (disposition).

**Dependencies:** L2/L3 (things to load and enforce); L7 (packs are the delivery mechanism).  
**Gates:** G1 (traceability of every generalized artifact), G2 (contracts), G4.  
**Owner:** Refactoring Agent (elevation + generalization); Planning Agent (portfolio of which surfaces go into which workspaces).

### L6 + L7 — Providers, Packs, Toolchains, GitHub Integration

---

## 5. Architecture Traceability, Capabilities & Functional Decomposition

This section provides the rigorous cross-layer traceability and decomposition that was previously distributed or implicit. It directly supports G1 and enables the Planning and Refactoring Agents (and future executor/tools) to reason about scope.

### 5.1 Requirements Traceability (Source)
Primary source for IDE platform structure and generalization:
- **ide-structure-requirements-baseline.md** (self-hosted, produced by ide-requirements-baseline skill):
  - REQ-STRUCT-001: Separate platform config (manifests/gates/schemas/imports) from content (agents/skills/packs).
  - REQ-STRUCT-002: First-class IDE artifacts (.agent.md, SKILL.md, manifests, evidence) must be discoverable/editable under packs or designated content areas.
  - REQ-STRUCT-003: Quarantine legacy/historical material.
  - REQ-STRUCT-004: Structure must demonstrate L0-L8 + Cross functional decomposition.
  - REQ-STRUCT-005: Packaging/bootstrap must surface agents/skills/packs when opened as workspace.
  - REQ-STRUCT-006: Explicit traceability from structure decisions back to IDE vision (editors, viewers, self-hosting, PowerShell+GitHub, layers).
- Linkage to broader PRODUCT_REQUIREMENTS.md (historical SDLC hierarchy L0-L3) is maintained for continuity where relevant, but the reboot prioritizes the IDE-specific baseline above.
- WAVE_01 success criteria and Tranche 2 plan (in structural-refactor-execution-plan.md and remaining-xgen-refactoring-session.md) inherit these.

All work packages and generalized artifacts (including Tranche 2: ide-hierarchy-taxonomy-steward, ide-kpi-drift-analyst.agent.md, ide-repo-governance-autoflow-orchestrator, etc., and new L2 executor + tools) must trace to one or more of the above.

### 5.2 Capabilities by Layer (Refined)
See the expanded "Capabilities by Layer" in the companion FRAMEWORK_DECOMPOSITION.md. Key IDE-platform-relevant capabilities (updated for Tranche 2 and tooling):

- **L2 Orchestration Capabilities** (primary for executor + routing): Procedural SKILL.md execution (frontmatter parse, step execution with pwsh/bash/Python, evidence capture); hybrid dispatch; invocation of ide-portfolio-planning / ide-structural-refactoring and all generalized skills; evidence handoff to L3.
- **L3 Gate + Evidence Capabilities**: IDE surface gates (editor-contract, skill-pub, agent-rra, viewer-reg); policy profiles; evidence bundles (traceability, hierarchy, compliance); HITL.
- **L4 Plugin Host + Tooling Capabilities**: SKILL.md/.agent.md discovery & loading from ide-platform (now including Tranche 2 items); tool registry with permissions/scoping; viewer registration; pack manifest resolution.
- **Cross (XGEN / XSELF / XDOC / XLEG) Capabilities**: Systematic generalization of imported assets into IDE-native form; self-hosting (using generalized agents/skills + new tools/executor to perform further generalization, audits, and plan updates); doc hygiene while preserving G1 chains; legacy quarantine decisions with hierarchy.

### 5.3 Functional Decomposition (Hierarchy Metadata Standard)
All significant architecture elements, work packages, and generalized artifacts use this consistent format (as applied in ide-structure-requirements-baseline.md, structural-refactor-execution-plan.md, and recent Tranche 2 work):

- **Parent Capability**: (e.g., L2 Orchestration – Hybrid execution of first-class skills/agents)
- **Child Function**: (specific executable slice, e.g., Procedural execution of SKILL.md with evidence)
- **Decomposition Level**: 2–4
- **Allocated Component/Module**: (concrete path or artifact, e.g., src/platform/orchestration/executor.py + plugins/packs/ide-platform/agents/ide-xxx.agent.md)
- **Verification Method**: (e.g., smoke via executor; ide-source-to-evidence-traceability + ide-hierarchy-taxonomy-steward; G1/G4 evidence from this plan + invocation record)

**Examples (including new work):**
- L2 Executor (WP-L2-001): Parent = L2 Orchestration; Child = Procedural SKILL.md runner; Level=3; Allocated = src/platform/orchestration/ + tools/executor/run-skill.ps1; Verification = run on ide-structural-refactoring + evidence bundle; G2 contract.
- L4 Tool Registry & ide-specific tools (new from tooling todos): Parent = L4 Plugin Host; Child = Tool discovery, permission enforcement, file ops for .agent.md/SKILL.md, generalization helpers; Level=2; Allocated = platform/tools/ or ide-platform/tools/ + registry in loader; Verification = tool call tests from generalized skills; integration in executor.
- Tranche 2 Agent (e.g. ide-hierarchy-taxonomy-steward): Parent = L3/L4 Governance + Plugin Host (Cross XGEN); Child = Enforce L0-L8 taxonomy on generalized artifacts and plans; Level=2; Allocated = plugins/packs/ide-platform/agents/ide-hierarchy-taxonomy-steward.agent.md + skill; Verification = application in this plan + re-audit by the skill itself (self-hosting); G1/G4.
- Similar decomposition applied to ide-kpi-drift-analyst, ide-repo-governance-autoflow-orchestrator, ide-requirements-implementation-auditor, ide-technical-writer, ide-validation-plan, and all prior generalized items.

The LAYER_WORK_PACKAGE_INDEX.md serves as the living catalog of these decompositions (WP-IDs map to the hierarchy fields).

### 5.4 Traceability Matrix (Summary View)

| Source Requirement / Capability | Layer(s) | Functional Child (Hierarchy) | Key Artifacts (Tranche 1/2 + Tooling) | Verification / Evidence |
|--------------------------------|----------|------------------------------|---------------------------------------|-------------------------|
| REQ-STRUCT-002 (first-class agents/skills as editable artifacts) + L4 Plugin Host capability | L4 + L7 + Cross XGEN | Discovery/loading of SKILL.md/.agent.md; tool registry | plugins/packs/ide-platform/ (all ide-* from Tranche 1 + ide-hierarchy-*, ide-kpi-*.agent.md, ide-repo-governance-*, ide-requirements-implementation-*, ide-technical-writer, ide-validation-plan); plugin.manifest.yaml | Pack loader test; ide-hierarchy-taxonomy-steward run; G1 from remaining-xgen-refactoring-session.md + this plan |
| L2 Orchestration capability + WP-L2-001 | L2 | Procedural SKILL.md executor (parse + execute + evidence) | src/platform/orchestration/executor (new); tools/executor/run-skill.ps1; router.py updates | Executor smoke on ide-structural-refactoring; G2 contract; evidence bundle to L3 |
| Tooling foundation (new E1.1 + ide-specific tools todos) | L2 + L4 | File ops for .agent.md/SKILL.md; generalize helpers; hierarchy validator as tool; gh/evidence tools | platform/tools/ or ide-platform/tools/; tool registry; permission model | Tool call tests from generalized skills; self-hosting run by Refactoring Agent; G1 |
| REQ-STRUCT-004 (demonstrate L0-L8 decomp) + hierarchy cross-cutting | Cross + all | Consistent hierarchy metadata on all WPs and artifacts | LAYER_WORK_PACKAGE_INDEX.md; all generalized .agent.md (Parent/Child/Level/Allocated/Verification sections); structural-refactor-execution-plan Tranche 2 | ide-hierarchy-taxonomy-steward + source-to-evidence audits; G4 on wave |
| Self-hosting (XSELF) + G1 | Cross | Use generalized skills + new executor/tools to perform further XGEN/audits/plans | This invocation record; updated plans; Tranche 2 artifacts | Full re-audit cycle (requirements baseline, disposition, this plan, G4 packet) |

This matrix will be maintained in LAYER_WORK_PACKAGE_INDEX.md and re-generated/audited after each tranche (using the generalized audit skills once the executor is available).

**Traceability for Recent Work**: All Tranche 2 generalized agents/skills and the tooling/executor foundation trace directly to the requirements in ide-structure-requirements-baseline.md, the capabilities in this plan + FRAMEWORK_DECOMPOSITION, the functional hierarchy in the execution plan and layer index, and evidence in the remaining-xgen-refactoring-session.md invocation record.

---

### L6 + L7 — Providers, Packs, Toolchains, GitHub Integration

**Target:** GitHub provider is rich (PRs as work packages, Actions as gate enforcers, `gh` skills). `ide-platform` pack + generalized engineering-sdlc and threat-modeling exist. Toolchain plugins are declared and used by workspaces.

**Key work packages:**
- WP-L6-001: GitHub provider implementation (repos, Actions, PR evidence, gh CLI task execution).
- WP-L6-010: Deep `gh` CLI skills (create PR with evidence, query lineage, trigger gate workflow) — generalize from repo-governance-autoflow-orchestrator.
- WP-L7-001: Complete generalization of engineering-sdlc pack (move beyond raw imports).
- WP-L7-002: Threat-modeling pack as proper wrapper + graph viewer (keep A1–A9 as domain).
- WP-L7-003: First language/toolchain plugins (python, powershell, node) with detection + CI templates.
- WP-L7-010: `ide-platform` pack declared and used in the example workspace.

**Imported assets:** repo-governance-autoflow-orchestrator, repo-audit-*, process-audit-*, kpi-drift-analyst (for GitHub + pack governance); configuration-baseline + risk + validation + icd skills (as example assured flows inside packs).

**Dependencies:** L3 (gates enforced by GitHub Actions); L5 (workspace declares providers and packs); L4 (packs loaded).  
**Gates:** G4 (merge enforcement), G5 (baseline of packs).  
**Owner:** Refactoring Agent + collaboration with github-devops pack.

### Cross-Layer & L8 — Legacy, Docs, Overall Generalization, Self-Hosting, Product Alignment

**Target:** Legacy `src/` is explicitly decided (legacy/ tree + bridge or archive). Docs are slim and IDE-focused. All imported assets are generalized. The platform develops itself using its own layered plan, agents, and skills. External product repos (L8) consume the IDE cleanly.

**Key work packages (WP-X-xxx or WP-L8-xxx):**
- WP-XGEN-001 to WP-XGEN-030: Systematic generalization of every one of the 24 MATM agents + 17+ FarmRTK skills (one or more per wave, tracked by Planning Agent).
- WP-XLEG-001: Legacy `src/` decision record + execution (move to `legacy/`, extract useful pieces to `src/platform/`, update all references).
- WP-XDOC-001: Create `docs/archive/`, move historical sprint boards + duplicated governance, produce living IDE docs (`how-to-add-agent.md`, `ide-architecture.md`, etc.).
- WP-XSELF-001: First self-hosting milestone — use (Zed + Grok Build + current generalized skills + Planning/Refactoring Agents) to execute a slice of this plan and pass G4 on the result.
- WP-XPACK-001: Packaging alignment (pyproject, Makefile, skill smoke tests, platform-focused health check).
- WP-XL8-001: Workspace template and onboarding guide for an external product repo consuming the IDE.

**Imported assets:** Everything not yet covered; plus legacy `src/agents/*`, `src/graphs/supervisor.py`, old docs, etc.

**Dependencies:** All layers (generalization and hygiene touch everything).  
**Gates:** G1, G4, G5 (especially on self-hosting evidence and legacy decisions).  
**Owner:** Refactoring Agent leads; Planning Agent sequences waves and maintains portfolio view of debt reduction.

---

## 5. Cross-Layer Dependency Matrix & Wave Sequencing (Planning Agent)

**Dependencies (high-level):**
- L0/L1 surfaces need L2 (invocation) + L3 (evidence + HITL) + L4 (loading).
- L2/L3 need L4 (what to load and enforce) + L5 (context/manifests).
- L4/L5 need L7 (packs deliver the loadable units).
- L6/L7 need L3 (enforcement) + L5 (declaration).
- Cross-layer (legacy, docs, generalization, self-hosting) touches all and must be sequenced carefully.

**Wave sequencing guidance (Planning Agent using `ide-portfolio-planning`):**
- R1 waves: L2/L3 foundation (executor + basic gates) + first L4 loader extensions + L0 basic editors + first batch of XGEN (the two new agents/skills we already created) + XDOC first archive + XLEG decision.
- R2 waves: Full L0–L5 elevation (editors, viewers, agent/skill as first-class, workspace extensions) + remaining XGEN (bulk of the 24+ imports) + first GitHub provider work.
- R3+ waves: L6/L7 maturation, rich viewers, self-hosting demos, installer, external L8 examples.
- Ongoing: XGEN backlog, XSELF dogfooding, XDOC maintenance — tracked as portfolio items with KPI drift analysis.

Each wave must produce an intake verdict (G0) and pass G4 before closeout.

---

## 6. Traceability Catalog (Key Mappings)

**New agents/skills we introduced (already traceable):**
- Planning Agent ← multi-sprint-portfolio-planner + sprint-intake-gatekeeper + orchestrate-farmrtk + kpi-drift-analyst + ...
- Refactoring Agent ← repo-governance-autoflow-orchestrator + architecture-design-* + source-to-evidence-traceability-auditor + artifact-lineage-auditor + governance-policy-compiler + ...
- `ide-portfolio-planning` and `ide-structural-refactoring` (in platform/skills/ and referenced from ide-platform pack).

**Full imported asset → layer mapping** is maintained in the agents' SKILL.md files and will be updated by the Refactoring Agent during each XGEN tranche. Every generalized artifact must:
- Drop product suffix.
- Reference workspace/gate/pack manifests instead of hard paths.
- Declare IDE surfaces (editor, viewer, interaction, execution mode).
- Carry or link to architecture/design disposition + hierarchy metadata.
- Be registered in PLATFORM_AGENTS.md or the owning pack.
- Participate in at least one gate.

---

## 7. Risks, Governance, Execution Model & Success Metrics

(See original risks in prior version — they remain valid. Layering reduces "too much at once" risk by giving each wave clear abstraction scope.)

**Governance for this plan and its layered parts:**
- This document and all layer work packages are subject to G0 (charter), G1 (traceability to this plan + imported sources + reboot charter), G4 (independent review of structural waves), G5 (baseline after major layer increments).
- The Planning Agent prepares wave charters and intake evidence. The Refactoring Agent prepares structural disposition and evidence bundles. Both use their primary skills.

**How to execute a layer or cross-cut:**
1. Planning Agent (via `ide-portfolio-planning` skill) produces or updates the wave plan scoped to specific layers or WP-IDs.
2. Refactoring Agent (via `ide-structural-refactoring`) executes the generalization, disposition, and hygiene steps for the scoped items.
3. Results (generalized files, decision records, evidence) are reviewed (G4) and baselined (G5) as appropriate.
4. Self-hosting: repeat the above using the IDE surfaces as they come online.

**Success metrics (layer-aware, tracked by kpi-drift-analyst patterns):**
- Per-layer completion % (e.g., "L2/L3 router + gate engine: 40%").
- % of the 24+ imported agents/skills fully generalized and layer-registered.
- Cross-layer debt items closed per wave.
- Self-hosting coverage (waves executed using the agents/skills being built).
- All layer changes pass G1 + G4 with explicit evidence and hierarchy metadata.

---

**End of layered plan — produced and refined by the Planning Agent and Refactoring Agent.**

This version is deliberately structured by abstraction (L0–L8) for manageability while remaining one cohesive, fully traceable document. The master vision, cross-cutting principles, dependency matrix, and ownership model tie the parts together. Every layer and work package is linked back to the imported assets, the new agents/skills, and the gates.

**Related artifacts created/updated in this session:**
- `agents/platform/planning-agent.agent.md` and `refactoring-agent.agent.md`
- `platform/skills/ide-portfolio-planning/SKILL.md` and `ide-structural-refactoring/SKILL.md`
- `plugins/packs/ide-platform/plugin.manifest.yaml`
- Updates to `PLATFORM_AGENTS.md`, `IMPORT_MANIFEST.md`, `REFACTOR_TODO.md`, root `AGENTS.md`
- This plan (layered revision) + invocation record

The plan is now ready for wave-level breakdown by the Planning Agent and structural execution by the Refactoring Agent. Future re-planning of this document itself should be done by invoking the Planning Agent.