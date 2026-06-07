---
name: ide-hierarchy-taxonomy-steward
description: >
  Generalized skill for enforcing stable L0-L8 + Cross functional decomposition and hierarchy taxonomy
  for the agentic IDE platform. Primary for IDE Hierarchy Taxonomy Steward.
  Generalizes hierarchy-taxonomy-steward (MATM) + hierarchy-conformance-auditor patterns.
  Essential for all generalization (XGEN), structural reorganization, and self-hosting work.
metadata:
  short-description: "L0-L8 layer taxonomy, functional decomp, and hierarchy conformance for IDE agents, skills, plans, and structure"
  agent: ide-hierarchy-taxonomy-steward
  gates: [G1_traceability, G2_icd_interfaces, G4_independent_review, G5_baseline]
  maturity: M0+
# P1 tool registry + permission/scoping declaration (L2/L4; executor captures for evidence; dual-use PS + future GUI)
tools:
  - validate_hierarchy_metadata
  - read_ide_artifact
required_scopes:
  - ide.hierarchy
  - ide.fs.read
---

# ide-hierarchy-taxonomy-steward

**Agents:** IDE Hierarchy Taxonomy Steward (primary), Refactoring Agent, Architecture/Design Disposition Planner, Source-to-Evidence Traceability Auditor, Planning Agent  
**Parent:** [ide-hierarchy-taxonomy-steward.agent.md](../../../agents/ide-platform/ide-hierarchy-taxonomy-steward.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · [FRAMEWORK_DECOMPOSITION.md](../../../docs/charter/FRAMEWORK_DECOMPOSITION.md) · `agents/platform/invocations/remaining-xgen-refactoring-session.md`

## Purpose
Enforce and maintain a stable, auditable hierarchy taxonomy and functional decomposition (L0 GUI/Editors → L1 Runtime → L2 Orchestration → L3 Gates → L4 Plugin Host → L5 Workspace → L6 Providers → L7 Packs → L8+Cross) across every generalized agent, skill, work package, plan, structural change, and self-hosted governance artifact for the agentic IDE. This skill ensures that as we complete the remaining XGEN (MATM pending + FarmRTK) and continue IDE integration, all new first-class artifacts (.agent.md, SKILL.md in packs) and repo changes carry consistent, traceable decomposition metadata that supports editors, viewers, loading, and governance.

## When to Invoke
- During Phase 1 generalization of any remaining imported agents/skills (this tranche).
- Before/after structural content moves, legacy quarantine, or doc archive actions (Phase 2 of ide-structural-refactoring).
- When authoring or reviewing work packages in the layer index or execution plans.
- At G1 traceability checkpoints, G2 interface contract reviews for new surfaces, G4 independent review of XGEN or structural work, and before G5 baselines.
- User: "validate hierarchy for the remaining XGEN and FarmRTK batch", "enforce L0-L8 taxonomy on generalized agents/skills", "/ide-hierarchy-check".
- As a mandatory supporting step inside ide-structural-refactoring (Phases 1 and 3) and during self-hosting loops.

## Inputs
- Current layered architecture and decomposition (FRAMEWORK_DECOMPOSITION.md, IDE_REFACTOR_PLAN.md, LAYER_WORK_PACKAGE_INDEX.md).
- Generalized .agent.md and SKILL.md files (new and existing in ide-platform).
- Work packages, tranche plans, invocation records, and structural execution artifacts.
- Prior requirements baselines and architecture dispositions that contain hierarchy metadata.
- Current ide-platform manifest and pack structure.

## Procedure

### 1. Inventory Scope and Current Taxonomy
- Build inventory of items in scope for this pass (e.g., the 5 pending MATM agents + associated skills + priority FarmRTK items from the remaining XGEN tranche).
- For each, extract or assign:
  - Parent Capability (e.g., "L4 Plugin Host - Pack Content" or "Cross XGEN - Agent/Skill Generalization")
  - Parent Function
  - Child Function (the specific generalized artifact or structural change)
  - Decomposition Level (2–4 typical for XGEN items)
  - Allocated Component/Module (e.g., plugins/packs/ide-platform/agents/ide-xxx.agent.md)
  - Verification Method (traceability audit + policy compliance + re-audit by this skill + G4 evidence)

### 2. Validate and Normalize Hierarchy Fields
- Confirm consistency of identifiers and naming across parent/child (stable at portfolio/layer level for parents; executable slices for children).
- Validate fan-out is intentional (one parent capability normally maps to multiple child functions over tranches).
- Flag and normalize any drift (inconsistent layer tagging, missing fields on new generalized items, drift between the plan and the actual file placement in the pack).

### 3. Enforce IDE Surface and Self-Hosting Rules
- Every generalized agent/skill must declare explicit support for IDE surfaces: editable as .agent.md / SKILL.md in future editors, viewable in evidence/graph viewers, discoverable via pack loader, invocable via hybrid orchestration.
- Self-hosting check: the hierarchy for this item must be traceable back to the IDE vision (agents/skills as first-class, L0-L8 separation, PowerShell + GitHub native, thin platform + rich ide-platform pack).
- Record any violations as remediation items with file references.

### 4. Produce Report + Remediation
- Output a hierarchy conformance report with severity-ranked findings and explicit references.
- Produce normalized metadata fragments ready to be applied to the generalized artifacts or plans.
- Generate prioritized remediation backlog (e.g., "add full hierarchy section to ide-xxx.agent.md and update the layer index entry").

### 5. PowerShell / GitHub Native Steps
```powershell
# Example (future runner or ACP)
pwsh -File tools/hierarchy/validate-ide-taxonomy.ps1 -Scope "Remaining-XGEN-MATM-5 + FarmRTK-Audit-Batch" -LayerIndex docs/charter/ide-refactor/LAYER_WORK_PACKAGE_INDEX.md -TargetPack plugins/packs/ide-platform -Output evidence/hierarchy-taxonomy-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Hierarchy drift in remaining XGEN tranche" --label hierarchy,xgen,ide-platform --body-file evidence/hierarchy-taxonomy-*.md
```

### 6. Close the Loop (Self-Hosting)
- Re-run on the updated artifacts after remediation.
- Feed results into the Refactoring Agent for Phase 3 disposition and into the Planning Agent for portfolio balance.
- Update this skill and the owning agent with lessons (self-referential).

## Outputs
- Hierarchy conformance report with explicit file and WP references.
- Normalized hierarchy metadata ready for application.
- Prioritized remediation backlog mapped to generalized artifacts and work packages.
- Evidence suitable for G1/G2/G4 (including self-hosting chains).

## Guardrails
- Do not edit runtime implementation during taxonomy passes — only metadata, recommendations, and reports.
- Keep all updates local-first and deterministic.
- Treat taxonomy drift as governance debt requiring explicit work items.

## Generalization & IDE-Specific Notes
- Original MATM skill (focused on sprint issue artifacts and old planning/ paths) generalized to the full IDE layered model, work package system (WP-Lx / WP-X*), generalized pack content (ide-platform as the home for platform process agents/skills), and self-hosting of the reboot.
- All product-specific assumptions removed.
- Explicit support for the current remaining XGEN tranche and the structural-refactor-execution-plan.md.
- Designed to be used on the very artifacts it helps create (this skill, the new ide-* agents, the invocation record).

## Related Platform Artifacts
- Gates: G1, G2, G4, G5.
- Agents: IDE Hierarchy Taxonomy Steward (primary), Refactoring Agent, Architecture/Design agents, Traceability Auditor.
- Used heavily by ide-structural-refactoring (Phases 1 & 3) and in the layer work package index.
- Future: Integrated with hierarchy viewers and agent/skill editors that surface decomposition.