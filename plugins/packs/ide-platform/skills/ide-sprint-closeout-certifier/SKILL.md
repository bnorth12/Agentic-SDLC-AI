---
name: ide-sprint-closeout-certifier
description: >
  Generalized skill for certifying sprint/wave closeout quality, evidence completeness, and carryover governance for the agentic IDE platform.
  Primary for Sprint Closeout Certifier. Generalizes sprint-closeout-certifier (MATM) and related assets. Used to certify completion of prioritized procedures (generalization, structure refactor) and self-hosted waves.
metadata:
  short-description: "Sprint/wave closeout certification for IDE generalized assets, structure changes, and governance"
  agent: ide-sprint-closeout-certifier
  gates: [G4_independent_review, G5_baseline, G3_verification_plan]
  maturity: M0+
---

# ide-sprint-closeout-certifier

**Agents:** Sprint Closeout Certifier (primary), Verification Coverage Planner, Source-to-Evidence Traceability Auditor, Independent Review Orchestrator, Refactoring Agent, Planning Agent  
**Parent:** [ide-sprint-closeout-certifier.agent.md](../../../agents/ide-platform/ide-sprint-closeout-certifier.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · Structural Refactor Execution Plan

## Purpose
Ensure wave/sprint or structure work closure is auditable, complete, and suitable for progression in the IDE platform. Reconcile planned vs. delivered (XGEN, structure phases), validate evidence completeness (from procedures), verify deferred items, and issue certification. Supports self-hosting by certifying the platform's own development.

## When to Invoke
- At end of wave foundations or structure phases (e.g., after execution plan Phase 5).
- Before G5 baseline or next wave.
- When assessing readiness post-generalization or structure changes.
- User: "certify closeout for the structure execution plan", "ide-wave certification", "/ide-sprint-closeout".

## Inputs
- Wave/sprint plans (from Planning Agent, execution plan), delivery summaries (generalized in ide-platform, structure moves, evidence).
- Evidence bundles (baseline, disposition, audits, coverage, compliance reports).

## Procedure

### 1. Reconcile Planned vs. Delivered Scope
- Compare committed (e.g., generalize specific agents like the Arch/Design ones, execute structure phases) vs. delivered (actual generalized files, moves completed, evidence produced).
- For the execution plan: check Phase 1-5 completion against the plan.

### 2. Validate Evidence Package Completeness
- Ensure evidence for delivered work is present and complete (e.g., generalized SKILL.md/.agent.md with full chains, structure change records, compliance/traceability/verification reports).
- Check for the self-hosted procedures (e.g., the compliance audit, verification coverage for the plan).

### 3. Verify Deferred/Carryover Governance
- For any deferred (e.g., remaining legacy, ungeneralized imports, future phases), confirm rationale and carryover linkage (e.g., to next wave or legacy/).
- Document in the closeout.

### 4. Issue Closeout Certification
- Verdict: certified (all complete, evidence strong), conditional (gaps with plan to close), failed (critical issues).
- Include residual risks and required carryover controls.
- Tie to gates (G4 review, G5 baseline) and the new structure (e.g., ide-platform as the delivered content home).

### 5. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner or ACP)
pwsh -File tools/verification/closeout.ps1 -Scope "Structure-Refactor XGEN-Batch" -Plan docs/structural-refactor-execution-plan.md -Output evidence/closeout-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Wave closeout: IDE structure refactor" --label verification,compliance,ide-platform --body-file evidence/closeout-*.md
```

### 6. Support Iteration and Self-Hosting
- Re-certify after fixes or new work.
- The skill is self-referential: certify closeout of the waves that generalize the agents and execute the structure work.
- Feed into portfolio/KPI for trends.

## Outputs
- Closeout verdict: certified, conditional, failed.
- Residual risks and required carryover controls.
- Updated evidence.
- Evidence for G3, G4, G5.

## Guardrails
- Require objective closure evidence.
- Flag undocumented carryover as debt.
- Align with IDE readiness (e.g., structure supporting editors for agents/skills).

## Generalization & IDE-Specific Notes
- Removed product-specific (e.g., FarmRTK sprint plans, TC links).
- Added focus on IDE: closeout for waves delivering generalized agents/skills in ide-platform, structure changes (content, legacy, archive), self-hosting evidence from procedures, functional decomp verification.
- Designed to certify the work that generalizes the copied agents and refactors the repo to IDE-native.

## Related Platform Artifacts
- Gates: G3, G4, G5.
- Agents: Sprint Closeout Certifier (primary) + Verification, Traceability, Compliance, Refactoring, Planning agents.
- Used at end of waves with the execution plan and other skills. This skill is self-referential and will certify closeout of the changes that generalize the copied agents and make the repo IDE-native.