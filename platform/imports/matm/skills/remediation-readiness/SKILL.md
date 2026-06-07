---
name: remediation-readiness
description: "Assess whether an independent review report contains enough detail to begin remediation sprint intake, and summarize the final remediation strategy section."
---
# Remediation Readiness Skill

## Purpose
Translate an independent review report into remediation themes that are detailed enough for sprint intake, without turning the review itself into a full sprint plan.

## Inputs
- The latest independent review markdown report
- The matching JSON report, if available
- Active health floor from the selected policy profile

## Procedure
1. Read the health score, remediation floor, and severity summary.
2. Determine whether remediation is required before sprint planning.
3. Group findings into a small number of theme-based work packages.
4. Capture dependency order, starter actions, and acceptance criteria for each theme.
5. Distinguish planning-ready items from concept-only or governance-only items.

## Expected Outputs
- A remediation readiness verdict
- Theme-based intake guidance
- A health-floor trigger explanation
- A concise list of dependencies that block planning

## Guardrails
- Do not start or sequence the actual sprint.
- Keep the output local and report-driven.
- Use "health" as the primary readiness metric.
