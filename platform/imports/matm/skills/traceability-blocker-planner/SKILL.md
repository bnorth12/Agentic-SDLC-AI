---
name: traceability-blocker-planner
description: "Generate a planning-time remediation backlog from sprint traceability blocker output so recurring intake failures can be addressed systematically."
---
# Traceability Blocker Planner Skill

## Purpose
Provide an optional, repeatable planning-phase automation pass that turns traceability validation failures into an actionable remediation backlog.

## Inputs
- Sprint identifier (`YYYY_MM`)
- `scripts/verify_sprint_traceability.py` output

## Required Hierarchy Fields
- parent capability ID
- child function ID
- decomposition level (L0/L1/L2)
- allocated component/module
- verification method

## Procedure
1. Execute sprint traceability validation.
2. Classify blocker lines into:
- missing requirement documentation IDs
- issues missing explicit test evidence
 - issues missing required hierarchy fields
3. Emit a backlog report with ordered remediation steps.

## Outputs
- `independent_reviews/latest/traceability_blocker_backlog_latest.md`
- `independent_reviews/latest/traceability_blocker_backlog_latest.json`
