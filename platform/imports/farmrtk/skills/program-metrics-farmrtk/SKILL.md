---
name: program-metrics-farmrtk
description: >
  Compute FarmRTK program health KPIs (repo health, quality, execution) and
  write measurement pass to Docs/System-Level/measurements/. Use for KPI
  dashboard update, Program Analyst monthly review, or SYS-DOC-08 maintenance.
metadata:
  short-description: "KPI-1/2/3 program metrics"
---

# program-metrics-farmrtk

**Agent:** Program Analyst  
**Dashboard:** [08-Program-Health-Dashboard.md](../../../Docs/System-Level/08-Program-Health-Dashboard.md)

## When to invoke

- End of wave or monthly
- After KPI remediation PRs
- User: "run KPI measurement", "update program dashboard"

## Steps

1. Run metrics:

```powershell
powershell -File Tools/ci/program_metrics.ps1
```

2. Read output file `Docs/System-Level/measurements/<date>-kpi-pass-auto.md`.
3. Compare to thresholds in SYS-DOC-08 (warn / critical).
4. Open `KPI:` items in [System-Level BACKLOG](../../../Docs/System-Level/BACKLOG.md) if below threshold.
5. Manually bump `dashboard_rev` and snapshot table in SYS-DOC-08 when accepting pass.

## Maturity

At M0–M1, KPI misses are **tracked**, not commit-blockers.

## Dashboard update

```powershell
powershell -File Tools/ci/program_metrics.ps1 -UpdateDashboard
```

Patches SYS-DOC-08 snapshot, bumps `dashboard_rev`, writes `measurements/<date>-kpi-pass-02.md`.