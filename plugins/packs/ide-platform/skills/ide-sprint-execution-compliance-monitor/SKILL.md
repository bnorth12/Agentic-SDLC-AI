---
name: ide-sprint-execution-compliance-monitor
description: >
  Generalized skill for monitoring sprint/wave execution compliance with plans, hierarchy, and governance for the agentic IDE platform.
  Primary for Sprint Execution Compliance Monitor. Generalizes sprint-execution-compliance-monitor (MATM) and related assets. Monitors adherence during generalization and structure refactors.
metadata:
  short-description: "Sprint execution compliance monitoring for IDE generalized assets and structure"
  agent: ide-sprint-execution-compliance-monitor
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-sprint-execution-compliance-monitor

**Agents:** Sprint Execution Compliance Monitor (primary), Governance Policy Compiler, Hierarchy Conformance Auditor, Independent Review Orchestrator, Refactoring Agent, Planning Agent  
**Parent:** [ide-sprint-execution-compliance-monitor.agent.md](../../../agents/ide-platform/ide-sprint-execution-compliance-monitor.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · Structural Refactor Execution Plan

## Purpose
Monitor execution of IDE waves or structure work for compliance with plans, policies, hierarchy (decomp), and governance. Track during generalization of copied agents and repo structure refactors, flagging issues for remediation. Supports self-hosting compliance.

## When to Invoke
- During execution of waves or structure phases (e.g., mid-execution plan).
- To check adherence of generalized artifacts and changes.
- User: "monitor compliance for the structure execution plan", "/ide-sprint-compliance-monitor".

## Inputs
- Wave plans, execution plan, generalized artifacts in ide-platform, structure records, procedure outputs.

## Procedure

### 1. Monitor Against Plans and Policies
- Track execution (e.g., XGEN progress, structure phase completion) against the plan (e.g., execution plan phases).
- Check compliance with policies (via ide-governance-policy-compiler) and hierarchy (via ide-hierarchy-conformance).

### 2. Identify Deviations
- Flag non-adherence (e.g., missing hierarchy in structure changes, policy violations in generalized files, incomplete phases).
- Use the new structure to verify (e.g., content in ide-platform, no legacy in active tree).

### 3. Escalate and Report
- Classify findings by severity.
- Produce compliance status and prioritized escalations for review and remediation.
- Tie to self-hosting: ensure the platform's development adheres to its own governance.

### 4. PowerShell / GitHub Native Emphasis
```powershell
pwsh -File tools/compliance/execution-monitor.ps1 -Scope "Structure-Refactor" -Plan docs/structural-refactor-execution-plan.md -Output evidence/compliance-monitor-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Execution compliance issues in IDE structure" --label compliance,ide-platform --body-file evidence/compliance-monitor-*.md
```

### 5. Support Iteration
- Re-monitor after remediation.
- Self-referential for the platform's waves.

## Outputs
- Compliance status and deviation findings.
- Escalations for remediation.
- Evidence for G1, G4, G5.

## Guardrails
- Deterministic checks.
- Local evidence.
- Escalate hierarchy/policy breaches.

## Generalization & IDE-Specific Notes
- Removed product-specific.
- Added focus on IDE: monitoring generalized agents in ide-platform, structure changes for the model, self-hosting adherence, decomp in the refactor.
- Certifies the work generalizing copied agents and refactoring the repo.

## Related
- Gates: G1, G4, G5.
- Agents: Compliance Monitor + other governance, Refactoring, Planning.
- Self-referential for the generalization and structure work.