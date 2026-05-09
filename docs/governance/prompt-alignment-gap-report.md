# Prompt Alignment Gap Report

## Scope

Assesses alignment between current agent prompts and governance policies/plans.

Reviewed Sources:
- src/config/prompts.py
- docs/agent-roles.md
- docs/policies/*.md
- docs/plans/*.md

## Summary

Current prompts establish a solid engineering baseline and escalation model, but they under-specify explicit policy compliance reporting, gate readiness evidence, and role-specific governance outputs needed for consistent HITL decisions.

## Findings

1. Policy Traceability Output Gap
- Gap: Prompts require requirement traceability but do not require policy compliance declarations.
- Impact: HITL reviewers cannot quickly verify policy conformance.
- Remediation: Add required `policy_compliance` output section per agent response.

2. Gate Readiness Evidence Gap
- Gap: Prompts do not explicitly require gate readiness status and missing evidence list.
- Impact: Gate decisions may be inconsistent and harder to audit.
- Remediation: Add `gate_readiness` and `evidence_links` outputs.

3. Requirement Linkage Rigor Gap
- Gap: Requirement traceability is stated but not normalized as required IDs for features/functions.
- Impact: Weak trace consistency across architecture and implementation.
- Remediation: Require `traceability_links` with requirement IDs for every proposed feature or change.

4. HITL Approval Context Gap
- Gap: HITL prompt does not force explicit policy references or unresolved risk disclosure.
- Impact: Human approvers may accept incomplete context.
- Remediation: Add policy references, blocker list, and residual risk fields.

5. Board Governance Output Gap
- Gap: Board prompts do not require explicit requirement-trace and policy compliance vote rationale.
- Impact: Board decisions may miss governance dimensions.
- Remediation: Add compliance and trace checks to evaluation criteria and output schema.

## Remediation Status

- Implemented in this update: yes, core prompt templates were strengthened to require policy compliance, traceability links, gate readiness, and evidence references.
- Remaining future work: add specialist role prompts for configuration management and data management once corresponding runtime agents are implemented.

## Recommended Follow-On

- Add automated linting for required prompt output fields in agent responses.
- Add gate-specific response templates per phase to reduce ambiguity.
