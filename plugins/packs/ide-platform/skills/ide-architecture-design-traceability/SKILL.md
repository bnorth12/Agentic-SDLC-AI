---
name: ide-architecture-design-traceability
description: >
  Generalized skill for auditing architecture/design traceability alignment from requirements through implementation and verification for the agentic IDE platform.
  Primary for Architecture/Design Traceability Auditor. Generalizes architecture-design-traceability-auditor (MATM)
  and related assets. Critical for ensuring Requirements, Arch/Design, and structure changes have full chains during generalization and self-hosted repo refactor.
metadata:
  short-description: "Architecture/design traceability audit for IDE layers, surfaces, generalized assets, and structure"
  agent: ide-architecture-design-traceability-auditor
  gates: [G1_traceability, G2_icd_interfaces, G4_independent_review]
  maturity: M0+
---

# ide-architecture-design-traceability

**Agents:** Architecture/Design Traceability Auditor (primary), Requirements Baseline Steward, Architecture/Design Disposition Planner, Source-to-Evidence Traceability Auditor, Refactoring Agent  
**Parent:** [ide-architecture-design-traceability-auditor.agent.md](../../../agents/ide-platform/ide-architecture-design-traceability-auditor.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)

## Purpose
Audit whether the architecture and design framework for the IDE (L0 editors/viewers, L2 orchestration, L4 plugin host for skills/agents as artifacts, L7 packs, Cross-layer repo structure and functional decomp) fully supports the requirement shape, implementation approach (generalized agents/skills, structure changes), and verification plan. Identify concept-only gaps, as-built without backing, and hierarchy issues.

This ensures that as we generalize the copied agents into IDE-native versions and refactor the repo, the architecture stays traceable and aligned (self-hosting the audit).

## When to Invoke
- During or after requirements baselining and architecture/design disposition for IDE work or structural changes.
- Before/after generalization batches (XGEN) to ensure the new IDE-native versions have full traceability to layers and surfaces.
- When planning or reviewing repo structure improvements or functional decomp of L0-L8.
- At G1 traceability gates, G2 interface contracts, and before G4/G5.
- User: "audit arch/design traceability for the structure execution plan", "check chains for generalized skills", "/ide-arch-design-traceability".

## Inputs
- Requirements baselines with hierarchy metadata.
- Architecture and design docs (layered IDE_REFACTOR_PLAN, dispositions, etc.).
- Implementation artifacts (generalized SKILL.md/.agent.md in ide-platform, manifests, structure changes, code).
- Verification evidence and plans.
- Current traceability matrix and root hierarchy artifacts.

## Procedure

### 1. Identify Requirement/Work Item Traceability
- Inventory the scope (e.g., requirements for IDE structure, a batch of generalized agents/skills, or specific work packages in the execution plan).
- Identify which have architecture/design references (e.g., to L0 editors for agents, L4 pack content, Cross structure).

### 2. Separate Concept vs. As-Built
- Separate concept-only planned items (e.g., new viewer for evidence graphs, editor for .agent.md) from as-built implementation.
- Flag implementation (generalized files, pack manifests, directory moves for structure) that lacks architecture/design references.
- Highlight gaps where implementation shape does not match the documented design framework (e.g., layer boundaries, agent/skill artifact model).

### 3. Validate Hierarchy and Allocation
- For each requirement/work item, verify explicit parent capability ID, child function ID, decomposition level (L0/L1/L2), allocated component/module (e.g., plugins/packs/ide-platform/, gui/editors/), and verification method are present.
- Do not infer from prefixes or locations.

### 4. Report and Remediate
- Emit: IDs missing architecture/design traceability, concept-vs-as-built gap list, implementation-shape mismatch notes, hierarchy field coverage summary, iteration recommendations for design updates.
- Prioritize by severity (e.g., foundational L4 plugin host or structure changes), layer impact, and effect on self-hosting/editors.
- Recommendations should be actionable by Disposition Planner and Refactoring Agent.

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner or ACP)
pwsh -File tools/architecture/traceability-audit.ps1 -Scope "Structure-Refactor XGEN-Batch" -Baseline docs/ide-structure-requirements-baseline.md -Output evidence/arch-design-traceability-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Arch/design traceability gaps in IDE structure" --label architecture,traceability,ide-platform --body-file evidence/arch-design-traceability-*.md
```

### 6. Support Iteration and Self-Hosting
- Re-audit as new architecture/designs or requirements emerge during execution (common in early IDE development).
- Use on the platform's own artifacts (e.g., the execution plan itself, generalized skills).
- The skill is self-referential and will audit its own generalization and the structure work.

## Outputs
- Requirement/work item IDs missing architecture/design traceability.
- Concept-vs-as-built gap list.
- Implementation-shape mismatch notes.
- Hierarchy field coverage summary and missing-field list.
- Iteration recommendations for design updates.
- Evidence for G1, G2, G4.

## Guardrails
- Explicit references only — no inference.
- Local-first and file-referenced.
- Compatible with independent review reporting.

## Generalization & IDE-Specific Notes
- Removed product-specific paths and contexts (e.g., FarmRTK/MATM docs).
- Added explicit auditing for IDE model: traceability of agent/skill editors and viewers, pack content (ide-platform), layer decomposition (L0-L8), repo structure as architecture subject, hybrid orchestration, self-hosting (the platform audits its own architecture during generalization and refactor).
- Strong support for functional decomposition audits (ensuring hierarchy is consistent across requirements, design, implementation, verification for the structure changes and generalized agents).

## Related Platform Artifacts
- Gates: G1, G2 (new surface contracts), G4.
- Agents: Architecture/Design Traceability Auditor (primary) + Disposition Planner, Requirements, Traceability, Verification, Compliance agents, Refactoring Agent.
- Used in tight loop with ide-requirements-baseline, ide-architecture-design-disposition, and the execution of structural/generalization work. This skill is self-referential and will be used to audit the very changes that generalize the copied agents and improve the repo for the IDE.