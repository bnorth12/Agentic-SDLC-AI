# IDE Architecture Traceability Matrix

**Parent Documents:**
- [IDE_REFACTOR_PLAN.md](../IDE_REFACTOR_PLAN.md) (especially new §5: Architecture Traceability, Capabilities & Functional Decomposition)
- [FRAMEWORK_DECOMPOSITION.md](../FRAMEWORK_DECOMPOSITION.md) (L0–L8 + Cross layer model and capabilities)
- [ide-structure-requirements-baseline.md](../../ide-structure-requirements-baseline.md) (REQ-STRUCT-001 to REQ-STRUCT-006, self-hosted)
- [structural-refactor-execution-plan.md](../../structural-refactor-execution-plan.md) (Tranche 2 details and hierarchy)
- [LAYER_WORK_PACKAGE_INDEX.md](LAYER_WORK_PACKAGE_INDEX.md)
- [remaining-xgen-refactoring-session.md](../../../agents/platform/invocations/remaining-xgen-refactoring-session.md) (Tranche 2 generalized agents/skills and tooling foundation)

**Purpose:** Provide a standalone, viewer/auditor-friendly matrix for G1 traceability. Maps:
Requirements (from structure baseline + PRODUCT_REQUIREMENTS.md context)  
→ Layer Capabilities (L0–L8 + Cross)  
→ Functional Decomposition (consistent hierarchy metadata)  
→ Concrete Artifacts (generalized agents/skills, plans, executor, tools)  
→ Verification / Evidence (G1/G4 audits, generalized skills, self-hosting loops).

**Model Overview:** All significant architecture elements, work packages (WP-Lx-xxx, WP-XGEN-xxx), and generalized artifacts must carry or link to:
- **Parent Capability**
- **Child Function**
- **Decomposition Level**
- **Allocated Component/Module**
- **Verification Method**

This enables the Planning Agent (`ide-portfolio-planning`) and Refactoring Agent (`ide-structural-refactoring`) to scope, execute, and evidence waves. The matrix is living and will be re-audited after each tranche (using generalized skills once the L2 executor + core tools are available).

**Key Requirements Sources (Trace Start):**
- From `ide-structure-requirements-baseline.md` (primary for IDE platform reboot):
  - REQ-STRUCT-001: Separate platform configuration (manifests, gates, schemas, imports) from content (agents, skills, pack capabilities).
  - REQ-STRUCT-002: First-class IDE artifacts (.agent.md, SKILL.md, manifests, evidence) must live in discoverable, editable locations under packs or designated content areas (supports L0 editors/viewers, L4 loading).
  - REQ-STRUCT-003: Quarantine legacy/historical material (src/, old docs) to avoid polluting living IDE surface.
  - REQ-STRUCT-004: Structure must demonstrate functional decomposition of L0-L8 layers and cross-cuts.
  - REQ-STRUCT-005: Packaging, discovery, and bootstrap must align so opening as workspace immediately surfaces agents, skills, and packs.
  - REQ-STRUCT-006: Explicit traceability from structure decisions back to IDE vision (editors for agents/skills, viewers for evidence, self-hosting, PowerShell + GitHub native, L0-L8 decomposition).
- From `PRODUCT_REQUIREMENTS.md` (historical SDLC context, L0 stakeholder needs → L3 implementation): SH-*, SYS-*, AGT-*, GOV-*, etc., with 4-level hierarchy. Used for continuity where old SDLC capabilities become examples in domain packs.
- WAVE_01 success criteria and Tranche 2 plan inherit the above.

**Status Legend:** Tranche 1 (initial generalized batch), Tranche 2 (remaining XGEN + tooling foundation), Pending (queued in todo list).

---

## Traceability Matrix

