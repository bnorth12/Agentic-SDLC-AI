---
name: ide-architecture-contract-enforcer
description: >
  Generalized skill for enforcing architecture and interface contract integrity against requirement and implementation changes for the agentic IDE platform.
  Primary for Architecture Contract Enforcer. Generalizes architecture-contract-enforcer (MATM) and related assets. Ensures contracts for layers, editors, viewers, agents/skills, and structure are upheld during generalization and self-hosted refactor.
metadata:
  short-description: "Architecture contract enforcement for IDE layers, generalized assets, and structure"
  agent: ide-architecture-contract-enforcer
  gates: [G1_traceability, G2_icd_interfaces, G4_independent_review]
  maturity: M0+
---

# ide-architecture-contract-enforcer

**Agents:** Architecture Contract Enforcer (primary), Architecture/Design Traceability Auditor, Disposition Planner, Source-to-Evidence Traceability Auditor, Refactoring Agent  
**Parent:** [ide-architecture-contract-enforcer.agent.md](../../../agents/ide-platform/ide-architecture-contract-enforcer.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · Structural Refactor Execution Plan

## Purpose
Ensure architecture and design artifacts remain authoritative and aligned with requirement and implementation intent for the IDE (generalized agents/skills in ide-platform, structure changes, layer decomp, self-hosting). This supports the prioritized procedures and the repo refactor by enforcing contracts.

## When to Invoke
- During or after architecture/design disposition and traceability audits for IDE work or structure changes.
- Before/after generalization to ensure contracts for new IDE-native versions.
- When reviewing repo structure or functional decomp.
- At G1, G2, G4 gates.
- User: "enforce contracts for the structure execution plan", "check contracts for generalized skills", "/ide-arch-contract-enforce".

## Inputs
- docs/architecture/, docs/design/, Requirements/.
- Generalized artifacts in ide-platform, manifests, structure change records, baselines, dispositions.

## Procedure

### 1. Evaluate Requirement-to-Architecture/Design Traceability Coverage
- For the scope (e.g., structure refactor, XGEN batch), evaluate coverage of requirement-to-architecture/design traceability.
- Use the layered plans, baselines, and dispositions as reference.

### 2. Detect Missing or Stale Interface Contract Mappings
- Detect missing or stale interface contract mappings (e.g., for agent/skill editors, pack manifests, layer boundaries).
- Flag as-built work that lacks architecture/design trace evidence (e.g., generalized files or structure moves without references).

### 3. Classify Conceptual-Versus-As-Built Mismatch Risks
- Classify risks (e.g., conceptual debt vs. active regressions in the structure or generalization).
- Prioritize by severity for the execution plan.

### 4. Emit Findings
- Contract integrity findings and traceability gaps.
- Merge gate recommendation by severity/profile (e.g., block in strict mode for platform core).
- Recommendations for updates to the execution plan or generalized artifacts.

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner or ACP)
pwsh -File tools/architecture/contract-enforce.ps1 -Scope "Structure-Refactor XGEN-Batch" -Baseline docs/ide-structure-requirements-baseline.md -Output evidence/arch-contract-enforce-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Contract enforcement findings for IDE structure" --label architecture,compliance,ide-platform --body-file evidence/arch-contract-enforce-*.md
```

### 6. Support Iteration and Self-Hosting
- Re-enforce after changes or redlines.
- The skill is self-referential: enforce contracts for the generalized skills and the structure work.
- Use to keep the platform's architecture coherent during the refactor.

## Outputs
- Contract integrity findings and traceability gaps.
- Merge gate recommendation by severity/profile.
- Evidence for G1, G2, G4.

## Guardrails
- Treat architecture docs as source-of-truth contracts.
- Escalate missing traceability.
- Require explicit references.

## Generalization & IDE-Specific Notes
- Removed product-specific.
- Added enforcement for IDE model: contracts for agent/skill editors and viewers, pack content, layer decomp, repo structure, self-hosting.
- Strong support for the structure refactor and generalization (enforcing contracts during moves and updates).
- Designed to be used on the contracts for the generalized agents and the structure changes.

## Related Platform Artifacts
- Gates: G1, G2, G4.
- Agents: Architecture Contract Enforcer (primary) + Traceability Auditor, Disposition Planner, Refactoring Agent.
- Used with ide-architecture-design-traceability and the execution of structural work. This skill is self-referential and will enforce contracts for the changes that generalize the copied agents and improve the repo for the IDE.