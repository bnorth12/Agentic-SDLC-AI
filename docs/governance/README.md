# Governance Operations

This folder contains governance-operational artifacts used by agents and human reviewers.

## Contents

- policy-agent-enforcement-matrix.md
- lifecycle-gate-checklists.md
- prompt-alignment-gap-report.md

## How to Use

- Use the policy matrix to identify accountability and evidence ownership.
- Use gate checklists at each SDLC decision gate for APPROVE/CONDITIONAL/REJECT/DEFER decisions.
- Use the prompt alignment report to track governance-control coverage in prompt templates.

## Automated Validation

Run the governance evidence validator before marking a gate ready:

```bash
python scripts/validate_governance_evidence.py --input examples/governance/sample_gate2_outputs.json --gate gate_2
```

Input can be one output object, a list of output objects, or an object containing `outputs`.
The validator fails the check if required fields or gate evidence are missing.

## Supervisor Gate Hook

The supervisor now invokes governance validation automatically whenever any node update attempts to set:

- `gate_readiness.status = READY`

Hook behavior:

- Valid evidence: READY transition is allowed.
- Invalid or incomplete evidence: transition is blocked, gate status is downgraded to `NOT_READY`, phase transition is removed from updates, and human approval is required.

To pass the hook, updates must provide governance fields compatible with the validator:

- `policy_compliance`
- `traceability_links`
- `gate_readiness`
- `evidence_links`
- `risks_or_blockers`
