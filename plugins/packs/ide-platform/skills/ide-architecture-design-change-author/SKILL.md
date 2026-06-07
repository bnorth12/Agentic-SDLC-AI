---
name: ide-architecture-design-change-author
description: >
  Generalized skill for authoring concrete architecture/design updates that stay synchronized with implementation and verification for the agentic IDE platform.
  Primary for Architecture/Design Change Author. Generalizes architecture-design-change-author (MATM)
  and related assets. Used during generalization, structural refactors, and surface development to keep the IDE's own architecture current (self-hosting).
metadata:
  short-description: "Architecture/design change authoring with hierarchy for IDE layers, generalized assets, and structure"
  agent: architecture-design-change-author
  gates: [G1_traceability, G2_icd_interfaces, G4_independent_review]
  maturity: M0+
---

# ide-architecture-design-change-author

**Agents:** Architecture/Design Change Author (primary), Architecture/Design Disposition Planner, Requirements Baseline Steward, Source-to-Evidence Traceability Auditor, Refactoring Agent  
**Parent:** [architecture-design-change-author.agent.md](../../../agents/ide-platform/architecture-design-change-author.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)

## Purpose
Author specific, concrete architecture and design updates for any work on the IDE (generalization of copied agents into native versions, repo structure changes, new editors/viewers for agents/skills, pack updates, functional decomposition of layers). Keep implementation targets (files, manifests, moves, code) and verification targets synchronized with those updates, using explicit hierarchy metadata.

This skill is the "authoring" counterpart to disposition — it produces the actual architecture/design deltas that the Refactoring Agent and implementers execute, while ensuring the IDE's own architecture (L0-L8, self-hosting, agents/skills as artifacts) stays coherent.

## When to Invoke
- After architecture/design disposition when concrete updates are needed.
- During generalization (XGEN) of imported assets to author the IDE-native architecture for the new versions (e.g., how a generalized skill fits into L4 plugin host and L7 packs).
- When executing structural refactors (e.g., authoring the architecture for the new repo layout that supports editors for .agent.md/SKILL.md).
- Before closing changes that affect architecture or verification (G2/G4).
- User: "author architecture updates for the structure execution plan", "design the agent editor surface contract", "/ide-architecture-change-author".

## Inputs
- Active workpack or disposition (with requirements and hierarchy).
- Current architecture/design docs and layer descriptions.
- Proposed changes (generalization targets, structure moves, new surface contracts, functional decomp updates).
- Existing implementation sketches and verification plans.

## Procedure

### 1. Identify Required Updates from Workpack
- Review the scope (e.g., "move generalized content to ide-platform pack, quarantine legacy, support L0 editors for agents/skills").
- Identify specific architecture/design elements that need updating or new authoring:
  - Layer descriptions (e.g., update L4 for pack-local skills/agents, L0 for editor contracts).
  - Contracts and interfaces (e.g., SKILL.md/.agent.md as first-class artifacts, viewer registrations, pack manifest schema extensions).
  - Hierarchy for the changes themselves (parent capability, child function, etc.).
  - Self-hosting implications (the platform must be able to edit its own architecture artifacts using the IDE surfaces).

### 2. Author the Updates with Full Hierarchy
- Produce updated or new architecture/design workpack entries.
- For every slice, include complete hierarchy metadata: parent capability, child function, decomposition level, allocated component/module, verification method.
- Synchronize with implementation (what files/manifests/code will change) and verification (how we will prove the update works, e.g., "editor can load and preview a generalized .agent.md from ide-platform").

### 3. Keep Legs Synchronized
- Ensure implementation targets (e.g., the moves in the execution plan, updates to manifests) match the authored architecture.
- Ensure verification targets (e.g., tests for new editor behavior, compliance audit of the new layout) are defined and linked.
- Flag any gaps (e.g., "architecture for L7 pack content updated, but verification for self-hosting editor not yet defined").

### 4. Produce Execution-Ready Artifacts
- Updated architecture/design authoring workpack.
- Gap list for missing architecture/design, implementation, or verification legs.
- Execution-ready disposition checklist (tie back to the disposition planner).
- Recommendations for how the changes support functional decomp and the overall IDE vision.

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (future skill runner or ACP)
pwsh -File tools/architecture/author-change.ps1 -Workpack "Structure-Refactor-Execution" -Scope "L4-PluginHost L0-Editors Cross-Structure" -Output evidence/architecture-change-author-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Architecture updates for IDE repo structure" --label architecture,ide-platform --body-file evidence/architecture-change-author-*.md
```

### 6. Support Iteration and Self-Hosting
- Re-author as new requirements or designs emerge during execution.
- The authored updates themselves must be traceable and reviewable (self-referential).

## Outputs
- Updated architecture/design workpack entries with hierarchy.
- Synchronized implementation and verification targets.
- Gap list and execution-ready checklist.
- Evidence for G1, G2, G4.

## Escalation
- Inability to keep legs synchronized → Architecture/Design Disposition Planner for re-disposition + Planning Agent for wave impact.
- Gaps that affect compliance or verification → Governance Policy Compiler + Verification Coverage Planner + Independent Review (G4).

## Generalization & IDE-Specific Notes
- Removed product-specific remediation contexts.
- Strong focus on authoring for the IDE's own model: first-class editing of agents/skills (.agent.md/SKILL.md as architecture subjects), pack content (ide-platform as the living example), layer decomposition (L0-L8), repo structure as architecture, self-hosting (the platform authors its own architecture updates using the tools it is building).
- Explicitly supports authoring the changes that generalize the copied agents and make the repo a clean IDE workspace.

## Related Platform Artifacts
- Gates: G1, G2, G4.
- Agents: Architecture/Design Change Author (primary) + Disposition Planner, Requirements, Traceability, Verification, Compliance agents, Refactoring Agent.
- Used in tight loop with ide-architecture-design-disposition and the execution of structural/generalization work. This skill is self-referential and will author the architecture for its own generalization and the repo layout that hosts it.