# Lifecycle Gate Checklists (HITL)

## Purpose

Provide standard human-in-the-loop checklists for go/no-go decisions at each SDLC governance gate.

## Decision Options

- APPROVE
- APPROVE_WITH_CONDITIONS
- REJECT
- DEFER

## Gate 1: Objective Acceptance and Scope Definition

Checklist:
- Objective is clear, bounded, and success criteria are defined.
- Stakeholder intent and constraints are documented.
- Initial backlog and ownership are established.
- Initial risk scan exists with critical unknowns captured.

Required Evidence:
- Objective statement
- Initial backlog
- Initial risk register

## Gate 2: Requirements Baseline Approval

Checklist:
- Requirements are uniquely identified and prioritized.
- Requirements are testable and include verification method.
- Requirement sources and rationale are documented.
- Requirement-to-work-item trace links exist.

Required Evidence:
- Requirements baseline
- Requirements traceability matrix
- Open issues list

## Gate 3: Architecture Baseline Approval

Checklist:
- Architecture addresses approved requirements.
- Architecture elements are traced to requirements.
- Interfaces and constraints are defined.
- Major trade studies and design decisions are documented.
- Risks, safety, and security impacts are assessed.

Required Evidence:
- Architecture baseline package
- Requirement-to-architecture trace matrix
- Architecture board decision record

## Gate 4: Implementation Quality and Configuration Integrity

Checklist:
- Implemented work maps to approved requirements.
- Code quality checks passed and defects triaged.
- Configuration baseline is updated and controlled.
- Change records include rationale and approvals.

Required Evidence:
- Change set summary with requirement links
- Test and lint reports
- Configuration baseline update record

## Gate 5: Verification and Validation Evidence Acceptance

Checklist:
- Requirement-to-test traceability is complete for in-scope requirements.
- Verification results meet acceptance criteria.
- Defects are resolved or formally dispositioned.
- Coverage targets are achieved or waived with justification.

Required Evidence:
- V&V report
- Coverage summary
- Defect disposition log

## Gate 6: Security and Safety Release Approval

Checklist:
- Security controls are validated and high risks are dispositioned.
- Safety mitigations are verified and residual risk accepted.
- Open critical findings are resolved or explicitly waived.
- Release candidate satisfies security and safety conditions.

Required Evidence:
- Security assessment and test report
- Safety assessment and mitigation status
- Waiver approvals (if any)

## Gate 7: Post-Release Performance and Risk Review

Checklist:
- Operational performance meets expected thresholds.
- Incidents and anomalies are logged and triaged.
- Risk posture is updated with production observations.
- Backlog includes corrective and improvement actions.

Required Evidence:
- Post-release metrics summary
- Incident and problem report
- Updated risk register and action plan

## Conditional Approval Rules

- Every condition must become a tracked work item with owner and due date.
- Unclosed conditions block progression to the next dependent gate unless waived.
