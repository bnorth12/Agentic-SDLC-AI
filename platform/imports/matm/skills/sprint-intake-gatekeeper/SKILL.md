---
name: sprint-intake-gatekeeper
description: "Gate sprint intake on traceability completeness, dependency readiness, and governance quality."
---
# Sprint Intake Gatekeeper Skill

## Purpose
Prevent low-readiness scope from entering sprint execution.

## Inputs
- sprint planning files
- requirement, architecture, and issue-governance evidence
- root hierarchy artifacts (`docs/architecture/Capability_Hierarchy_Baseline.md`, `docs/architecture/Function_Hierarchy_Registry.md`)
- end-to-end traceability registry (`Requirements/15_End_To_End_Traceability_Attributes_Registry.md`)

## Procedure
1. Validate intake item requirement linkage and acceptance criteria.
2. Confirm dependency order and risk labels.
3. Check governance policy alignment for intake quality.
4. Enforce root hierarchy integrity: every intake item must map to valid parent capability and child function IDs.
5. Enforce registry linkage: intake items must have a matching end-to-end traceability row or a pre-approved action to create one in-sprint.
6. Return intake verdict with closure criteria.

## Outputs
- Intake gate outcome: ready, conditional, blocked.
- Missing prerequisites and action checklist.
- Explicit blockers for missing root artifacts and missing end-to-end registry legs.
