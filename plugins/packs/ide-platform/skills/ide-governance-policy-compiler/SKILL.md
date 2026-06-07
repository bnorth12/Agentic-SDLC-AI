---
name: ide-governance-policy-compiler
description: >
  Generalized skill for compiling policy profiles and layer/context rules into enforceable governance
  for the agentic IDE, with strong support for self-hosting, repo structure, agent/skill development,
  and compliance during iterative architecture discovery.
metadata:
  short-description: "Policy compilation and enforcement for IDE layers, self-hosting, and structural work"
  agent: governance-policy-compiler
  gates: [G1_traceability, G4_independent_review]
  maturity: M0+
---

# ide-governance-policy-compiler

**Agents:** Governance Policy Compiler (primary), Requirements Baseline Steward, Architecture/Design Disposition Planner, Independent Review Committee, Refactoring Agent  
**Parent:** [governance-policy-compiler.agent.md](../../../agents/ide-platform/governance-policy-compiler.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)

## Purpose
Compile and enforce the policies that govern development of the agentic IDE itself (including the repo structure, generalization of process capabilities, creation of editors/viewers for agents/skills, and self-hosting). This skill ensures we stay compliant with our own plans while the architecture is still maturing.

## When to Invoke
- Before structural refactors, large XGEN tranches, or changes to platform core layers.
- When assessing compliance of proposed work against current policies and the layered model.
- As part of intake or before verification.

## Procedure (High-Level)
1. Validate policy schema and thresholds for IDE context (strict for core layers and repo structure).
2. Compile routing rules for planning, disposition, generalization, structural change, merge, and self-hosting.
3. Detect conflicts or layer violations.
4. Emit policy status report + enforcement directives.
5. Support updates as better architecture emerges (tie to disposition planner).

## IDE-Specific Notes
- Strong emphasis on self-hosting policies (the rules we use to build the IDE must themselves be enforceable inside the IDE).
- Layer-aware and functional-decomposition-aware policies.
- PowerShell + GitHub native enforcement examples.

## Related
- Used heavily alongside ide-requirements-baseline and ide-architecture-design-disposition in early waves.
- Feeds independent review and verification planning.