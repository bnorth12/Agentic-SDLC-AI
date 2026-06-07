# GUI Design — Agentic IDE Shell (L0)

**Status:** Initial consolidated design (R1–R2 foundations, full surfaces in R2+)
**Parent:** [FRAMEWORK_DECOMPOSITION.md](../charter/FRAMEWORK_DECOMPOSITION.md) (L0 `gui-shell`) · [IDE_REFACTOR_PLAN.md](../charter/IDE_REFACTOR_PLAN.md) (L0 + L1 work packages) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md) (L0-001 traceability)
**Traceability:** Directly satisfies REQ-STRUCT-002 (first-class editable artifacts under discoverable locations), REQ-STRUCT-004 (L0-L8 decomposition visible in UI), REQ-STRUCT-006 (editors/viewers for agents/skills/evidence, PowerShell + GitHub native, self-hosting). See matrix L0-001 and L4-001 / L5-001.

---

## 1. System-Level Design (What the GUI Must Deliver)

### 1.1 Vision & Core Experience
A coherent, workspace-driven agentic IDE where:
- Users open a workspace (manifest-driven repos + packs + maturity).
- First-class artifacts are directly editable: `.agent.md`, `SKILL.md`, `plugin.manifest.yaml`, gate evidence bundles, layer work packages, traceability matrix rows.
- Rich viewers render work products in context (markdown, diagrams, graphs, tables, audit trails).
- Agent interaction is native (ACP panels, slash commands, multi-agent sessions).
- Everything is governed: tool permissions are explicit, actions produce evidence, gates (G0–G5) surface in the UI with HITL controls.
- PowerShell (Windows primary) + GitHub are first-class (terminal, gh tasks, PR evidence).
- The UI itself demonstrates the L0–L8 model and is self-hosting friendly (the platform's own agents/skills/packs are the best examples).

### 1.2 Major Areas / Information Architecture (Top-Level Layout)
The target long-term shell will provide a modern, dockable, multi-pane IDE layout that follows contemporary lightweight editor design patterns (dockable panels, structure-aware editors, rich viewers, command surfaces, agent interaction areas, integrated terminal, etc.). It will be a fully custom, unique implementation purpose-built for the agentic IDE. We will not reuse or fork source from Zed, VS Code, Eclipse, or any other editor.

In the meantime, we are deliberately continuing with a **PowerShell-first** primary interaction and development surface (the L2 executor running SKILL.md procedures, the `ide_core` tools, direct skill invocation, and terminal workflows). This allows continued self-hosting and platform advancement until we are ready to instantiate a clean custom GUI framework as a true MVP shell.

1. **Workspace / Explorer** (left sidebar, L5-driven)
   - Tree of repos from `workspace/*.yaml`.
   - Packs (`plugins/packs/*`), with agents/ and skills/ subtrees.
   - First-class artifacts highlighted (`.agent.md`, `SKILL.md`, manifests, evidence bundles).
   - Quick filters: "Generalized", "Pending XGEN", "My recent", gate status.

2. **Editor Area** (central, tabbed or split)
   - Structure-aware editors for:
     - Agent definitions (`.agent.md`): outline + rich text + preview of composition.
     - Skills (`SKILL.md`): frontmatter editor + procedure steps + "invoke" action.
     - Manifests (`plugin.manifest.yaml`, `platform/manifest.yaml`).
     - Evidence bundles, ADRs, layer work packages, traceability matrix rows.
   - "Invoke skill" / "Run via executor" button that routes to L2 (procedural / ACP).
   - Live preview / diff for generated artifacts.

3. **Viewers Dock / Panels** (right or bottom, multi-view)
   - Registered via L4 viewer registry + gate `viewer` field.
   - Current planned (R2/R3):
     - `viewer.markdown` — REQ, ADR, backlog, SKILL.md body, evidence.
     - `viewer.mermaid` — architecture diagrams, threat models, layer decompositions.
     - `viewer.graph-canonical` — MATM-style graphs, dependency / traceability graphs.
     - `viewer.stix` — threat bundles.
     - `viewer.icd-csv` / interface tables.
     - `viewer.audit-trail` — G1/G4 evidence, invocation records, hierarchy validation results.
   - Viewers can be opened from gate evidence, from editors, or from the explorer.
   - Multiple viewers can be open simultaneously; layout is persisted per workspace.

4. **Agent Interaction Panel** (right or floating, L1 + L2)
   - ACP-powered chat / session UI for Planning Agent, Refactoring Agent, other generalized agents.
   - Multi-agent sessions (e.g., joint Planning + Refactoring run on a wave charter).
   - Slash command input (`/orchestrate-ide-portfolio`, `/refactor-ide-structure`).
   - Real-time evidence streaming from L2 executor / L3 gates.
   - HITL controls surfaced here (approve/reject gate, edit artifact before proceeding).

5. **Integrated Terminal** (bottom, PowerShell primary on Windows)
   - Full OS terminal (pwsh / bash) with platform context injected (workspace root, active pack, current gate context).
   - Can run generalized procedural steps directly.
   - Output can be captured as evidence and sent to viewers or the matrix.

6. **Status / Governance Bar** (top or bottom)
   - Current workspace + maturity level (affects gate modes).
   - Active gate / evidence status.
   - XGEN progress (from the traceability matrix).
   - Tool permission / scope indicator (what the current skill/agent is allowed to do).
   - GitHub / PR status for the active change.

7. **Command Palette + Global Search**
   - "Open agent", "Invoke skill", "View evidence for WP-L2-001", "Run traceability audit".
   - Search across all artifacts (agents, skills, matrix rows, evidence).

8. **Settings / Preferences**
   - Workspace manifest editor (visual + raw).
   - Gate policy overrides.
   - Tool permission profiles.
   - Theme + layout presets.
   - Provider configuration (Grok Build, GitHub, etc.).

### 1.3 Key User Flows (System Level)
- **Open as IDE workspace** → Load manifest → Populate explorer with agents/skills/packs → Show L0-L8 decomposition hint in UI.
- **Edit + Invoke cycle** → Open `ide-structural-refactoring/SKILL.md` in editor → "Invoke" button → L2 executor runs it (using ide_core tools) → Evidence appears in `viewer.audit-trail` and matrix row updates.
- **Multi-agent planning** → Open Agent Panel → Start joint session with Planning + Refactoring Agents → They produce updated charter + matrix → User reviews in viewers + HITL gate.
- **Self-hosting hygiene** → Run `ide-repo-audit` or `ide-process-audit` → Results in viewers + matrix updated + new evidence bundle.
- **Generalization PR flow** → Edit/create new ide-* skill → Pre-commit `ide-check-work-commit` scan → Viewers show impact on matrix → Merge gate runs `ide-independent-review`.

### 1.4 Non-Functional Requirements (System Level)
- **First-class artifact editing**: Any `.agent.md` or `SKILL.md` opened from the explorer must feel native (structure-aware, live validation, invoke action).
- **Viewer extensibility**: New viewers registered via L4 pack manifest + gate registry; no core rebuild required.
- **Permission visibility**: Every tool call or executor step must show its scope in the UI.
- **Evidence as first-class**: Every significant action produces a viewable evidence bundle that can be opened in the appropriate viewer and linked in the matrix.
- **Performance**: Responsive even with large numbers of generalized agents/skills (hundreds).
- **Self-hosting**: The GUI must make it natural to develop the platform itself (the repo opened as a workspace should feel complete).
- **Hybrid execution transparency**: User should see whether a skill is running procedurally (L2 executor), via ACP, or LangGraph.

---

## 2. Software-Level Design (How the GUI Is Built)

### 2.1 Layer Responsibilities (L0 + Dependencies)
- **L0 (GUI Shell)**: Presentation, layout, editors, viewers, terminal, agent panels. Does **not** implement business logic for skills/agents (delegates to L2/L4).
- **L1 (Agent Runtime)**: ACP stdio host, tool permission enforcement scoped to IDE surfaces.
- **L2 (Orchestration)**: Procedural executor + router (invokes skills from editor "invoke" actions or panels).
- **L3 (Gates + Evidence)**: Gate evaluation, HITL interrupts, evidence bundle production. Viewers are wired to gate `viewer` fields.
- **L4 (Plugin Host)**: Discovery of `SKILL.md` / `.agent.md`, viewer registry, tool registry + permissions, pack loading.
- **L5 (Workspace)**: Manifest-driven configuration that populates the explorer, enables/disables surfaces, sets maturity (affects gate modes and tool scopes).

### 2.2 Major Components (SW Level)
- **ShellHost** (`gui/shell/`)
  - Current: Zed Personal via `zed-agent-servers.json` (ACP registry).
  - Future: Portable host (Tauri / custom) that owns layout, docks, theming, global command palette.
  - Responsibilities: window management, persistent layout (per workspace), terminal integration, status bar.

- **EditorManager**
  - Structure-aware editors for agent/skill/manifest/evidence.
  - Uses language server (LSP) for code + custom outline / form views for frontmatter + procedure steps.
  - "Invoke" action that constructs a WorkPackage and sends to L2 router.
  - Live validation (calls `validate_hierarchy_metadata` from ide_core tools).

- **ViewerRegistry + ViewerHost**
  - L4-registered viewers (markdown, mermaid, graph, etc.).
  - Opened by gate evidence, by editor actions, or explicitly.
  - Each viewer is a self-contained pane that can request more context (e.g., "show related matrix row").

- **AgentPanel / SessionHost** (L1 + L2)
  - ACP client for interactive agents.
  - Multi-session support.
  - Slash command router.
  - Real-time evidence subscription from L2/L3.

- **ToolPermissionUI**
  - Visual indicator and approval surface for what the current executing skill/agent/tool is allowed to do (read/write specific artifact types, run pwsh, call gh, etc.).
  - Backed by L4 tool registry + L1 permission model.

- **EvidenceBus / GateClient**
  - Subscribes to L3 evidence production.
  - Routes evidence to the correct viewer and updates the traceability matrix view (if open).

### 2.3 Data Models (Key SW Artifacts)
- `Workspace` (from L5 manifest): repos, packs, maturity, gate overrides, enabled surfaces.
- `Artifact` (first-class): id, type (agent|skill|manifest|evidence|matrix-row), path, frontmatter, body, hierarchy metadata.
- `GateEvidence`: bundle id, gate, producer (skill or agent), payload, viewer hints, traceability links.
- `ViewerRegistration`: id, supported formats/mime, component, gate association.
- `ToolScope`: what a running procedural step is allowed (read paths, write paths, execute commands, call other skills).

### 2.4 Integration Points & Extensibility
- **With L2 Executor**: Editor "invoke" or panel action → WorkPackage (skill_id, payload, mode=procedural) → executor runs SKILL.md steps → evidence returned → L3 + viewers.
- **With L4 Loader**: On workspace open or pack change, L4 discovers new agents/skills/viewers/tools and registers them with L0 surfaces.
- **With Gates (L3)**: Every significant editor action or viewer open can be gated; evidence is produced.
- **Pack Extensibility (L7)**: Domain packs can contribute viewers, toolchains, and even custom editor behaviors via manifest.
- **Self-hosting**: The `ide-platform` pack (agents + skills) + the matrix + this design doc are the primary content the GUI is built to edit and visualize.

### 2.5 Philosophy: Unique Custom Instantiation (Modern Editor Patterns, No Source Reuse)
The long-term GUI is **not** a fork, embedding, or reuse of Zed, VS Code, or Eclipse source code.

- We follow **design patterns and interaction models** from modern lightweight editors (Zed in particular for its speed and extensibility feel, VS Code for the overall dockable editor + panel + viewer paradigm).
- All core components are built by us: custom shell, custom editors for `.agent.md`/`SKILL.md`/manifests, custom viewer system, custom agent interaction surfaces, custom layout/docking engine, etc.
- Extensibility comes through our own L4 plugin host + pack manifests (viewers, tools, editor behaviors), not by forking an existing editor's extension system.
- The goal is a purpose-built agentic IDE that feels familiar to developers coming from Zed/VS Code, but is optimized for first-class agent/skill artifacts, evidence viewing, multi-agent sessions, and governance.

### 2.6 Current Implementation State (Bootstrap Only)
- **Temporary Phase 1 host (bootstrap / early self-hosting)**: Zed Personal is used via `gui/shell/zed-agent-servers.json` for ACP agent integration and a working PowerShell terminal. This gives us fast iteration on agents, skills, the executor, and the platform itself while the custom shell is built.
- **Long-term host**: Custom portable shell (targeting Tauri + webview or a more native custom implementation). This will own the full custom layout, editors, viewers, panels, etc.
- **Installer**: `gui/installer/Install-AgenticPlatform.ps1` (minimal/full profiles) — currently bootstraps Zed + platform for convenience.
- **Viewers**: Stubs + registry definition only (`gui/viewers/README.md`). Real custom viewer implementations planned R2 (markdown, mermaid, icd) / R3 (graph, stix, audit trails).
- **Editors / Panels**: Will be custom components in the new shell (structure-aware editors for agent/skill artifacts, agent interaction panels, etc.). The current "Zed config" work is purely bootstrap scaffolding.
- **Agent panel & multi-agent**: Will be custom surfaces in the portable shell, backed by L1 ACP + L2 router.
- **Tool permissions UI**: Will be custom, integrated with the L4 tool registry and L1 permission model. (P1: registry.py + scopes + frontmatter declarations + PS Invoke-IdeTool.ps1 implemented and live-tested; dual for current PowerShell-MVP and future GUI terminal PS integration.)
  P2 complete: run_robust_powershell (truncation, timeout, env scoping, basic sandbox) now default for SKILL.md pwsh steps via executor; dedicated Run-RobustPwsh.ps1 + registry exposure; real skill tests; dual PS/GUI. See matrix L2-001 / invocation record.
  P4: gh_evidence tool (auth, create/attach evidence to issues/PRs, schema) + Invoke-GhEvidence.ps1; registry + real SKILL integration via python/tool calls. Dual. See matrix TOOL-001, test_p4_gh_evidence_smoke.py.
  P5: gate_evidence_bundler + New-GateEvidenceBundle.ps1 (bundle exec+gh for G1/G3/G4 into md/json viewer bundles); GateEngine integration; real SKILL + engine tests. Dual. See matrix L3-001, test_p5_gate_evidence_bundler_smoke.py.

### 2.7 Open Decisions & Risks (to be resolved in detailed SW design)
- Exact layout/docking engine for the custom portable shell (we will own this, not reuse an existing editor's).
- Editor implementation strategy (custom structure-aware components for `.agent.md` / `SKILL.md` vs. leveraging LSP where it makes sense for code-like content).
- Depth of in-UI tool permission prompting vs profile-based trust.
- How deeply the traceability matrix and layer work packages are visualized live vs. treated as first-class editable artifacts.
- Theming, theming extensibility, and accessibility for our custom shell.
- Whether to start the custom shell on Tauri (webview) for speed of development or go more native earlier.

---

## 3. Roadmap Alignment (L0 Surfaces) — PowerShell-First Phase

- **R1 (current foundations, PowerShell-centric)**: Executor + tools + generalized content (including full FarmRTK batches) + traceability + architecture docs. Primary development and daily use of the platform happens through PowerShell (scripts, the L2 executor running SKILL.md procedures, `ide_core` tools, direct skill invocation, and an enhanced terminal experience). The temporary Zed ACP bridge is used only for early multi-agent sessions and convenience during self-hosting.

- **When ready — Custom GUI MVP**: Once a suitable GUI framework is available that allows a clean, minimal custom shell (no forking of existing editor source), we instantiate our own L0 GUI Shell. This will provide structure-aware editors for `.agent.md` / `SKILL.md` / manifests, basic viewers, agent panels, PowerShell terminal integration, etc., while strictly following our design patterns and owning the implementation.

- **R2+ (post-GUI MVP)**: Rich custom editors, multi-viewer layouts, full ACP multi-agent UI, tool permission surfaces, pack extensibility for viewers/editors, polished experience. At this point PowerShell remains fully supported and native, but the visual IDE becomes the primary surface for most users.

This approach lets us continue rapid self-hosting development inside our own generalized skills and executor without compromising the "unique custom instantiation" principle.

This document will be updated as L0 work packages are executed. All changes must maintain traceability in the matrix and reference the L0-L8 decomposition.

**End of initial GUI design.** Ready for detailed component specs, wireframes, or implementation tickets.