---
name: hierarchy-taxonomy-steward
description: "Define and normalize hierarchy taxonomy for sprint issue artifacts so capability/function decomposition is structurally consistent and reusable."
---
# Hierarchy Taxonomy Steward Skill

## Purpose
Maintain a stable decomposition taxonomy for remediation planning where each issue maps to a governed hierarchy chain.

## Inputs
- Sprint ID (YYYY-MM or YYYY_MM)
- Sprint issue files under planning/issues/

## Procedure
1. Inspect sprint issue files for required hierarchy fields:
- Parent Capability ID
- Parent Function ID
- Child Function ID
- Decomposition Level
- Allocated Component/Module
- Verification Method

2. Normalize identifiers and naming conventions:
- Parent capability IDs are stable at portfolio level.
- Parent function IDs are stable within capability families.
- Child function IDs represent executable remediation slices.

3. Validate decomposition level semantics:
- L0: capability boundary
- L1: parent function boundary
- L2: child function implementation slice

4. Ensure fan-out is intentional:
- parent capability should usually map to multiple child functions over time
- parent function should show coherent grouping of child functions

5. Capture taxonomy drift findings and include corrective guidance in governance reports.

## Guardrails
- Do not edit runtime implementation code.
- Keep updates local-first and deterministic.
- Treat taxonomy drift as governance debt requiring explicit remediation work items.
