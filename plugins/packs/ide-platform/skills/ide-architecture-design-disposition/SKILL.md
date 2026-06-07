---
name: ide-architecture-design-disposition
description: >
  Generalized skill for forcing explicit architecture/design disposition decisions with hierarchy metadata
  on any significant IDE work (new editors/viewers, generalized agents/skills, packs, repo structure changes,
  functional decomposition of layers). Must be used before implementation or generalization proceeds.
  Primary for Architecture/Design Disposition Planner.
metadata:
  short-description: "Architecture/design disposition with hierarchy for IDE layers, surfaces, and structural work"
  agent: architecture-design-disposition-planner
  gates: [G1_traceability, G2_icd_interfaces, G4_independent_review]
  maturity: M0+
---

# ide-architecture-design-disposition

**Agents:** Architecture/Design Disposition Planner (primary), Requirements Baseline Steward, Implementation Architecture Alignment Auditor, Refactoring Agent, Planning Agent  
**Parent:** [architecture-design-disposition-planner.agent.md](../../../agents/ide-platform/architecture-design-disposition-planner.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)

## Purpose
Ensure that requirements, architecture/design, implementation, and verification remain synchronized for every meaningful piece of work on the agentic IDE. This skill forces an explicit disposition decision (update architecture to match implementation, or implementation to match architecture) with full hierarchy metadata before any generalization, coding, or structural change is considered "done."

It is especially critical while the IDE's own architecture (L0-L8 layers, editors for agents/skills, viewers, pack model, repo structure, self-hosting) is still being discovered and refined.

## When to Invoke
- Before generalizing any imported agent or skill into the platform or ide-platform pack.
- Before implementing or changing any editor, viewer, orchestration behavior, gate, pack manifest, or repo structure.
- When execution reveals that current architecture no longer matches emerging understanding or requirements.
- At architecture reviews or before G2/G4 gates on significant work.
- User: "disposition the agent editor surface", "architecture decision on repo structure refactor", "/ide-architecture-disposition".

## Inputs
- Requirements baseline and hierarchy metadata (from ide-requirements-baseline).
- Current layered architecture documentation and gate registry.
- Proposed change or work package (generalization target, new surface, structural refactor, functional decomposition).
- Existing implementation or sketches.
- Traceability and compliance context.

## Procedure

### 1. Build the Workpack
- Explicitly list for the slice:
  - Requirement IDs (from baseline).
  - Architecture/Design targets (current L0-L8 view or proposed update).
  - Implementation targets (files, packs, manifests, code, generalized SKILL.md/.agent.md).
  - Verification targets/methods.
- Require complete hierarchy metadata on every item: parent capability, child function, decomposition level, allocated component/module, verification method.

### 2. Analyze Alignment
- Compare the four legs (requirements, architecture/design, implementation, verification).
- Identify gaps, mismatches, or orphans.
- For repo structure or functional decomposition work: explicitly assess fit to the IDE model (agents/skills as editable artifacts, packs as primary delivery, gates as enforcement, self-hosting).

### 3. Force Disposition Decision
Require a single, recorded choice:
- Path A: Update architecture/design (and associated docs, gate entries, pack manifests) to match the proposed or discovered implementation.
- Path B: Update implementation (or proposed change) to match the approved architecture/design.
- Record rationale, trade-offs, and any temporary exceptions with expiration.

### 4. Produce Disposition Artifacts
- Updated architecture/design workpack with hierarchy.
- Disposition decision record (suitable for ADR or gate evidence).
- Clear directives for the Refactoring Agent, implementers, or generalizers.
- Gap list for verification and compliance follow-up.

### 5. Compliance & Traceability Check
- Verify the disposition does not violate current policies (governance-policy-compiler) or layer boundaries.
- Ensure full source-to-evidence traceability is preserved or improved.

### 6. PowerShell / GitHub Native Emphasis
```powershell
# Example (to be turned into reusable fragments)
pwsh -File tools/architecture/disposition.ps1 -WorkItem "Generalize requirements-baseline-steward + add agent editor surface" -Scope "L0-Editors L4-PluginHost Cross-Structure"

gh issue create --title "Disposition: Agent definition editor surface" --label architecture,ide-platform --body "See attached disposition record..."
```

## Outputs
- Architecture/design workpack with complete hierarchy metadata.
- Disposition decision record with rationale and approval evidence.
- Updated architecture artifacts or change directives.
- Verified traceability and gap list for verification agents.

## Escalation
- Inability to choose a clean disposition path (architecture too immature) → Planning Agent for limited exploration wave + mandatory follow-up disposition.
- Disposition that would weaken compliance or layer integrity → Governance Policy Compiler + Independent Review (G4).
- Large structural implications (e.g., repo reorg) → Refactoring Agent + full review.

## Generalization & IDE-Specific Notes
- Removed all product-specific assumptions (MATM threat pipelines, FarmRTK hardware).
- Added strong support for the IDE's own model: first-class editing of agents and skills, viewer contracts, pack-based delivery, hybrid orchestration, PowerShell + GitHub as native, functional decomposition of L0-L8, and self-hosting (the platform's architecture is developed using the same discipline).
- Explicitly designed to be used on repo structure improvements and iterative architecture discovery.

## Related Platform Artifacts
- Gates: G1, G2 (new surface contracts), G4.
- Agents: Architecture/Design Disposition Planner (primary), Requirements Baseline Steward, Compliance and Verification agents, Refactoring Agent.
- Used heavily in XGEN (generalization) and structural refactor work packages.