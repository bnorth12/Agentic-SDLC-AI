# Requirements Management Policy

## Policy ID

RMP-001

## Purpose

Ensure every delivered capability is grounded in approved, testable requirements with end-to-end traceability.

## Scope

Applies to requirements elicitation, analysis, baseline management, change control, and verification linkage.

## Plan Reference

This policy is implemented by **RMP-PLAN-001** (Requirements Management Plan) located at `docs/plans/requirements-management-plan.md`. All authoring standards, formats, ID schemes, and lifecycle rules are defined there.

## Policy Statements

1. Every feature and function shall trace to at least one approved requirement.
2. Every requirement shall be uniquely identified using the `[PREFIX]-[NNNN]` scheme defined in RMP-PLAN-001 §2.2.
3. Every requirement shall be written in **noun-SHALL-verb** format as defined in RMP-PLAN-001 §2.1.
4. Every requirement shall include all mandatory attributes defined in RMP-PLAN-001 §2.3: ID, Short Name, Requirement Text, Rationale, Verification Method(s), Verification Statement, Status, Priority, Source, and Trace fields.
5. Every requirement shall include at least one verification method and a verification statement explaining how compliance will be confirmed.
6. Requirement changes after baseline shall require change control and impact analysis.
7. Implementation and architecture work shall not proceed on unapproved requirement deltas unless explicitly waived.

## Requirement Quality Criteria

- Clear and unambiguous language
- Verifiable outcome
- Traceable source and rationale
- Consistent with system constraints
- Non-overlapping with existing requirements

## Traceability Rules

- Requirement -> Architecture element mapping is mandatory.
- Requirement -> Work item mapping is mandatory.
- Requirement -> Test case mapping is mandatory before release.
- Missing trace links block governance gate approval.

## Change Management

- Proposed changes must include rationale, impact, and affected artifacts.
- Chief Engineer approves technical impact assessment.
- Program Manager approves schedule and resource impact.

## Compliance Evidence

- Requirements baseline (PRODUCT_REQUIREMENTS.md at Gate 2)
- Requirements traceability matrix (RTM linking requirements to architecture, work items, and tests)
- Change request and disposition records
- Verification linkage reports
- Requirements format compliance audit (noun-SHALL-verb check)
