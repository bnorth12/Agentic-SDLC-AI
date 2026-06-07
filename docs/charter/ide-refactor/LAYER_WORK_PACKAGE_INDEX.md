# Layer Work Package Index + Dependency Matrix

**Parent:** [IDE_REFACTOR_PLAN.md](../IDE_REFACTOR_PLAN.md) (the cohesive master plan)  
**Purpose:** Quick-reference catalog of work packages organized by abstraction layer (L0–L8 + cross-cutting). Enables the Planning Agent (`ide-portfolio-planning`) and Refactoring Agent (`ide-structural-refactoring`) to scope waves, track progress, and maintain traceability.

All IDs, dependencies, gates, and imported asset links are defined in the master plan. This file is a living index, not a replacement for the full narrative.

---

## Layer Ownership Model (recap from master plan)
- **Planning Agent + ide-portfolio-planning**: Owns sequencing, wave intake (G0), portfolio balance, cross-layer prioritization.
- **Refactoring Agent + ide-structural-refactoring**: Owns structural execution, generalization (XGEN), architecture/design disposition, evidence/lineage hygiene, legacy decisions.
- Both collaborate on any layer that touches IDE surfaces or governance.

---

## Prioritized XGEN Sequencing for Max Bang-for-Buck (per user direction)

**Current refined order for early waves (R1 focus):**
1. **Requirements + Traceability** (before Arch/Design/Implementation) — requirements-baseline-steward, traceability-blocker-planner / source-to-evidence-traceability-auditor, requirements-management-farmrtk, traceability-audit-farmrtk.
2. **Architecture & Design** (disposition, change, alignment, document surfaces, functional decomp of layers) — architecture-design-disposition-planner, architecture-design-change-author, implementation-architecture-alignment-auditor, architecture-document-surface-enforcer, icd-maintenance-farmrtk, decision-record-farmrtk.
3. **Compliance / Governance / Policy / Independent Review** — governance-policy-compiler, hierarchy-*, process-audit-farmrtk, repo-governance-autoflow-orchestrator, independent-review-orchestrator family, check-work-*-farmrtk.
4. **Verification / V&V Planning & Execution** — verification-coverage-planner, validation-plan-farmrtk, test-authoring-farmrtk, sprint-closeout-certifier, remediation-readiness-strategist.

This order gives the most immediate value for governing the IDE build itself (including repo structure improvements and self-hosting). We will use these capabilities to drive the structural refactor as an early self-hosted task (produce requirements + architecture for the IDE-aligned repo structure, disposition the changes, execute under compliance/verification).

The Planning Agent + ide-portfolio-planning and Refactoring Agent + ide-structural-refactoring remain the orchestration and execution backbone. We expect (and plan for) iteration/refactoring as clearer architecture emerges.

**XGEN Progress (burning through prioritized procedures):**
- Generalized (in ide-platform pack; full coordination across L4/L7/Cross + manifests + tools): requirements-baseline-steward, architecture-design-disposition-planner, governance-policy-compiler, verification-coverage-planner, source-to-evidence-traceability-auditor, independent-review-orchestrator, architecture-design-change-author, ide-architecture-design-traceability-auditor, ide-implementation-architecture-alignment-auditor, ide-kpi-drift-analyst (agent artifact added), ide-architecture-document-surface-enforcer, ide-artifact-lineage-auditor, ide-hierarchy-conformance-auditor, ide-sprint-closeout-certifier, ide-remediation-readiness-strategist, ide-sprint-execution-compliance-monitor, ide-sprint-intake-gatekeeper, ide-traceability-blocker-planner, ide-multi-sprint-portfolio-planner, ide-architecture-contract-enforcer, ide-process-audit, ide-repo-audit, ide-traceability-audit, ide-hierarchy-taxonomy-steward, ide-repo-governance-autoflow-orchestrator, ide-requirements-implementation-auditor, ide-independent-review-history-rollup-orchestrator + supporting. All FarmRTK (17; batches 1-3 in order via ide_core tools): ide-repo-audit, ide-process-audit, ide-program-metrics, ide-check-work-commit, ide-decision-record, ide-icd-maintenance, ide-risk-register, ide-configuration-baseline, ide-data-storage, ide-test-authoring, ide-independent-review, ide-bom-procurement, ide-technical-writer, ide-validation-plan, ide-kpi-drift-analyst, ide-requirements-baseline, ide-traceability-audit, ide-source-to-evidence-traceability, ide-hierarchy-taxonomy-steward, ide-hierarchy-conformance, ide-requirements-implementation-auditor, ide-governance-policy-compiler, ide-process-audit, ide-repo-audit, ide-independent-review-orchestrator, ide-multi-sprint-portfolio-planner, ide-sprint-*, ide-traceability-*, ide-verification-*, ide-remediation-*, ide-artifact-lineage, ide-architecture-*, etc. (see ide-platform/plugin.manifest.yaml, IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md, invocation record for full list + coordination with L2 executor, ide_core tools, manifests, PowerShell-MVP, custom GUI). See agents/platform/invocations/remaining-xgen-refactoring-session.md and structural-refactor-execution-plan.md Tranche 2 section. XGEN progress: complete for platform skills.
- All generalized items and new L2 executor + tooling foundation now carry explicit traceability in the enhanced IDE_REFACTOR_PLAN.md §5 (Requirements from ide-structure-requirements-baseline → Layer Capabilities → Functional Hierarchy (Parent/Child/Level/Allocated/Verification) → Artifacts → Evidence). See also updated FRAMEWORK_DECOMPOSITION.md for per-layer capabilities + decomposition examples.
- Self-hosted artifacts produced: ide-structure-requirements-baseline.md, ide-structure-architecture-disposition.md, structural-refactor-execution-plan.md (using the new agents/skills + Refactoring Agent for functional decomp, compliance, verification hooks).
- We are burning through the order (Requirements → Architecture/Design → Compliance → Verification) and will redline/adapt plans, skills, and structure as clearer designs emerge. The copied agents continue to be the raw material for IDE-native versions.

