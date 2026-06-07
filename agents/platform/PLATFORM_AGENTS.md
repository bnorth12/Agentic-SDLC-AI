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
| **Planning Agent** (new) | ide-portfolio-planning (primary), generalized orchestrate-sdlc, program-metrics-sdlc | New (R1) — composes multi-sprint-portfolio-planner + sprint-intake-gatekeeper + kpi-drift-analyst + ... from imports |
| **Refactoring Agent** (new) | ide-structural-refactoring (primary), generalized repo-audit-sdlc, traceability-audit-sdlc, technical-writer-sdlc | New (R1–R3) — composes repo-governance-autoflow-orchestrator + architecture-design-* + source-to-evidence-traceability-auditor + artifact-lineage-auditor + governance-policy-compiler + ... from imports |

## MATM governance agents (imported)

24 agents in `platform/imports/matm/agents/` — merged/synthesized into platform roles (including the new Planning Agent and Refactoring Agent) in R1–R2. All must be generalized (product suffixes removed, manifest-driven, IDE surfaces added) before full promotion. See the two new agent definitions for composition details.

## Pack-only agents

| Pack | Agents |
|------|--------|
| engineering-sdlc | CAD, Firmware, RF, Electronics (from FarmRTK) — generalize further for IDE |
| threat-modeling | MATM A1–A9 (runtime) — wrap as viewer + pipeline plugin |
| github-devops | DevOps / Build Engineer (planned) + gh CLI skills for gates |
| ide-platform | Planning Agent, Refactoring Agent, IDE Hierarchy Taxonomy Steward, IDE KPI Drift Analyst, IDE Repo Governance Autoflow Orchestrator, IDE Requirements Implementation Auditor, IDE Independent Review History Rollup Orchestrator (and supporting governance/compliance agents from all XGEN tranches), plus FarmRTK-derived (ide-decision-record, ide-icd-maintenance, ide-risk-register, ide-configuration-baseline, ide-data-storage, ide-test-authoring, ide-independent-review, ide-bom-procurement, ide-program-metrics, ide-check-work-commit, ide-repo-audit, ide-process-audit, etc. — see full list in plugins/packs/ide-platform/agents/ and skills/). Future Editor/Viewer/Interaction agents (platform-level process). See plugins/packs/ide-platform/agents/ for the generalized .agent.md files. |

**XGEN complete note (FarmRTK + MATM):** All 17 FarmRTK platform skills + 24 MATM agents generalized into this pack (Tranche 1/2/3; see agents/platform/invocations/remaining-xgen-refactoring-session.md and IDE_ARCHITECTURE_TRACEABILITY_MATRIX.md for batch details, tool usage via ide_core.py, and coordination with L2 executor, L4 loader, matrix, IDE_REFACTOR_PLAN §5, PowerShell-MVP). Full registration, manifest, and cross-plan updates executed. Domain FarmRTK remain in engineering-sdlc. Cross-coordination: L4/L7 packs, Cross XGEN, gates, new tools. Open to GUI/custom shell evolution.