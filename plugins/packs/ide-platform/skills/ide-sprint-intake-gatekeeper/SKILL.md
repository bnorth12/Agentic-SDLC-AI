---
name: ide-sprint-intake-gatekeeper
description: >
  Generalized skill for gating sprint/wave intake on traceability completeness, dependency readiness, architecture alignment, and governance quality for the agentic IDE platform.
  Primary for Sprint Intake Gatekeeper. Generalizes sprint-intake-gatekeeper (MATM) and related assets. Prevents low-readiness generalized agents or structure changes from entering execution.
metadata:
  short-description: "Sprint/wave intake gate for IDE generalized assets, structure, and governance"
  agent: ide-sprint-intake-gatekeeper
  gates: [G0_wave_charter, G1_traceability, G4_independent_review]
  maturity: M0+
---

# ide-sprint-intake-gatekeeper

**Agents:** Sprint Intake Gatekeeper (primary), Requirements Baseline Steward, Architecture/Design Traceability Auditor, Verification Coverage Planner, Governance Policy Compiler, Refactoring Agent, Planning Agent  
**Parent:** [ide-sprint-intake-gatekeeper.agent.md](../../../agents/ide-platform/ide-sprint-intake-gatekeeper.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · Structural Refactor Execution Plan

## Purpose
Prevent low-readiness scope (generalized agents/skills, structure changes, new IDE surfaces) from entering sprint/wave execution or the refactored repo. Gate on requirement alignment, dependency readiness, architecture traceability, hierarchy, and governance quality. This is the intake "quality gate" for the prioritized procedures and self-hosted work.

## When to Invoke
- Before starting execution of waves, XGEN batches, or structure phases.
- When proposing new generalized agents or changes to the execution plan.
- At G0 wave charter or intake points.
- User: "gate intake for the next generalization batch", "ide-sprint-intake", "/ide-wave-intake-gate".

## Inputs
- Sprint/wave plans or proposed changes (generalized files, structure moves from execution plan).
- Requirement baselines, architecture dispositions, hierarchy artifacts, end-to-end traceability registry.
- Governance policy profiles and previous review outputs.

## Procedure

### 1. Validate Requirement and Architecture Traceability
- For each intake item (e.g., a generalized agent or structure change), validate linkage to requirements (from baseline) and architecture/design (from disposition).
- Confirm alignment with IDE layers (e.g., L4 for skills in ide-platform, Cross for structure).

### 2. Verify Dependency Ordering and Readiness
- Check dependency order, risk labels, and acceptance readiness.
- Ensure prerequisites (e.g., prior generalized skills, structure phases) are met.

### 3. Check Governance and Hierarchy
- Confirm governance artifacts (policies, reviews) are sufficient.
- Enforce root hierarchy integrity: every intake item must map to valid parent capability and child function IDs (L0-L8 or structure components).
- Enforce registry linkage: items must have matching traceability or pre-approved action.

### 4. Issue Intake Verdict
- Return: ready, conditional (with explicit closure criteria), or blocked.
- List missing prerequisites and actionable checklist.
- Explicit blockers for missing hierarchy or traceability legs.

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner or ACP, adapted for IDE)
pwsh -File tools/intake/gate.ps1 -Scope "XGEN-Batch Structure-Phase" -Plan docs/structural-refactor-execution-plan.md -Baseline docs/ide-structure-requirements-baseline.md -Output evidence/intake-gate-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Intake gate findings for IDE structure" --label compliance,intake,ide-platform --body-file evidence/intake-gate-*.md
```

### 6. Support Iteration and Self-Hosting
- Re-gate after remediation or new proposals.
- The skill is self-referential: gate the intake of the very changes that generalize the copied agents and execute the structure plan.
- Feed blockers into the execution plan or Refactoring Agent.

## Outputs
- Intake gate outcome: ready, conditional, blocked.
- Missing prerequisites and action checklist.
- Explicit blockers for missing root artifacts, hierarchy, or traceability.
- Evidence for G0, G1, G4.

## Guardrails
- Intake decisions must be evidence-based.
- Block when critical traceability or hierarchy legs are missing.
- Align with active policy profile (strict for platform core and structure).

## Generalization & IDE-Specific Notes
- Removed product-specific (e.g., FarmRTK sprint files, SYS-DOC).
- Added explicit gating for IDE model: intake must align with layers (L4 packs for generalized skills, L0 for editors, Cross for structure), support agents/skills as editable artifacts, enable the refactored repo layout, and pass self-hosting checks.
- Strong support for functional decomp: enforce hierarchy in all intake items.
- Designed to gate the work that generalizes the copied agents and improves the repo for the full IDE.

## Related Platform Artifacts
- Gates: G0, G1, G4.
- Agents: Sprint Intake Gatekeeper (primary) + Requirements, Arch/Design, Verification, Compliance agents, Refactoring, Planning.
- Used at the start of waves with the execution plan and baselines. This skill is self-referential and will gate the intake of the changes that generalize the copied agents and make the repo IDE-native.