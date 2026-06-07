---
name: ide-program-metrics
description: >
  Compute IDE platform program health KPIs (generalization progress, XGEN coverage,
  structure hygiene, self-hosting quality, layer completion) and write measurement
  passes. Generalizes program-metrics-farmrtk. Use for KPI dashboard update,
  Planning Agent monthly review, or after major generalization tranche.
metadata:
  short-description: "KPI program metrics for IDE platform generalization and self-hosting"
  agent: program-analyst
  gates: [G1_traceability, G4_independent_review, G5_baseline]
  maturity: M0+
---

# ide-program-metrics

**Agent:** Program Analyst (generalized)  
**Parent:** [PLATFORM_AGENTS.md](../../../agents/platform/PLATFORM_AGENTS.md) · [IDE_REFACTOR_PLAN.md](../../../docs/charter/IDE_REFACTOR_PLAN.md) (Cross XGEN / XSELF) · [IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md](../../../docs/charter/ide-refactor/IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md)

## Purpose
Compute and report IDE platform health KPIs focused on generalization (XGEN % complete, FarmRTK/MATM coverage), structure (L0-L8 demonstration, legacy quarantine progress), self-hosting quality, and traceability matrix maintenance. Feeds the Planning Agent portfolio view and kpi-drift-analyst.

## When to Invoke
- End of XGEN tranche or WAVE (e.g., after FarmRTK batch).
- Monthly or after KPI remediation.
- User: "run IDE platform KPIs", "update generalization dashboard".
- As part of ide-portfolio-planning closeout or after using new L2 executor/tools.

## Inputs
- The traceability matrix, LAYER_WORK_PACKAGE_INDEX.md, and recent invocation records.
- Generalized content count in ide-platform (agents/ + skills/).
- Structure audit results (from ide-repo-audit / ide-process-audit).
- Previous measurement passes.

## Procedure

### 1. Run Metrics (generalized)
```powershell
# Generalized metrics collection
pwsh -File tools/ci/ide_program_metrics.ps1 -Scope "XGEN + self-hosting + matrix"
```

### 2. Read & Compare
- Read output (e.g., evidence/measurements/<date>-ide-kpi-pass.md).
- Compare to thresholds in the matrix or layer index (warn/critical for generalization % , hierarchy coverage, etc.).

### 3. Open Items & Update
- Open KPI: items in the layer index or BACKLOG if below threshold.
- Manually bump dashboard_rev / matrix version when accepting pass.
- Optional: -UpdateDashboard to patch references.

### 4. Post-Pass
- Feed results to ide-kpi-drift-analyst for trend analysis.

## Outputs
- KPI pass report with scores for generalization, structure, self-hosting.
- Updated matrix or layer index with new measurements.
- Evidence for G1/G4/G5.

## Escalation
- Sustained low generalization % or matrix drift → Planning Agent re-sequencing + Refactoring Agent.
- Missing data for new tools/executor → L2 tooling work.

## Generalization & IDE-Specific Notes
- Stripped FarmRTK hardware/project-specific KPIs (CAD, firmware, SYS-DOC paths).
- Replaced with IDE-native: XGEN coverage (Tranche 1/2 + FarmRTK), L0-L8 demonstration via matrix, self-hosting audit quality, tool/executor adoption.
- PowerShell + gh for attaching KPI passes to generalization PRs.
- Directly supports the traceability matrix as a primary data source.

## Related Platform Artifacts
- Gates: G1, G4, G5.
- Tools: ide_core, the L2 executor (for automated metric collection in future).
- Used by: ide-kpi-drift-analyst, Planning Agent (ide-portfolio-planning), ide-structural-refactoring closeout.
- Lives in the IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md (Cross rows).
