---
name: architecture-design-disposition-planner
description: "Prepare architecture/design disposition workpacks so remediation execution makes an explicit design-vs-implementation decision with traceability and approval."
---
# Architecture/Design Disposition Planner Skill

## Purpose
Create a deterministic disposition package before implementation closeout so remediation work does not bypass architecture/design decision logic.

## Inputs
- Remediation sprint plan under planning/
- Evidence target list in the selected remediation plan
- Requirement IDs in scope
- Existing architecture/design, implementation, and verification references

## Required Hierarchy Fields
- parent capability ID
- child function ID
- decomposition level (L0/L1/L2)
- allocated component/module
- verification method

## Procedure
1. Parse the selected remediation sprint plan and extract requirement IDs plus evidence targets.
2. Build an authoring workpack that separates architecture/design targets, implementation targets, and verification targets.
3. Require explicit parent-child decomposition and code-level allocation fields for each remediation slice.
4. Flag missing legs in the traceability chain.
5. Require one disposition decision path and a rationale/approval record.

## Outputs
- `independent_reviews/latest/architecture_design_authoring_workpack_latest.md`
- `independent_reviews/latest/architecture_design_authoring_workpack_latest.json`
- Explicit disposition decision template with approval and rerun-verification fields.
