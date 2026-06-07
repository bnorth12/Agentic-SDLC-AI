---
name: ide-traceability-blocker-planner
description: >
  Generalized skill for generating a planning-time remediation backlog from traceability blocker output for the agentic IDE platform.
  Primary for Traceability Blocker Planner. Generalizes traceability-blocker-planner (MATM) and related assets. Turns intake failures into actionable backlog for generalization and structure work.
metadata:
  short-description: "Traceability blocker backlog planner for IDE generalized assets and structure"
  agent: ide-traceability-blocker-planner
  gates: [G1_traceability, G4_independent_review]
  maturity: M0+
---

# ide-traceability-blocker-planner

**Agents:** Traceability Blocker Planner (primary), Requirements Baseline Steward, Architecture/Design Traceability Auditor, Source-to-Evidence Traceability Auditor, Refactoring Agent, Planning Agent  
**Parent:** [ide-traceability-blocker-planner.agent.md](../../../agents/ide-platform/ide-traceability-blocker-planner.agent.md) (generalized, to be created) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) · Structural Refactor Execution Plan

## Purpose
Provide an optional, repeatable planning-phase automation that turns traceability validation failures (from baselines, audits, structure changes) into an actionable remediation backlog. This helps systematically address recurring intake or compliance issues during generalization of copied agents and the repo structure refactor.

## When to Invoke
- During planning of waves or structure phases, when traceability validation has been run.
- After audits or baselines to generate backlog for the execution plan.
- User: "plan remediation for traceability blockers in structure", "/ide-traceability-blocker".

## Inputs
- Sprint/work identifier or scope (e.g., "Structure-Refactor").
- Traceability validation output (from ide-source-to-evidence-traceability or similar).
- Hierarchy artifacts, requirements baselines.

## Procedure

### 1. Execute or Use Traceability Validation
- Run or reference the traceability validation (e.g., via ide-source-to-evidence-traceability on the execution plan or generalized assets).

### 2. Classify Blocker Lines
- Classify into:
  - Missing requirement documentation IDs.
  - Issues missing explicit test/verification evidence.
  - Issues missing required hierarchy fields (parent, child, level, allocated, verification).
- For IDE: include blockers related to agents/skills artifacts, layer allocation, structure changes.

### 3. Emit Backlog Report
- Produce a backlog report with ordered remediation steps (prioritized by severity, layer impact, dependency on other work).
- Make it planning-oriented (do not auto-edit; feed to Refactoring Agent or execution plan).
- Include recommendations for the structure (e.g., "add hierarchy to generalized skills in ide-platform per Phase 1").

### 4. PowerShell / GitHub Native Emphasis
```powershell
# Example (adapt)
pwsh -File tools/traceability/blocker-planner.ps1 -Scope "Structure-Refactor" -ValidationOutput evidence/traceability-audit-*.md -Output evidence/traceability-blocker-backlog-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "Traceability blocker backlog for IDE structure" --label traceability,compliance,ide-platform --body-file evidence/traceability-blocker-backlog-*.md
```

### 5. Support Iteration
- Re-generate after fixes or new validations.
- Self-referential: use on the platform's own traceability for the generalization and structure work.

## Outputs
- `evidence/traceability_blocker_backlog_latest.md` (or dated).
- JSON equivalent if needed.
- Prioritized remediation steps for the execution plan or Refactoring Agent.

## Guardrails
- Keep planning-oriented.
- Enforce hierarchy fields.
- Local-only.

## Generalization & IDE-Specific Notes
- Removed product-specific (e.g., sprint ID formats, FarmRTK paths).
- Added focus on IDE: blockers for generalized agents/skills, layer allocation in structure, editors/viewers support, self-hosting traceability.
- Helps plan the remediation in the execution plan (e.g., for hierarchy in L4 packs or Cross structure).

## Related
- Gates: G1, G4.
- Agents: Traceability Blocker Planner + Requirements, Arch/Design, Traceability, Compliance, Refactoring, Planning.
- Used with validation and the structure plan. Self-referential for the work generalizing copied agents.