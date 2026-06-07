# System Architecture (Legacy / Pre-Reboot View)

**Status:** This document describes the pre-reboot (pre-2026-06) LangGraph-centric architecture. It is retained for historical reference but is **superseded** by the new agentic IDE platform layered model.

**Authoritative Sources (New IDE Platform View):**
- [docs/charter/FRAMEWORK_DECOMPOSITION.md](charter/FRAMEWORK_DECOMPOSITION.md) — L0–L8 + Cross severable layers with explicit capabilities per layer.
- [docs/charter/IDE_REFACTOR_PLAN.md](charter/IDE_REFACTOR_PLAN.md) (especially §5: Architecture Traceability, Capabilities & Functional Decomposition).
- [docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md) — Standalone matrix: Requirements → Capabilities → Functional Decomposition (hierarchy metadata) → Artifacts → Verification/Evidence.
- [docs/ide-structure-requirements-baseline.md](ide-structure-requirements-baseline.md) and [docs/ide-structure-architecture-disposition.md](ide-structure-architecture-disposition.md) — Self-hosted requirements and disposition for the IDE structure itself.
- [docs/structural-refactor-execution-plan.md](structural-refactor-execution-plan.md) (Tranche 2 section) and [docs/charter/ide-refactor/LAYER_WORK_PACKAGE_INDEX.md](charter/ide-refactor/LAYER_WORK_PACKAGE_INDEX.md).
- Recent generalized artifacts in `plugins/packs/ide-platform/` (Tranche 1 + Tranche 2: ide-hierarchy-taxonomy-steward, ide-kpi-drift-analyst.agent.md, ide-repo-governance-autoflow-orchestrator, etc.) and the tooling/executor foundation (see todo list for L2 executor + ide-specific tools).

## Shift to New Model
The reboot (Platform Reboot Charter + IDE_REFACTOR_PLAN) moves from a monolithic LangGraph supervisor (old Levels 0-2) to a **severable, plugin-first, hybrid orchestration** IDE platform:
- **L0**: GUI Shell (editors for .agent.md/SKILL.md, viewers, panels, PowerShell terminal).
- **L1**: Agent Runtime (ACP stdio, tool permissions scoped to IDE surfaces).
- **L2**: Orchestration (new procedural SKILL.md executor + LangGraph adapter + ACP; hybrid router).
- **L3**: Gate Engine + HITL + Evidence (registry-driven, maturity profiles, bundles).
- **L4**: Plugin Host (discover/load SKILL.md + .agent.md from packs; tool registry + permissions; viewer registration).
- **L5**: Workspace (manifest-driven context, maturity affecting gates).
- **L6**: Providers (Grok Build ACP primary, GitHub as first-class with gh skills).
- **L7**: Packs (ide-platform for core process/governance + domain packs; agents/skills as first-class pack content).
- **L8 + Cross**: Product consumption, legacy migration (quarantine to legacy/), doc hygiene (archive to docs/archive/), continuous XGEN (generalization of imports), self-hosting/dogfooding.

**Hybrid Execution**: Procedural (SKILL.md steps with PowerShell + gh), LangGraph (stateful where valuable), ACP (interactive multi-agent, e.g. Planning + Refactoring Agents).

Old patterns (shared AgentState, PostgresCheckpointer, interrupt_before/after HITL, review board subgraphs) are selectively bridged into L2 (LangGraph adapter) and L3 (HITL policy) or re-expressed via the new generalized skills (ide-portfolio-planning, ide-structural-refactoring) and the upcoming L2 executor + tool layer.

**Legacy Note**: The pure hierarchical LangGraph supervisor described below is no longer the primary model. It informed early governance but is being generalized and elevated into the new L0-L8 surfaces and ide-platform pack content.

## Retained Useful Elements (for Bridging)
- Persistent state and checkpointing → L2/L5.
- HITL interrupts and evidence packages → L3.
- Multi-agent collaboration (review boards) → Generalized into ide-independent-review-orchestrator family and ACP sessions (L1/L2).

For the current authoritative design, start with the charter documents and traceability matrix listed above. The old 12-agent SDLC capabilities (see docs/CAPABILITIES.md) are now treated as examples/domain content in packs (e.g., engineering-sdlc) rather than core platform.

## Old High-Level Design (Deprecated View — For Reference Only)
(This section is the original pre-reboot content. Do not extend it.)

### High-Level Design
This system uses a **hierarchical LangGraph** with persistent state.

- **Level 0 (Supervisor)**: Program Manager + Chief Engineer agents
- **Level 1**: Specialist Agents (Requirements, Architecture, Safety, etc.)
- **Level 2**: Review Board Subgraphs (multi-agent collaborative reviews)

### Core Components

#### Shared State (`AgentState`)
- Current artifacts (requirements, architecture, code baseline, etc.)
- Risk register, decision log, history summary
- Program metrics (schedule, open issues, verification status)

#### Persistence
- LangGraph `PostgresCheckpointer` → survives restarts
- pgvector → long-term memory & RAG

#### Human-in-the-Loop
LangGraph `interrupt_before` / `interrupt_after` nodes allow experts to review, edit, or override decisions.

#### Review Boards
Implemented as reusable subgraphs where multiple specialist agents debate, vote, and produce a recommendation. Chief Engineer / Program Manager can override with justification.

### Data Flow
1. New task → Supervisor routes to appropriate agent(s)
2. Agent works → updates shared state
3. Major decision → routed to Review Board subgraph
4. HITL interrupt (if configured)
5. Continue or loop back as needed

**End of legacy content.** All new development follows the L0-L8 IDE platform model and the traceability in the matrix.