---
name: ide-remediation-readiness
description: >
  Generalized skill for assessing remediation readiness and evidence completeness for IDE development waves and structure changes.
  Primary for Remediation Readiness Strategist. Generalizes remediation-readiness-strategist (MATM) and related assets. Ensures the prioritized procedures and repo structure refactor are ready for closeout and progression.
metadata:
  short-description: "Remediation readiness assessment for IDE generalized assets, structure, and governance"
  agent: ide-remediation-readiness-strategist
  gates: [G4_independent_review, G5_baseline, G3_verification_plan]
  maturity: M0+
---

# ide-remediation-readiness

**Agents:** Remediation Readiness Strategist (primary), Sprint Closeout Certifier, Verification Coverage Planner, Independent Review Orchestrator, Refactoring Agent, Planning Agent  
**Parent:** [ide-remediation-readiness-strategist.agent.md](../../../agents/ide-platform/ide-remediation-readiness-strategist.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · Structural Refactor Execution Plan

## Purpose
Assess readiness for remediation or closeout of IDE waves or structure work. Reconcile evidence from self-hosted procedures, verify compliance/verification, and recommend carryover for gaps. Supports certifying the generalization of copied agents and the repo refactor.

## When to Invoke
- Before closeout or G5 for structure/generalization waves.
- Post-execution of phases in the execution plan.
- User: "assess readiness for the structure refactor", "ide-remediation-readiness", "/ide-remediation-readiness".

## Inputs
- Wave plans, execution plan, evidence bundles (generalized in ide-platform, structure records, audits, coverage, compliance).

## Procedure

### 1. Reconcile Planned vs. Actual
- Compare committed remediation (XGEN prioritized, structure phases) vs. delivered (generalized files, moves, evidence produced).

### 2. Validate Evidence Completeness
- Check that evidence packages are complete (generalized SKILL.md/.agent.md with chains, structure changes, reports from procedures).

### 3. Verify Deferred Items
- For any deferred (remaining legacy, future XGEN), confirm rationale and carryover (e.g., to next wave or legacy/).

### 4. Issue Readiness Assessment
- Assessment: ready, conditional, not-ready.
- Residual risks and carryover controls.
- Tie to the new structure and self-hosting.

### 5. PowerShell / GitHub Native Emphasis
```powershell
pwsh -File tools/verification/remediation-readiness.ps1 -Scope "Structure-Refactor" -Plan docs/structural-refactor-execution-plan.md -Output evidence/remediation-readiness-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Remediation readiness for IDE structure" --label verification,compliance,ide-platform --body-file evidence/remediation-readiness-*.md
```

### 6. Support Iteration
- Re-assess after fixes.
- Self-referential for the platform's development waves.

## Outputs
- Readiness assessment with verdict, risks, carryover.
- Updated evidence.
- Evidence for G3, G4, G5.

## Guardrails
- Objective evidence required.
- Align with IDE readiness.

## Generalization & IDE-Specific Notes
- Removed product-specific.
- Added focus on IDE: readiness for generalized agents in ide-platform, structure changes, self-hosting, decomp.
- Certifies the work generalizing copied agents and refactoring the repo.

## Related
- Gates: G3, G4, G5.
- Agents: Remediation Readiness Strategist + Closeout, Verification, etc.
- Self-referential for the generalization and structure work.