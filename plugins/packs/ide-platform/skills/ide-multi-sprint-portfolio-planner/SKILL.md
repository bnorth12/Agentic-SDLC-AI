---
name: ide-multi-sprint-portfolio-planner
description: >
  Generalized skill for planning and staging multiple waves/sprints into a dependency-aware governance portfolio for the agentic IDE platform.
  Primary for Multi-Sprint Portfolio Planner. Generalizes multi-sprint-portfolio-planner (MATM) and related assets. Balances architecture runway, verification, generalization, and structure work across the reboot phases.
metadata:
  short-description: "Multi-wave portfolio planning for IDE generalization, structure, and governance"
  agent: ide-multi-sprint-portfolio-planner
  gates: [G0_wave_charter, G1_traceability, G4_independent_review]
  maturity: M0+
---

# ide-multi-sprint-portfolio-planner

**Agents:** Multi-Sprint Portfolio Planner (primary), Planning Agent, Refactoring Agent, Requirements Baseline Steward, Architecture/Design Traceability Auditor, Verification Coverage Planner, Governance Policy Compiler  
**Parent:** [ide-multi-sprint-portfolio-planner.agent.md](../../../agents/ide-platform/ide-multi-sprint-portfolio-planner.agent.md) (generalized, to be created) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · Structural Refactor Execution Plan

## Purpose
Build a governed multi-wave structure that balances capability delivery (generalized agents/skills in ide-platform), system integrity (repo structure, layers), architecture runway, verification load, and governance checkpoints across the reboot phases (R1 foundations, elevation, etc.).

This provides the portfolio-level planning to sequence the XGEN and structure work without overloading any wave, while keeping dependency realism.

## When to Invoke
- At the start of major phases or when re-planning the portfolio (e.g., after redlines in structure work).
- To balance the remaining generalization with structure execution and verification.
- User: "plan the portfolio for the remaining XGEN and structure", "/ide-multi-sprint-portfolio".

## Inputs
- Wave plans and roadmap artifacts (from IDE_REFACTOR_PLAN, execution plan, WAVE_01).
- Architecture/design prerequisites (dispositions, baselines).
- Verification load, generalization status, risk concentration from audits.

## Procedure

### 1. Build Dependency Graph
- Across wave epics and requirements (e.g., structure execution depends on certain generalized agents for compliance/verification; L4 pack content depends on Arch/Design).
- Map dependencies between generalization batches, structure phases, layer decomp, self-hosting demos.

### 2. Identify Critical Path and Runway
- Identify critical path items (e.g., core compliance agents before full structure moves; hierarchy decomp before editors).
- Track architecture runway (L0-L8 definitions must precede surface work) and verification prerequisites.

### 3. Score Risk and Propose Staging
- Score risk concentration and carryover exposure (e.g., too many structure changes in one wave risks breaking self-hosting).
- Propose staged portfolio execution gates (align with G0/G4/G5).
- Balance delivery scope (more generalized agents) with integrity (clean structure, full traceability).

### 4. Output Portfolio Plan
- Portfolio staging plan with dependency-aware sequencing.
- Governance checkpoints and risk mitigation schedule.
- Recommendations for the WAVE plans and execution plan (e.g., "move Phase 2 legacy quarantine to next wave if verification coverage is low").

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner)
pwsh -File tools/planning/portfolio.ps1 -Scope "R1-Foundations to R2-Elevation" -Baseline docs/structural-refactor-execution-plan.md -Output evidence/portfolio-plan-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Multi-wave portfolio for IDE structure and XGEN" --label planning,ide-platform --body-file evidence/portfolio-plan-*.md
```

### 6. Support Iteration
- Re-plan as new architecture or redlines emerge (common in early IDE).
- Self-referential: plan the portfolio that includes generalizing more agents like this one and executing the structure.

## Outputs
- Portfolio staging plan with dependency-aware sequencing.
- Governance checkpoints and risk mitigation schedule.
- Updated recommendations for WAVE_01 and execution plan.
- Evidence for G0, G1, G4.

## Guardrails
- Prioritize dependency realism over optimistic scheduling.
- Track architecture and verification prerequisites explicitly.
- Quantify risk carryover.
- Keep auditable and update-friendly (feed back into the plans for redlining).

## Generalization & IDE-Specific Notes
- Removed product-specific (e.g., FarmRTK hardware runway).
- Added focus on IDE: balancing generalization of copied agents (Requirements/Arch/Design/Compliance/Verification), structure refactor for editors/viewers/agents as artifacts, layer decomp (L0-L8), self-hosting, pack content in ide-platform.
- Supports the "use the agents to plan the refactor" by sequencing the XGEN and structure work across waves.

## Related
- Gates: G0, G1, G4.
- Agents: Multi-Sprint Portfolio Planner + Planning, Refactoring, Requirements, Arch/Design, Verification, Compliance.
- Used at portfolio level with the execution plan and WAVE plans. Self-referential for the work generalizing the copied agents and refactoring the repo to the full IDE.