A first concrete self-hosted procedure exercise has been performed: a Requirements Baseline for the IDE structure/repo alignment was produced using `ide-requirements-baseline` (see docs/ide-structure-requirements-baseline.md). This fed the Architecture/Design Disposition for structural changes. We are burning through the prioritized procedures (Requirements, Architecture/Design, Compliance, Verification) and will redline and adapt as we execute.

## Work Package Catalog (by Layer)

### L0 + L1 — GUI Shell, Editors, Viewers, Interaction, Runtime
- WP-L0-001: Basic agent + skill editors (markdown + outline + invoke action)
- WP-L0-002: Viewer registry + first viewers (markdown, mermaid, graph-canonical)
- WP-L0-003: Agent panel + multi-agent ACP sessions (L1)
- WP-L1-001: ACP stdio host + IDE-scoped tool permissions
- WP-L0-010: Interaction agent patterns (HITL panel, command router) — generalize from MATM independent-review-orchestrator + sprint-intake-gatekeeper

**Primary imported patterns:** MATM independent-review-* family, sprint-intake-gatekeeper  
**Key gates:** G2, G4  
**Cross-layer deps:** Needs L2 (invocation), L3 (evidence), L4 (loading)

### L2 + L3 — Orchestration, Gate Engine, HITL, Planning/Refactoring Integration
- WP-L2-001: Procedural skill executor (SKILL.md parsing, PowerShell entrypoints, evidence return)
- WP-L2-002: LangGraph adapter bridge (selected legacy stateful patterns)
- WP-L2-003: Integrate Planning Agent + Refactoring Agent into router (ACP or procedural)
- WP-L3-001: Extend gate registry with IDE surface gates (editor-contract, viewer-reg, skill-pub, agent-rra)
- WP-L3-002: Policy compiler + maturity profiles for IDE development (strict vs advisory)
- WP-L3-010: Evidence bundle format + viewer integration (generalize artifact-lineage-auditor + source-to-evidence-traceability-auditor)

**Primary imported patterns:** orchestrate-farmrtk + multi-sprint-portfolio-planner + sprint-* family (L2); governance-policy-compiler + hierarchy-* + independent-review-orchestrator family + sprint-closeout-certifier (L3)  
**Key gates:** G0, G1, G3, G4 (this plan and all layer work)  
**Cross-layer deps:** Needs L4 (loadable units), L5 (manifest context)

### L4 + L5 — Plugin Host, Skill/Agent Elevation, Workspace
- WP-L4-001: Platform + pack skill/agent loader (discover SKILL.md + .agent.md)
- WP-L4-002: Viewer registration contract + loader
- WP-L4-003: Generalize all 24 MATM agents + 17 FarmRTK platform skills (move stable ones out of imports/)
- WP-L4-010: ide-platform pack maturation (entrypoints for IDE process skills/agents)
- WP-L5-001: Workspace schema extensions (editor/viewer slots, skill modes, agent RRA)
- WP-L5-002: Workspace loader + validation used by router/gate/shell

**Primary imported patterns:** The entire set of 24+17+ assets (all must be processed via ide-structural-refactoring)  
**Key gates:** G1, G2, G4  
**Cross-layer deps:** Needs L2/L3 (things to load/enforce); feeds L7 (packs)

### L6 + L7 — Providers, Packs, Toolchains, GitHub
- WP-L6-001: GitHub provider (repos, Actions, PR evidence, gh CLI execution)
- WP-L6-010: Deep gh CLI skills (create PR with evidence, query lineage, trigger gate) — generalize repo-governance-autoflow-orchestrator
- WP-L7-001: engineering-sdlc pack generalization (beyond raw imports)
- WP-L7-002: threat-modeling pack as wrapper + graph viewer (retain A1–A9 as domain)
- WP-L7-003: Core toolchain plugins (python, powershell, node) + detection + templates
- WP-L7-010: ide-platform pack declared in example workspace + used for platform development

