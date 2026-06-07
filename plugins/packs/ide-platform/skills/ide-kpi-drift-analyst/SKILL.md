---
name: ide-kpi-drift-analyst
description: >
  Generalized skill for analyzing KPI and health trends to detect governance drift, regressions, and remediation impact for the agentic IDE platform.
  Primary for KPI Drift Analyst. Generalizes kpi-drift-analyst (MATM) and related assets. Used for compliance and to monitor the health of self-hosted work including generalization and repo structure refactors.
metadata:
  short-description: "KPI drift analysis for IDE governance, generalization progress, and structure changes"
  agent: ide-kpi-drift-analyst
  gates: [G1_traceability, G4_independent_review]
  maturity: M0+
---

# ide-kpi-drift-analyst

**Agents:** KPI Drift Analyst (primary), Governance Policy Compiler, Independent Review Orchestrator, Refactoring Agent, Planning Agent  
**Parent:** [ide-kpi-drift-analyst.agent.md](../../../agents/ide-platform/ide-kpi-drift-analyst.agent.md) (generalized) · [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md)

## Purpose
Analyze KPI and health trends over time to detect governance drift, regression windows, and remediation impact for the IDE platform's own development (generalization of copied agents into native versions, repo structure improvements, functional decomp, self-hosting, compliance with plans). Translate into operator actions and trend summaries.

This provides the metrics/compliance layer to monitor the health of the prioritized procedures and the structural work, enabling early detection of issues so we can redline and adapt as better designs emerge.

## When to Invoke
- During or after XGEN batches or structural phases to monitor progress and drift.
- Periodically for governance health (e.g., after self-hosted audits or changes).
- When assessing remediation impact from previous reviews or structure moves.
- At wave closeout or before G4/G5.
- User: "analyze drift for the structure execution plan", "KPI trends for generalization", "/ide-kpi-drift".

## Inputs
- independent_reviews/history/snapshot_index.json or equivalent trend data from audits (baseline, disposition, execution plan, compliance audits).
- Backfill and latest KPI scoreboard artifacts (e.g., XGEN completion %, traceability coverage, compliance status, structure phase progress).
- Prior generalized skill outputs (requirements baseline, arch disposition, verification coverage, etc.).

## Procedure

### 1. Compute Trend Deltas and Inflection Windows
- Analyze deltas in key KPIs over time (e.g., % of high-reusability imports generalized into ide-platform, traceability chain completeness for structure changes, compliance score from policy compiler, verification coverage for execution plan).
- Identify regression streaks, health instability zones, and inflection events (e.g., drift after a batch of generalizations or during structure moves).

### 2. Detect Regression and Impact
- Distinguish directional drift from one-off variance.
- Compare remediation-period vs. "implementation" (generalization/structure execution) period behavior.
- Estimate remediation impact and execution side effects (e.g., how structure changes affect editor/viewer readiness for agents/skills).

### 3. Publish Insights and Actions
- Emit concise latest scoreboard and narrative trend analysis.
- Surface leading indicators of alignment decay (e.g., decreasing coverage in L4 plugin host during refactors).
- Produce targeted process-correction suggestions (e.g., "redline the execution plan for more verification hooks on generalized skills" or "use Refactoring Agent to address drift in hierarchy metadata").

### 4. PowerShell / GitHub Native Emphasis
```powershell
# Example (future runner or ACP)
pwsh -File tools/governance/kpi-drift.ps1 -Scope "Structure-Refactor XGEN-Batch" -Baseline docs/ide-structure-requirements-baseline.md -Output evidence/kpi-drift-$(Get-Date -Format yyyyMMdd).md

gh issue create --title "KPI drift detected in IDE structure work" --label compliance,drift,ide-platform --body-file evidence/kpi-drift-*.md
```

### 5. Support Iteration and Self-Hosting
- Re-analyze as new data emerges during execution (the skill itself benefits from the structure changes it monitors).
- Feed insights back into Planning Agent (for re-sequencing), Refactoring Agent (for targeted fixes), and the other generalized skills (e.g., update verification coverage based on drift).
- The skill is self-referential and will analyze trends in its own generalization and the platform's governance health.

## Outputs
- KPI drift summary and trend dashboard recommendations.
- Targeted process-correction suggestions.
- Evidence for G1, G4.
- Updated views for compliance and planning.

## Guardrails
- Base on reproducible time-series evidence.
- Keep trend artifacts concise in latest and complete in history.
- Local-first.

## Generalization & IDE-Specific Notes
- Removed product-specific KPI contexts.
- Added explicit focus on IDE metrics: XGEN progress for prioritized agents (Requirements/Arch/Design/Compliance/Verification), traceability coverage for structure changes, compliance with layered model and self-hosting, functional decomp health, readiness of editors/viewers for agents/skills as artifacts.
- Designed to monitor the very work that generalizes the copied agents and executes the repo refactor, enabling the "redline and adapt" loops.

## Related Platform Artifacts
- Gates: G1, G4.
- Agents: KPI Drift Analyst (primary) + Governance Policy Compiler, Independent Review Orchestrator, Refactoring Agent, Planning Agent.
- Used alongside the other early governance skills to provide the metrics layer for the prioritized procedures and self-hosted structure work. This skill is self-referential and will analyze drift in the platform's own development.