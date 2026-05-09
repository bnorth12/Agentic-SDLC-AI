# Policy-to-Agent Enforcement Matrix

## Purpose

Map each governance policy to enforcing agents, review mechanisms, and evidence artifacts so the organization can execute accountable SDLC control.

## Current Implementation Status

Implemented agents:
- Program Manager
- Chief Engineer
- Requirements Development Agent
- Architecture Agent

Planned agents (not fully implemented yet):
- Safety/Security/Reliability
- Software Development
- Verification and Validation
- Configuration Management
- Data Management
- Integration and Test
- Quality Assurance

## Matrix

| Policy | Primary Enforcer | Supporting Agents | Review Board / HITL Gate | Required Evidence |
|---|---|---|---|---|
| Systems Engineering Management Policy | Chief Engineer | Program Manager, Requirements, Architecture | Gates 2-7 with HITL approval | Decision log, risk updates, board outcomes |
| Project Management Policy | Program Manager | Chief Engineer, all specialist agents | Gate 1 and sprint reviews | Backlog, sprint plan, status metrics |
| Requirements Management Policy | Requirements Agent | Program Manager, Chief Engineer, V&V | Gate 2 | Requirements baseline, RTM, change records |
| Architecture Development Policy | Architecture Agent | Requirements Agent, Chief Engineer | Gate 3 (ARB + HITL) | Architecture baseline, ADRs, requirement links |
| Configuration Management Policy | Configuration Management Agent (planned) | Program Manager, Development, V&V | Gate 4 and Gate 6 | Baseline register, change logs, release manifest |
| Data Management Policy | Data Management Agent (planned) | Program Manager, Chief Engineer, V&V | Gates 5-7 | Data inventory, quality reports, access audit |
| Software Development Plan | Software Development Agent (planned) | Architecture, Requirements, CM | Gate 4 | Requirement-linked PRs, test evidence |
| System Security Management Plan | Safety/Security Agent (planned) | Architecture, Development, Chief Engineer | Gate 6 | Threat model, security tests, waiver records |
| Safety Engineering Plan | Safety/Security Agent (planned) | Requirements, Architecture, V&V | Gate 6 | Hazard log, mitigations, residual risk approval |
| Verification and Validation Plan | V&V Agent (planned) | Requirements, Development, Chief Engineer | Gate 5 | Requirement-test mapping, coverage, test results |
| Risk Management Plan | Program Manager + Chief Engineer | All agents | Gate 1-7 | Risk register, mitigation status, risk acceptance |
| HITL Governance Plan | HITL Reviewer + Chief Engineer | Program Manager, board members | All defined gates | Approval decisions, corrective actions, overrides |

## Enforcement Priority

1. Enforce requirements-to-architecture-to-implementation traceability.
2. Enforce gate readiness evidence before progression.
3. Enforce waiver discipline with explicit accountability.

## Near-Term Actions

- Add planned specialist agents to runtime workflow.
- Bind policy checks to board and HITL prompts.
- Automate evidence completeness checks for each gate.