**Primary imported patterns:** repo-governance-autoflow-orchestrator + repo-audit-* + process-audit-* + kpi-drift-analyst; configuration-baseline + risk + validation + icd skills (as example flows)  
**Key gates:** G4 (merge), G5 (baseline)  
**Cross-layer deps:** Needs L3 (enforcement), L5 (declaration)

### Cross-Layer + L8 — Legacy, Docs, Overall Generalization (XGEN), Self-Hosting, Product Alignment
- WP-XGEN-001 … WP-XGEN-030+: Systematic generalization of every imported agent/skill (one or more per wave; tracked in Planning Agent portfolio)
- WP-XLEG-001: Legacy `src/` decision record + execution (legacy/ tree, extract useful pieces, update references)
- WP-XDOC-001: docs/archive/ creation + move of historical boards/duplicated governance + production of living IDE docs (how-to-add-*.md, ide-architecture.md, etc.)
- WP-XSELF-001: First self-hosting milestone (use current generalized skills + Planning/Refactoring Agents + Zed/Grok Build to execute a slice of this plan and pass G4)
- WP-XPACK-001: Packaging/bootstrap/test alignment (pyproject, Makefile targets for plan/skill invocation, platform health check)
- WP-XL8-001: External product workspace template + onboarding guide (L8 consumers)

**Primary imported patterns:** All remaining + legacy `src/agents/*`, `src/graphs/supervisor.py`, old docs, old scripts, etc.  
**Key gates:** G1, G4, G5 (especially self-hosting evidence and legacy decisions)  
**Cross-layer deps:** Touches every layer; must be carefully sequenced

---

## Layer Dependency Matrix (High-Level)

```
L0/L1 (Surfaces + Runtime)
  ↑ needs invocation & evidence
L2/L3 (Router + Gates)
  ↑ needs loadable units & context
L4/L5 (Host + Workspace)
  ↑ feeds packs & enforcement
L6/L7 (Providers + Packs)
  ↑ declared by
L5 (Workspace)
  ↑ enforced by
L3 (Gates)

Cross-Layer (XGEN / XLEG / XDOC / XSELF / XPACK)
  touches all layers — sequenced by Planning Agent as portfolio items
```

**Sequencing rules (Planning Agent):**
- Foundations (L2/L3 executor + basic gates + loader extensions) before heavy surface or pack work.
- First XGEN batch (the two new agents/skills we created) + XDOC archive + XLEG decision early.
- L0/L1 basics can proceed in parallel with L2/L3 once router can invoke skills.
- Bulk XGEN + full L0–L5 elevation in middle waves.
- L6/L7 + rich self-hosting + external L8 examples later.
- Ongoing XGEN, XSELF, and XDOC are portfolio items with drift tracking.

---

## Traceability Rules (enforced by Refactoring Agent)

For every work package and every generalized imported asset:
1. Link back to specific imported source (e.g. `multi-sprint-portfolio-planner.agent.md` + `orchestrate-farmrtk`).
2. Reference the layer(s) it primarily affects.
3. Declare or update architecture/design disposition with hierarchy metadata when the change is structural.
4. Ensure it participates in at least one gate (G0/G1/G2/G4/G5).
5. Register the result (agent in PLATFORM_AGENTS.md or pack; skill in loader / ide-platform pack; viewer in registry).
6. Produce evidence bundle suitable for G4 / independent review.

All of the above is executed via the procedure in `platform/skills/ide-structural-refactoring/SKILL.md` and sequenced via `ide-portfolio-planning`.

---

**How to use this index:**
- Planning Agent runs `ide-portfolio-planning` against a scope (e.g. "R1 wave: L2/L3 foundations + WP-XGEN-001..005 + WP-XDOC-001 + WP-XLEG-001").
- Refactoring Agent executes the scoped items using `ide-structural-refactoring`.
- Progress is tracked by updating this index + the master plan + evidence in the repo.

This index is intentionally lightweight and references the cohesive master plans for full context, rationale, and narrative:
- Layered details: [IDE_REFACTOR_PLAN.md](../IDE_REFACTOR_PLAN.md)
- High-level waves/epics (limited details): [AGENTIC_IDE_PROJECT_PLAN.md](../../project-plan/AGENTIC_IDE_PROJECT_PLAN.md)
- Reusability evaluation (driving XGEN): [REUSABILITY_EVALUATION_REPORT.md](../REUSABILITY_EVALUATION_REPORT.md)
- Detailed Wave 01 (R1): [WAVE_01_R1_FOUNDATIONS_DETAILED_PLAN.md](../../project-plan/WAVE_01_R1_FOUNDATIONS_DETAILED_PLAN.md)