---
name: ide-architecture-document-surface-enforcer
description: >
  Generalized skill for enforcing required architecture and design document surfaces for governed review contexts in the agentic IDE platform.
  Primary for Architecture Document Surface Enforcer. Generalizes architecture-document-surface-enforcer (MATM)
  and related assets. Ensures docs for layers, editors, viewers, agents/skills, packs, and structure are present and referenced during generalization and self-hosted refactor.
metadata:
  short-description: "Architecture document surface enforcement for IDE layers, surfaces, generalized assets, and structure"
  agent: ide-architecture-document-surface-enforcer
  gates: [G1_traceability, G2_icd_interfaces, G4_independent_review]
  maturity: M0+
---

# ide-architecture-document-surface-enforcer

**Agents:** Architecture Document Surface Enforcer (primary), Architecture/Design Traceability Auditor, Disposition Planner, Source-to-Evidence Traceability Auditor, Refactoring Agent  
**Parent:** [ide-architecture-document-surface-enforcer.agent.md](../../../agents/ide-platform/ide-architecture-document-surface-enforcer.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)

## Purpose
Enforce that required architecture and design document surfaces (for L0 editors/viewers, L2 orchestration, L4 plugin host for skills/agents as artifacts, L7 packs, Cross-layer repo structure and functional decomp) are present, referenced, and current in governed review contexts. This supports traceability, compliance, and the ability to develop the IDE (self-hosting the enforcement).

## When to Invoke
- During architecture/design disposition and traceability audits for IDE work or structure changes.
- Before/after generalization to ensure docs for new IDE-native versions are in place and referenced.
- When reviewing repo structure or functional decomp.
- At G1, G2, G4 gates.
- User: "enforce document surfaces for the structure execution plan", "check docs for generalized skills", "/ide-arch-document-surface".

## Inputs
- Architecture and design docs (layered plans, dispositions, hierarchy).
- Traceability, review, and disposition artifacts.
- Generalized skills/agents, manifests, structure change records.
- Requirements baselines, verification plans.

## Procedure

### 1. Identify Required Document Surfaces
- For the scope (e.g., structure refactor, XGEN batch), list required architecture/design document families (e.g., layer definitions, editor contracts for agents/skills, pack manifest examples, structure change records, functional decomp docs).
- Cross-reference with the layered IDE_REFACTOR_PLAN and dispositions.

### 2. Verify Presence, References, and Currency
- Confirm the surfaces are present in the expected locations (e.g., under docs/ or in ide-platform).
- Verify they are explicitly referenced from the relevant traceability, review, disposition, and implementation artifacts (e.g., from the execution plan, generalized SKILL.md).
- Check for staleness (e.g., outdated layer descriptions after structure changes) or orphaned surfaces (not referenced in current work).

### 3. Flag Gaps and Issues
- Report missing, stale, or orphaned surfaces with clear context (e.g., "No editor contract doc for agent definitions in L0, referenced in execution plan but missing in ide-platform").
- Validate that surfaces support hierarchy and functional decomp (e.g., docs reference parent/child for layers).
- For structure work: ensure docs for the new layout enable editing agents/skills as artifacts and viewing evidence.

### 4. Recommend Updates
- Prioritized remediation for the Disposition Planner and Refactoring Agent (e.g., "Author/update L0 editor contract doc and reference in structure plan and generalized skills").
- Tie to self-hosting: surfaces that the platform can use to govern its own development.

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner or ACP)
pwsh -File tools/architecture/document-surface-enforce.ps1 -Scope "Structure-Refactor XGEN-Batch" -Baseline docs/ide-structure-requirements-baseline.md -Output evidence/arch-document-surface-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Missing document surfaces for IDE structure" --label architecture,docs,ide-platform --body-file evidence/arch-document-surface-*.md
```

### 6. Support Iteration and Self-Hosting
- Re-enforce as architecture evolves during execution.
- Use on the platform's own docs (e.g., the execution plan, generalized agent docs).
- The skill is self-referential and will enforce surfaces for its own generalization and the structure work.

## Outputs
- List of missing/stale/orphaned surfaces with context.
- Recommendations for updates.
- Hierarchy conformance notes.
- Evidence for G1, G2, G4.

## Guardrails
- Explicit references only.
- Local-first.
- Compatible with independent review.

## Generalization & IDE-Specific Notes
- Removed product-specific docs.
- Added enforcement for IDE model: surfaces for agent/skill editors and viewers, pack content, layer decomp (L0-L8), repo structure, self-hosting (docs that support editing the platform's own agents/skills during refactor).
- Strong support for ensuring surfaces enable functional decomp and the IDE vision.

## Related Platform Artifacts
- Gates: G1, G2, G4.
- Agents: Architecture Document Surface Enforcer (primary) + Traceability Auditor, Disposition Planner, Refactoring Agent.
- Used with ide-architecture-design-traceability and the execution of structural work. This skill is self-referential and will enforce docs for the changes that generalize the copied agents and improve the repo for the IDE.