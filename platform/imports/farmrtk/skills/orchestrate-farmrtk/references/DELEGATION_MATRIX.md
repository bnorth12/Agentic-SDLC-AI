# Delegation matrix (orchestrate-farmrtk)

Machine-readable source: [Tools/orchestrate/delegation_map.json](../../../../Tools/orchestrate/delegation_map.json)

| Backlog tag | Primary agent | Project skill(s) | Bundled skill |
|-------------|---------------|----------------|---------------|
| `SW:` | Firmware Engineer | — | `implement`, `check-work` |
| `HW:` (CAD) | FarmRTK CAD Engineer | `openscad-parametric-farmrtk` | — |
| `HW:` (plan) | Mechanical Engineer | `openscad-parametric-farmrtk` | `design` |
| `EL:` | Electronics Engineer | `electronics-wiring-farmrtk` | `design` |
| `TC:` | System Test Engineer | `test-authoring-farmrtk` | `check-work` |
| `DOC:` / `REQ:` | Requirements Manager | `requirements-management-farmrtk` | `design` |
| `KPI:` | Program Analyst | `program-metrics-farmrtk` | — |
| `CM:` | Configuration Manager | `configuration-baseline-farmrtk` | — |
| Merge / gate | EIRC | `independent-review-farmrtk` | `review` |
| ICD / trades | Systems Engineer | `icd-maintenance-farmrtk`, `decision-record-farmrtk` | `design` |
| V&V strategy | V&V Lead | `validation-plan-farmrtk` | — |
| Repo hygiene | Repo Organization Manager | `repo-audit-farmrtk`, `traceability-audit-farmrtk` | — |
| Risk | Risk Manager | `risk-register-farmrtk` | — |
| `INT:` / bench | Integration Engineer | `integration-bench-farmrtk` | `check-work` |

## Milestone routing

| Gate | Lead agent | Skill |
|------|------------|-------|
| M-G0 | Program Manager | `orchestrate-farmrtk` |
| M-G1 | Traceability Manager | `traceability-audit-farmrtk` |
| M-G2 | Systems Engineer | `icd-maintenance-farmrtk` |
| M-G3 | V&V Lead | `validation-plan-farmrtk` |
| M-G4 | System Test Engineer | `test-authoring-farmrtk` |
| M-G5 | Configuration Manager | `configuration-baseline-farmrtk` |