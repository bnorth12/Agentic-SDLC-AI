# Platform Agent Registry

**Parent:** [REBOOT_CHARTER.md](../../docs/charter/REBOOT_CHARTER.md)  
**Imports:** `platform/imports/farmrtk/`, `platform/imports/matm/`

Platform agents own **process and governance**. Domain agents live in **plugin packs**.

---

## Core platform agents

| Agent | Skills (target) | Readiness |
|-------|-----------------|-----------|
| **Workspace Orchestrator** | orchestrate-sdlc | IMPORTED |
| **Chief Engineer** | design, review (bundled) | Partial |
| **Independent Review Committee** | independent-review-sdlc, check-work-commit-sdlc | IMPORTED |
| **Requirements Manager** | requirements-management-sdlc | IMPORTED |
| **Traceability Manager** | traceability-audit-sdlc | IMPORTED |
| **Systems Engineer** | icd-maintenance-sdlc, decision-record-sdlc | IMPORTED |
| **V&V Lead** | validation-plan-sdlc, test-authoring-sdlc | IMPORTED |
| **Configuration Manager** | configuration-baseline-sdlc | IMPORTED |
| **Quality Assurance Engineer** | process-audit-sdlc | IMPORTED |
| **Program Analyst** | program-metrics-sdlc | IMPORTED |
| **Risk Manager** | risk-register-sdlc | IMPORTED |
| **Repo Organization Manager** | repo-audit-sdlc | IMPORTED |
| **Technical Writer** | technical-writer-sdlc | IMPORTED |
| **Data Manager** | data-schema-audit-sdlc | IMPORTED |
| **Procurement Coordinator** | procurement-audit-sdlc | IMPORTED |
| **Integration Engineer** | integration-bench (pack) | IMPORTED |
| **Threat Modeling Operator** | threat-modeling pack | WRAP |

## MATM governance agents (imported)

24 agents in `platform/imports/matm/agents/` — merge with platform roles in R2; dedupe orchestrators and auditors.

## Pack-only agents

| Pack | Agents |
|------|--------|
| engineering-sdlc | CAD, Firmware, RF, Electronics (from FarmRTK) |
| threat-modeling | MATM A1–A9 (runtime) |
| github-devops | DevOps / Build Engineer (planned) |