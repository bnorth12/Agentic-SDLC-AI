---
name: kpi-drift-analyst
description: "Analyze KPI trends over time to detect drift, regressions, and remediation impact."
---
# KPI Drift Analyst Skill

## Purpose
Translate trend history into governance insights and operator actions.

## Inputs
- independent_reviews/history/snapshot_index.json
- backfill and latest KPI scoreboard artifacts

## Procedure
1. Compute trend deltas and identify inflection windows.
2. Detect regression streaks and health instability zones.
3. Compare remediation-period versus implementation-period behavior.
4. Publish concise latest scoreboard and narrative analysis.

## Outputs
- KPI drift summary and trend dashboard recommendations.
- Targeted process-correction suggestions.