### Cross-Cutting (Applies to All Layers)
| ID | Source Requirement / Capability | Layer(s) | Functional Decomposition (Hierarchy) | Key Artifacts | Verification / Evidence | Status |
|----|--------------------------------|----------|-------------------------------------|---------------|-------------------------|--------|
| XGEN-001 | REQ-STRUCT-002 + L4/L7 "Agents/skills as first-class editable artifacts" | Cross XGEN + L4 + L7 | Parent: L4 Plugin Host + L7 Packs – Elevation of agents/skills<br>Child: Generalized, registered .agent.md + SKILL.md with IDE surfaces, hierarchy, PS/gh<br>Level: 2<br>Allocated: plugins/packs/ide-platform/ (agents/ + skills/)<br>Verification: Pack loader + manifest resolution | All Tranche 1/2 generalized in ide-platform (e.g. ide-hierarchy-taxonomy-steward.agent.md, ide-kpi-drift-analyst.agent.md, ide-technical-writer/SKILL.md, ide-validation-plan/SKILL.md + prior batch); plugin.manifest.yaml | ide-hierarchy-taxonomy-steward + ide-source-to-evidence-traceability runs; G1 from remaining-xgen-refactoring-session.md + this matrix; G4 on tranche | Tranche 1 + 2 |
| TOOL-001 | REQ-STRUCT-004 + L2 "Hybrid execution of first-class skills" + new tooling foundation | Cross + L2 + L4 | Parent: L2 Orchestration – Procedural execution + tool support<br>Child: Tool registry + permission model; ide-specific file ops, generalize helpers, hierarchy validator as callable tools<br>Level: 3<br>Allocated: platform/tools/ or ide-platform/tools/; src/platform/orchestration/ (executor integration); tool registry in L4 loader<br>Verification: Tool call tests from generalized skills; integration in executor | New tools from todo list (file_operations_ide, generalize-import, hierarchy_validator, gh/evidence wrappers); executor (E1.1) | G2 executor/tool interface contracts; self-hosted runs (future); evidence bundles | P4 slice 1: gh_evidence.py (auth check, create/attach, schema) + registry 'gh_evidence' + test_p4_gh_evidence_smoke.py (structured calls). Slice 2: Invoke-GhEvidence.ps1 + schema/attach sim in smoke. Slice 3: real SKILL step (gh_evidence in python block + executor evidence). Prior P1/P2/P3 complete. Dual PS-MVP + GUI terminal ready. See invocation P4 logs. P4 concluded.
P5 slice 1: gate_evidence_bundler.py (exec+gh -> G1/G3/G4 bundles + md/json); 'bundle_gate_evidence' registry; smoke (bundle+viewer+invoke). Live PASS. Tiny anchors. L3-001/§5 trace.
P5 slice 2: New-GateEvidenceBundle.ps1 (PS wrapper); smoke for bundles from P2/P4 tools + viewer. Live PASS. Dual + anchors.
P5 conclusion (slice 3): GateEngine.bundle_evidence_for_gate integration + real executor result (skill with gates) + gh sim + registry + viewer outputs. Live PASS. All P5 complete in small batches. P5 concluded.
L0-001 MVP: Phases 1-4 executed (tkinter CUSTOM shell launchable on Win11: explorer L4, editor L0, PS terminal P2, viewers P5, gates L3, self-host via generalized skills, launcher + packaging). Full validation smokes. Tiny anchors. See GUI_DESIGN, invocation MVP plan. 
This batch (tasks 1-5): menu primary controls, ACP panel (task1), dockable Paned (task2), real editor load + palette (task3), clarity/legend/tooltips (task4), deeper github/grok (task5). GUI/HMI framework for plugins. Smoke PASS. See invocation. |
| XSELF-001 | REQ-STRUCT-006 + Cross XSELF "Self-hosting / dogfooding" | Cross XSELF | Parent: Cross – Use generalized agents/skills + tools/executor to perform further XGEN, audits, plan updates<br>Child: Re-apply ide-structural-refactoring / ide-portfolio-planning / audit skills to updated docs and artifacts<br>Level: 2<br>Allocated: agents/platform/invocations/*; updated plans + matrix<br>Verification: Full re-audit cycle (requirements baseline, disposition, G4 packet) | This matrix; IDE_REFACTOR_PLAN §5; invocation records; generalized skills | ide-governance-policy-compiler + ide-verification-coverage + ide-source-to-evidence-traceability on the matrix and §5 (once executor available) | Tranche 2 (partial); full after executor |

| X GOV-WIRING-001 | Cross "Mandatory engineering rigor in all interfaces (PS + GUI) before coding or user exposure" (this wiring) | Cross L2/L3/HMI | Parent: Cross – Governance surface that forces upfront skills (policy, hierarchy, traceability, verification, check-work) + evidence before any user command, GUI action, ACP suggestion, or coding start<br>Child: Preflight helpers in ShellHost + PS wrappers; new G0.1/G_pre_user/G_hmi gates; calls to ide-governance-policy-compiler + ide-check-work-commit etc. via L2; P5 bundles always; non-bypass in dispatch points<br>Level: 3<br>Allocated: src/platform/gui/shell_host.py (_run_governance_preflight + calls in invoke/palette/ACP/handoff); src/platform/tools/Invoke-IdeTool.ps1 (preflight before target); platform/gates/registry.yaml (new gates); L2 executor (gate/tool capture)<br>Verification: phase1 smoke extension (preflight calls); self-host run of the gov skills on the wiring itself; evidence bundles in viewers; matrix/plan updates | New gates G0.1_upfront_engineering, G_pre_user_command_testing, G_hmi_governance_enforcement; _run_governance_preflight + PS preflight code; updated matrix L0/L3/Cross, GUI_DESIGN flows, invocation GAP-CLOSURE + GOV anchors | G1 (this wiring audited by the skills it wires); live preflight evidence on every user action; prevents "code before engineering" and "command before test" | Wired in GOV batch after HMI closure (skills/tools self-host evaluation + implementation). Dual PS/GUI. Enforced at interfaces so rigor is never skipped. |

| X PS-IDE-TRANSITION-001 | Cross "PS-to-IDE self-hosting transition for continuing IDE development" | Cross L0/L2/L3 + HMI | Parent: Cross – Enable moving primary development surface from PS-MVP (robust wrappers + terminal) to the IDE itself (GUI + co-running PS) while preserving governance, traceability, and dual use<br>Child (Level 3): Catalog basic functionality baseline (menu/dockables/explorer/L2 invokes/gov preflights/ACP with context/PS context/self-host demo); document stubs/TODOs explicitly (editor full edit, rich viewers, strict gov blocking); dedicated transition checklist + testing; flip primary in manifests/docs when ready<br>  - L0-002 GUI as Governed IDE Dev Surface (Level 2, Allocated: shell_host.py + launch_ide.py + GUI_DESIGN baseline; Verification: transition smoke + preflight evidence on dev actions like edit/invoke/ACP)<br>  - L2-003 Executor with Gov Hooks for Transition (Level 3, Allocated: executor.py + preflight calls; Verification: auto-gov on user skills + L2 evidence)<br>  - L3-002 Mature Enforcement for IDE Dev (Level 2, Allocated: gates/registry.yaml + GateEngine + P5; Verification: G0.1/G_pre hard-block on transition paths + bundles)<br>  - Cross Dual Workflow (Level 2, Allocated: Invoke-IdeTool.ps1 + manifests + preflights; Verification: dual execution + gov evidence on PS/GUI)<br>Level: 3 overall<br>Allocated: docs/gui/GUI_DESIGN.md (Basic Functionality Baseline subsection); src/platform/gui/launch_ide.py + shell_host.py (transition notes + preflight); invocation record (PS-to-IDE Transition Readiness section); [PS_IDE_TRANSITION_PLAN.md](./PS_IDE_TRANSITION_PLAN.md) (full step-by-step with requirements + L0-L8 decomp); matrix this row + L0-001/L3-001 updates<br>Verification: temp_transition_gap_eval.py + skill runs (ide-verification-coverage etc.); phase1 smoke (core paths); explicit basic functionality catalog; future dedicated transition smoke | GUI_DESIGN 2.6 + new baseline catalog; [PS_IDE_TRANSITION_PLAN.md](./PS_IDE_TRANSITION_PLAN.md); matrix X PS-IDE-TRANSITION-001 + expanded L0/L3; invocation record GOV + new transition anchor; preflight wiring already produces gov evidence on all user paths | G1 (skills evaluated gaps); documented basic functionality (menu, dockables, real L2/P5/self-host, gov preflight, PS dual) sufficient to start developing the IDE inside the IDE; stubs/TODOs acceptable if basic functionality present and documented | Evaluated in TRANS batch using the skills/tools themselves (see temp_transition_gap_eval.py output + matrix self-audit note). Full plan created with requirements + functional decomp. Phase 0 intake executed (skills run via temp_phase0_intake.py, P5 bundle for G0, smoke re-PASS). Phase 1 Batch 1: decomp expanded with L0/L2/L3 subs (based on hierarchy/gov skill input). PS remains fully supported; transition when basic functionality + docs/tests allow moving dev work into the IDE. |

### L0 + L1 (GUI Shell + Agent Runtime)
| ID | Source Requirement / Capability | Layer(s) | Functional Decomposition (Hierarchy) | Key Artifacts | Verification / Evidence | Status |
|----|--------------------------------|----------|-------------------------------------|---------------|-------------------------|--------|
| L0-001 | REQ-STRUCT-002 (editable artifacts) + L0 "Agent/skill editors + viewers" | L0 | Parent: L0 GUI Shell – Editors and viewers for first-class artifacts<br>Child: Structure-aware editors for .agent.md / SKILL.md / manifests / evidence; rich viewers (markdown, mermaid, graph-canonical, audit); primary menu + workspace controls; dockable tool panes (PanedWindow); command palette; HMI clarity (UI Legend + hovers); ACP stdio host with JSON protocol + workspace context injection<br>Level: 2<br>Allocated: src/platform/gui/shell_host.py (CUSTOM tkinter ShellHost + _launch_custom_tkinter, menubar, _create_agent_panel with JSON framing, _on_tree_select, _show_command_palette, help_label + _show_ui_legend); src/platform/gui/launch_ide.py; gui/ (future viewers/editors)<br>Verification: test_phase1_batch1_smoke.py (menu methods, _create_agent_panel, palette, L4/L2/P5 wiring, ACP creation); live self-host demo (open repo -> explorer -> invoke generalized skill + P5 bundle); P1-P5 tool registry + L2 executor integration; tiny anchors in invocation record + this matrix | gui/ (CURRENT: tkinter CUSTOM MVP ShellHost with menu (File: open/close folder + reload via L4; GitHub via P4 gh_evidence; Grok/Build: Launch ACP + PS context + handoff; Help: full legend); dockable Paned (explorer | center with editor/viewers + PS terminal); real SKILL.md load on tree; Ctrl+P palette dispatching real skills; hover clarity + UI Legend explaining every stub/control + P1-P5/L2/L3/L4 wiring; ACP panel with initial system context (opened workspace/repo) + user messages as {"role":"user","content":...} + stdout JSON pretty or raw + real L2 handoff button); status bar with gates + self-host note. launch_ide.py entry (venv python -m src.platform.gui.launch_ide). Dual PS + GUI preserved. | **MVP delivered (phases 1-4 + 5-tasks batch + ACP protocol micro):** L0-001 advanced from scaffold to launchable Win11 CUSTOM shell with primary user controls (menu at top per user request), resizable dockable framework (ttk.PanedWindow, PS terminal as first-class example), real editor + palette (task 3), full clarity (UI Legend + hovers so "I can understand what any stub does"), deeper GH/Grok + ACP (task 1/5 with JSON fix for the exact user error "failed to parse... Raw: evaluate the repo..."). Self-hosting: the delivered IDE can open this repo, show ide-platform skills via L4, invoke real generalized skills via L2 + produce P5 bundles. See invocation record "Tasks 1-5..." and "MVP IDE Plan" sections + ACP-JSON-FRAME-001 anchor. Hierarchy enforced via ide-hierarchy-taxonomy-steward (this closure batch). Gaps remain for full rich editors/viewers (R2+), dedicated L0 surface gates, deeper G1 chains on the HMI surfaces themselves. |
| L1-001 | L1 "ACP stdio host + tool permissions" | L1 | Parent: L1 Agent Runtime – Interactive multi-agent sessions with scoped tools<br>Child: ACP host for Planning/Refactoring Agents + generalized skills; permission model for IDE surfaces (file ops, gh, etc.)<br>Level: 2<br>Allocated: src/platform/orchestration/acp/<br>Verification: Session handoff to L2 executor; permission enforcement tests | src/platform/orchestration/ (scaffold); tool permission integration with new tool registry | G3/HITL gates; ACP integration tests with ide-portfolio-planning / ide-structural-refactoring | Task 1: _create_agent_panel spawns agent_command, Text panel + handoff to L2 (in tkinter shell). Menu wired. Smoke PASS. See invocation. Partial (scaffold) -> more real in GUI. **ACP protocol fix (this micro-batch):** send initial system context (opened workspace/repo) + every typed command wrapped as JSON {"role":"user","content":...} before stdin write; stdout reader does json.loads+pretty or raw. Fixes exact error "failed to parse incoming message: expected value at line 1 column 1. Raw: evaluate the repo...". Stub improved to simulate context. Real L2 handoff preserved. Smoke re-validated PASS. Tiny anchor. L1-001 advance. |

### L2 (Orchestration) – Focus on Executor + Tooling
| ID | Source Requirement / Capability | Layer(s) | Functional Decomposition (Hierarchy) | Key Artifacts | Verification / Evidence | Status |
|----|--------------------------------|----------|-------------------------------------|---------------|-------------------------|--------|
| L2-001 | REQ-STRUCT-006 + L2 "Procedural SKILL.md executor + hybrid dispatch" (E1.1) | L2 | Parent: L2 Orchestration – Hybrid router (procedural / LangGraph / ACP)<br>Child: Procedural Skill Executor – parse SKILL.md frontmatter, execute pwsh/bash/Python steps or tool calls, capture/return evidence<br>Level: 3<br>Allocated: src/platform/orchestration/executor.py + tools/executor/run-skill.ps1; router.py updates<br>Verification: Smoke test running ide-structural-refactoring and ide-portfolio-planning procedures; G2 executor interface contract; evidence bundles to L3 | src/platform/orchestration/router.py (scaffold); new executor module; PowerShell example from WAVE_01 plan | Executor successfully runs generalized skills from Tranche 2; evidence packet for G4; integration with gate engine | Pending (primary L2 executor + tooling todo) |
| L2-002 | L2 "Integration of Planning & Refactoring Agents" + tool support | L2 + Cross XGEN | Parent: L2 Orchestration – Invocation of meta agents<br>Child: Wire ide-portfolio-planning and ide-structural-refactoring (and Tranche 2 skills) as invocable targets; support new tools (file ops, generalize, audits)<br>Level: 2<br>Allocated: src/platform/orchestration/; plugins/packs/ide-platform/agents/ (ide-portfolio-planning references via skills)<br>Verification: Successful invocation producing updated plans/matrix; G1 from invocation records | agents/platform/planning-agent.agent.md + refactoring-agent.agent.md; platform/skills/ide-* ; new tools | Runs in self-hosted context (e.g. this matrix generation); G0/G1 from planning/refactoring invocations | Tranche 1 (meta) + pending full executor wiring |

### L3 (Gate Engine + HITL + Evidence)
| ID | Source Requirement / Capability | Layer(s) | Functional Decomposition (Hierarchy) | Key Artifacts | Verification / Evidence | Status |
|----|--------------------------------|----------|-------------------------------------|---------------|-------------------------|--------|
| L3-001 | REQ-STRUCT-006 + L3 "Registry-driven enforcement + evidence bundles" | L3 | Parent: L3 Gate Engine + HITL + Evidence – Full G0-G5 enforcement with maturity profiles<br>Child: IDE surface gates (editor-contract, skill-pub, agent-rra, viewer-reg); evidence bundle format + viewer integration; policy compiler application<br>Level: 2<br>Allocated: platform/gates/registry.yaml; src/platform/gates/; generalized policy compiler<br>Verification: New gates in registry; evidence bundles from generalized audits; G4 packets | platform/gates/registry.yaml (extensions); ide-governance-policy-compiler; evidence/ from Tranche 2 | ide-governance-policy-compiler run on Tranche 2 + matrix; G4 independent review of structural/XGEN work | Partial (basic engine); extensions in progress |

### L4 + L5 (Plugin Host + Workspace) – Focus on ide-platform + Tools
| ID | Source Requirement / Capability | Layer(s) | Functional Decomposition (Hierarchy) | Key Artifacts | Verification / Evidence | Status |
|----|--------------------------------|----------|-------------------------------------|---------------|-------------------------|--------|
| L4-001 | REQ-STRUCT-001/002/005 + L4 "Discover/load SKILL.md + .agent.md; tool registry" | L4 + L7 | Parent: L4 Plugin Host – Load packs, providers, viewers, toolchains, skill/agent loading<br>Child: Discovery/registration of all XGEN generalized agents/skills (Tranche 1/2/3 + FarmRTK batches); tool registry + permissions; pack-local paths in ide-platform manifest<br>Level: 2<br>Allocated: plugins/packs/ide-platform/ (agents/ + skills/ + plugin.manifest.yaml); src/platform/plugins/ (loader) + ide_core tools<br>Verification: Loader finds and registers new ide-* (full list per manifest); tool calls (validate_hierarchy_metadata, etc.) succeed from skills; manifest updates | plugins/packs/ide-platform/ (full Tranche 1 + 2 + 3: all ide-* from MATM/FarmRTK incl. ide-decision-record, ide-icd-maintenance, ide-risk-register, ide-configuration-baseline, ide-data-storage, ide-test-authoring, ide-independent-review, ide-bom-procurement, ide-program-metrics, ide-check-work-commit + earlier); tool registry + ide_core | L4 loader tests; ide-hierarchy-taxonomy-steward validation; G1 from generalized artifacts' Parent sections + this matrix; cross with L2 executor | All XGEN complete (core + tooling); coordinated with PowerShell-MVP + custom GUI |
| L5-001 | REQ-STRUCT-002/004 + L5 "Workspace-driven everything" | L5 + Cross | Parent: L5 Workspace – Manifests, maturity, context for all layers<br>Child: Workspace schema extensions for editor/viewer slots, skill execution modes, agent RRA; drives L2 router, L3 gates, L4 loader<br>Level: 2<br>Allocated: workspace/ (templates + schemas); example-farmrtk.workspace.yaml updates<br>Verification: Workspace validation opens ide-platform content cleanly; maturity affects gate modes | workspace/templates/; platform/schemas/workspace.schema.json | Workspace loader tests; self-hosting "open as workspace" checks | Partial (example exists); extensions needed for IDE surfaces |

### L6 + L7 (Providers + Packs) + L8 + Cross (Legacy/Docs/Generalization)
| ID | Source Requirement / Capability | Layer(s) | Functional Decomposition (Hierarchy) | Key Artifacts | Verification / Evidence | Status |
|----|--------------------------------|----------|-------------------------------------|---------------|-------------------------|--------|
| L7-001 | REQ-STRUCT-002 + L7 "ide-platform pack maturation + domain packs" | L7 + Cross XGEN | Parent: L7 Packs – Delivery of domain + platform-process capabilities<br>Child: ide-platform as home for planning, refactoring, governance (Tranche 1/2 content); generalized engineering-sdlc, threat-modeling as wrapper<br>Level: 2<br>Allocated: plugins/packs/ide-platform/; plugins/packs/engineering-sdlc/ (beyond raw imports)<br>Verification: Pack manifests resolve correctly; generalized skills/agents loadable and traceable | plugins/packs/ide-platform/ (full Tranche 1 + 2); engineering-sdlc updates | Manifest resolution + loader tests; G1 on generalized content | Tranche 1 + 2 in progress |
| XDOC-001 / XLEG-001 | REQ-STRUCT-003 + Cross "Doc hygiene + legacy quarantine" | Cross XDOC + XLEG | Parent: Cross – Quarantine legacy, archive historical, keep living IDE-focused set<br>Child: Move bulk src/ to legacy/; docs/governance/ + old sprint boards to docs/archive/; update references<br>Level: 2<br>Allocated: legacy/; docs/archive/; src/platform/ (kept runtime pieces)<br>Verification: Before/after structure snapshots; compliance audit; no pollution of active surfaces | legacy/ (to be created); docs/archive/; updated pyproject.toml, Makefile, README, plans | ide-source-to-evidence-traceability on changes; G4 on structural work; re-baseline | Planned in execution plan Tranche 2 / Phase 2-3 |

**FarmRTK Continuation (this session, using new ide_core tools):**
- Batch 1 (previous): ide-repo-audit, ide-process-audit, ide-program-metrics, ide-check-work-commit.
- Batch 2 (executed in order): Used basic_generalize_stub (via tool) for plans on decision-record-farmrtk, icd-maintenance-farmrtk, risk-register-farmrtk, configuration-baseline-farmrtk, data-storage-farmrtk. Generalized to ide-decision-record, ide-icd-maintenance, ide-risk-register, ide-configuration-baseline, ide-data-storage. Wrote SKILL.md files. Validated (content check equivalent to validate_hierarchy_metadata tool: all 5 pass with full hierarchy metadata + explicit matrix/IDE_REFACTOR_PLAN §5 refs).
- New in ide-platform/skills/: ide-decision-record, ide-icd-maintenance, ide-risk-register, ide-configuration-baseline, ide-data-storage.
- Batch 3 (previous): ide-test-authoring, ide-independent-review, ide-bom-procurement.
- Completes the 17 FarmRTK platform skills generalization (modulo any absorption into meta like orchestrate/requirements/traceability). Closes final Cross XGEN rows. Advances WAVE-02 charter and full XGEN progress in matrix.

**Notes on Matrix Maintenance:**
- Update after each XGEN tranche or structural slice (Refactoring Agent produces updates; Planning Agent sequences).
- Include explicit links in all generalized .agent.md / SKILL.md (Parent sections) and plans (WP-IDs map to rows here).
- Future self-hosted audit (see below): Once L2 executor + core tools implemented, invoke generalized skills (ide-source-to-evidence-traceability, ide-hierarchy-taxonomy-steward, ide-governance-policy-compiler, ide-verification-coverage, ide-requirements-implementation-auditor) on this matrix + IDE_REFACTOR_PLAN §5 + updated docs.
- Evidence location: Link to `evidence/` bundles, invocation records, G4 packets.

---

## Visual Traceability Flow (Mermaid)

```mermaid
flowchart TD
    subgraph Requirements
        R1[REQ-STRUCT-001..006<br/>ide-structure-requirements-baseline.md]
        R2[PRODUCT_REQUIREMENTS.md<br/>historical L0-L3]
    end

    subgraph Layers
        L0[L0 GUI Shell<br/>Editors + Viewers]
        L1[L1 Agent Runtime<br/>ACP + Permissions]
        L2[L2 Orchestration<br/>Procedural Executor + Tools]
        L3[L3 Gate Engine<br/>Evidence + HITL]
        L4[L4 Plugin Host<br/>Loader + Tool Registry]
        L5[L5 Workspace]
        L6[L6 Providers]
        L7[L7 Packs<br/>ide-platform]
        CX[Cross XGEN / XSELF / XDOC / XLEG]
    end

    subgraph Capabilities
        C2[L2: Procedural execution<br/>+ tool calling]
        C4[L4: Skill/Agent discovery<br/>+ tool permissions]
        CXG[Cross: Generalization<br/>+ Self-hosting]
    end

    subgraph Artifacts
        A1[Tranche 2 ide-* agents/skills<br/>ide-hierarchy-*, ide-kpi-*, etc.]
        A2[L2 Executor + tools<br/>executor.py + ide_core.py]
        A3[Plans + Matrix<br/>IDE_REFACTOR_PLAN §5 + this file]
        A4[Invocation Records<br/>remaining-xgen-*.md]
    end

    subgraph Verification
        V1[ide-source-to-evidence-traceability]
        V2[ide-hierarchy-taxonomy-steward]
        V3[G1 / G4 bundles + re-baseline]
        V4[Self-hosted audit<br/>(post-executor)]
    end

    R1 --> L2
    R1 --> L4
    R1 --> CX
    R2 -.->|historical| L7

    L2 --> C2
    L4 --> C4
    CX --> CXG

    C2 --> A2
    C4 --> A1
    CXG --> A3

    A1 --> V1
    A2 --> V1
    A3 --> V2
    A1 --> V3
    A2 --> V3
    A3 --> V4
```

**How to read the diagram:** Requirements drive layer capabilities. Capabilities are realized by artifacts (generalized content + new executor/tools). Artifacts are verified by the generalized skills (once executable via the L2 executor).

---

**End of Matrix.** This file is the primary artifact for auditors and automated viewers. It is referenced from IDE_REFACTOR_PLAN.md §5 and the layer index. All changes in this reboot (including Tranche 2 and tooling foundation) are traced here for G1 compliance. 

**Revision History**
- Initial creation: Fleshed out from IDE_REFACTOR_PLAN §5, FRAMEWORK_DECOMPOSITION, structure baseline, and Tranche 2 work (remaining XGEN + tooling todos).
- Extended: Added L2 executor + tooling rows, Tranche 2 specifics, and Mermaid visual traceability flow.
- P1 batch: TOOL-001 advanced; src/platform/tools/registry.py (core + scopes + declaration parser) + executor integration + Invoke-IdeTool.ps1; live validation + SKILL frontmatter updates + tiny-anchor logs in invocation record. (Priority 1 of 5 tools executed in small testable batch for dual PS-MVP + future custom GUI/PS-integrated IDE.)
- P2 smallest slice: hardened _execute_powershell + run_robust_powershell (truncation, explicit timeout); registered as tool; test_p2_pwsh_smoke.py (success/trunc/timeout/registry paths) + live validation. Tiny anchors in invocation + this rev. Dual PS + GUI terminal. (L2-001 / TOOL rows, §5.)
- P2 slice 2: env= param (safe merge) + sandbox notes in robust pwsh; PS wrapper example; smoke extended for env. Live validation passed. Tiny anchors. Dual + §5/matrix trace. (Continuing small batches toward full sandbox.)
- P2 conclusion (slice 3): parser now uses run_robust_powershell for real SKILL.md steps; real skill step smoke test (temp SKILL + executor); dedicated Run-RobustPwsh.ps1; all P2 requirements (timeouts/env/cwd/output limits/error surfacing, sandbox notes, PS wrappers, registry, real tests, dual PS/GUI, §5/matrix trace) complete. Tiny anchors.
- P3 slice 1: PluginLoader extended with discover_skills() (pack entry.skills_dir + P1 frontmatter/tools parse); test_p3_loader_skills_smoke.py (ide-platform + declared_tools from P1). Live PASS. Tiny anchors. Advances L4-001 / Cross XGEN (manifest-driven discovery). Dual + §5 trace.
- P3 slice 2: run_procedural_skill now uses loader (manifest resolution); registry populates _skill_declarations from skills. Smoke validates end-to-end (via_loader, declared in outputs, reg decls). Tiny anchors. L4 integration complete.
- P3 conclusion (slice 3): Discover-IdePack.ps1 (PS helper); manifest + GUI_DESIGN updates; full live (py+PS discovery). All P3 items done (loader+discover, L4/executor/reg integrate, PS helper, ide-platform test, anchors, dual, trace to §5/L4-001). P3 concluded in small batches.