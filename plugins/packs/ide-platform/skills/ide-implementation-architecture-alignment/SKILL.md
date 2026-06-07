---
name: ide-implementation-architecture-alignment
description: >
  Generalized skill for auditing implementation shape against approved architecture and design artifacts for the agentic IDE platform.
  Primary for Implementation Architecture Alignment Auditor. Generalizes implementation-architecture-alignment-auditor (MATM)
  and related assets. Critical for keeping implementation (generalized skills/agents, structure changes) aligned with architecture during generalization and self-hosted repo refactor.
metadata:
  short-description: "Implementation-architecture alignment audit for IDE layers, generalized assets, and structure"
  agent: ide-implementation-architecture-alignment-auditor
  gates: [G1_traceability, G2_icd_interfaces, G4_independent_review]
  maturity: M0+
---

# ide-implementation-architecture-alignment

**Agents:** Implementation Architecture Alignment Auditor (primary), Architecture/Design Disposition Planner and Change Author, Source-to-Evidence Traceability Auditor, Governance Policy Compiler, Refactoring Agent  
**Parent:** [ide-implementation-architecture-alignment-auditor.agent.md](../../../agents/ide-platform/ide-implementation-architecture-alignment-auditor.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)

## Purpose
Check whether implementation artifacts for the IDE (generalized SKILL.md/.agent.md in ide-platform, pack manifests, repo structure changes, supporting code/docs) conform to the approved architecture and design model (L0-L8 layers, editors/viewers for agents/skills as artifacts, functional decomp, self-hosting, etc.) and governance contracts. Identify drift, gaps, and mismatches.

This ensures that as we generalize the copied agents and execute the repo structure refactor, implementation stays aligned with the architecture (self-hosting the audit).

## When to Invoke
- During or after architecture/design disposition and change authoring for any IDE work or structural changes.
- Before/after generalization batches (XGEN) to ensure the new IDE-native versions align with the architecture.
- When planning or reviewing repo structure improvements or functional decomp.
- At G1 traceability, G2 interface contracts, G4 independent review, and before G5.
- User: "audit impl-arch alignment for the structure execution plan", "check generalized skills against layers", "/ide-impl-arch-alignment".

## Inputs
- Source implementation (generalized files in ide-platform, manifests, structure changes, scripts).
- Architecture and design artifacts (dispositions, layered IDE_REFACTOR_PLAN, hierarchy docs).
- Verification evidence under tests/ or evidence/.
- Independent review outputs.
- Current traceability matrix.

## Procedure

### 1. Map Implementation to Governing Architecture/Design
- Map implementation artifacts (e.g., moves in execution plan, updated manifests, generalized SKILL.md/.agent.md) to the governing architecture and design references (L0 editors for agents, L4 pack content, Cross structure, layer boundaries).
- Use explicit references from the active workpack or disposition.

### 2. Flag Gaps and Drift
- Flag implementation-only behavior that lacks an architecture/design anchor (e.g., structure changes without layer references).
- Flag architecture/design expectations that are not represented in the implementation (e.g., planned editor surfaces or pack content not reflected in moves).
- Record contract drift, boundary mismatches, and missing evidence legs.
- Validate that hierarchy fields (parent capability, child function, etc.) are respected in the implementation.

### 3. Report and Remediate
- Emit: Implementation-to-architecture alignment gaps, design-only concepts that need implementation follow-through, implementation-only artifacts lacking trace, remediation notes for governance closeout.
- Prioritize by severity (e.g., foundational L4 or structure changes), layer impact, and effect on self-hosting/editors.
- Recommendations should be actionable by Refactoring Agent and Disposition Planner.

### 4. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner or ACP)
pwsh -File tools/architecture/alignment-audit.ps1 -Scope "Structure-Refactor XGEN-Batch" -Disposition docs/ide-structure-architecture-disposition.md -Output evidence/impl-arch-alignment-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Impl-arch alignment gaps in IDE structure" --label architecture,alignment,ide-platform --body-file evidence/impl-arch-alignment-*.md
```

### 5. Support Iteration and Self-Hosting
- Re-audit as new architecture/designs or requirements emerge during execution.
- Use on the platform's own artifacts (e.g., the execution plan, generalized skills).
- The skill is self-referential and will audit its own generalization and the structure work.

## Outputs
- Implementation-to-architecture alignment gaps.
- Design-only concepts that need implementation follow-through.
- Implementation-only artifacts lacking architecture/design trace.
- Remediation notes for governance closeout.
- Evidence for G1, G2, G4.

## Guardrails
- Explicit references only — no inference.
- Local-first and file-referenced.
- Compatible with independent review reporting.

## Generalization & IDE-Specific Notes
- Removed product-specific contexts.
- Added explicit auditing for IDE model: alignment of agent/skill editors and viewers, pack content (ide-platform), layer decomposition (L0-L8), repo structure changes, hybrid orchestration, self-hosting (the platform audits its own implementation during generalization and refactor).
- Strong support for functional decomposition audits (ensuring implementation respects hierarchy for layers and structure).
- Designed to be used on the very changes that generalize the copied agents and improve the repo for the IDE.

## Related Platform Artifacts
- Gates: G1, G2 (new surface contracts), G4.
- Agents: Implementation Architecture Alignment Auditor (primary) + Disposition Planner and Change Author, Requirements, Traceability, Verification, Compliance agents, Refactoring Agent.
- Used in tight loop with ide-architecture-design-disposition, ide-architecture-design-change-author, and the execution of structural/generalization work. This skill is self-referential and will be used to audit the very changes that generalize the copied agents and improve the repo for the IDE.