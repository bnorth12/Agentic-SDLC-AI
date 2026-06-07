---
name: source-to-evidence-traceability
description: "Audit full source-to-evidence traceability per requirement across source, architecture/design, implementation, and verification artifacts."
---
# Source-to-Evidence Traceability Skill

## Purpose
Validate requirement coverage using a complete chain model:
source requirement artifact -> architecture/design trace -> implementation evidence -> verification evidence.

## Inputs
- Sprint scope
- Requirement corpus in Requirements/
- Architecture and design docs in docs/architecture and docs/design
- Implementation and test evidence references from planning and traceability artifacts
- Root hierarchy artifacts: `docs/architecture/Capability_Hierarchy_Baseline.md` and `docs/architecture/Function_Hierarchy_Registry.md`

## Required Hierarchy Fields
- parent capability ID
- child function ID
- decomposition level (L0/L1/L2)
- allocated component/module
- verification method

## Procedure
1. Build requirement inventory from Requirements/ documents.
2. For each requirement ID, capture evidence refs for all four chain legs:
- source refs
- architecture/design refs
- implementation refs
- verification refs
3. Classify each requirement chain as:
- complete (all four legs present)
- partial (one or more legs missing)
- missing-link (critical leg absent for planning readiness)
4. Validate that sprint issues and decomposition artifacts include all required hierarchy fields.
5. Validate that parent capability IDs and child function IDs are present in root hierarchy artifacts.
6. Validate that each requirement has a corresponding row in `Requirements/15_End_To_End_Traceability_Attributes_Registry.md` linking architecture/design, implementation, and verification artifacts.
7. Emit chain-aware findings with requirement text and evidence snippets.
8. Summarize chain completeness ratio and top missing-link clusters.

## Expected Outputs
- Chain completeness summary
- Missing-link breakdown by requirement prefix and evidence type
- Requirement-level findings that include readable requirement text and evidence refs
- Hierarchy field coverage summary and missing-field list by requirement ID

## Guardrails
- Do not infer evidence where no explicit reference exists.
- Do not stop at first-level ID presence.
- Keep analysis local and file-referenced.
- Treat missing root capability/function artifacts as a hard missing-link condition.
