# Platform Reboot — Major Refactor TODO

**Parent:** [REBOOT_CHARTER.md](REBOOT_CHARTER.md)  
**Status:** Living burn-down — update as imports are generalized

---

## Legend

| Status | Meaning |
|--------|---------|
| `IMPORTED` | Copied from source repo; not yet generalized |
| `RENAME` | Skill/agent id must drop product suffix |
| `WRAP` | Becomes plugin wrapper, not inline code |
| `DROP` | Remove from platform; stays in source repo only |
| `BRIDGE` | Temporary adapter during migration |

---

## FarmRTK → Platform mapping

### Platform skills (`platform/imports/farmrtk/skills/`)

| Source skill | Target platform id | Status | Refactor work |
|--------------|-------------------|--------|---------------|
| `orchestrate-farmrtk` | `orchestrate-sdlc` | IMPORTED | Generalize `delegation_map.json`; workspace-relative paths |
| `independent-review-farmrtk` | `independent-review-sdlc` | IMPORTED | Maturity profiles; product-agnostic EIRC checklist |
| `check-work-commit-farmrtk` | `check-work-commit-sdlc` | IMPORTED | Parameterize repo layout rules |
| `traceability-audit-farmrtk` | `traceability-audit-sdlc` | IMPORTED | REQ/TC patterns configurable per workspace |
| `program-metrics-farmrtk` | `program-metrics-sdlc` | IMPORTED | KPI dashboard path from manifest |
| `requirements-management-farmrtk` | `requirements-management-sdlc` | IMPORTED | Segment path aliases |
| `test-authoring-farmrtk` | `test-authoring-sdlc` | IMPORTED | TC prefix configurable |
| `configuration-baseline-farmrtk` | `configuration-baseline-sdlc` | IMPORTED | Baseline tuple from manifest |
| `icd-maintenance-farmrtk` | `icd-maintenance-sdlc` | IMPORTED | ICD doc path configurable |
| `decision-record-farmrtk` | `decision-record-sdlc` | IMPORTED | ADR dir from manifest |
| `repo-audit-farmrtk` | `repo-audit-sdlc` | IMPORTED | README tree rules generic |
| `validation-plan-farmrtk` | `validation-plan-sdlc` | IMPORTED | V&V plan path alias |
| `risk-register-farmrtk` | `risk-register-sdlc` | IMPORTED | Risk doc id configurable |
| `process-audit-farmrtk` | `process-audit-sdlc` | IMPORTED | Registry paths from platform root |
| `technical-writer-farmrtk` | `technical-writer-sdlc` | IMPORTED | Quick-start template generic |
| `data-storage-farmrtk` | `data-schema-audit-sdlc` | IMPORTED | Schema doc + header paths in manifest |
| `bom-procurement-farmrtk` | `procurement-audit-sdlc` | IMPORTED | BOM + PROC tag configurable |

### Domain pack (`plugins/packs/engineering-sdlc/imports/`)

| Source skill | Pack action | Status |
|--------------|-------------|--------|
| `OpenSCAD-Parametric-FarmRTK` | Stay in engineering pack | IMPORTED |
| `firmware-build-farmrtk` | Generalize → `firmware-build` + toolchain plugin | IMPORTED |
| `integration-bench-farmrtk` | Generalize → `integration-bench` | IMPORTED |
| `electronics-wiring-farmrtk` | Optional embedded pack extension | IMPORTED |
| `rf-antenna-farmrtk` | Optional embedded pack extension | IMPORTED |

### FarmRTK agents

| Source | Platform agent | Status |
|--------|----------------|--------|
| `AGENTS-AND-SKILLS.md` registry | `agents/platform/PLATFORM_AGENTS.md` | TODO R1 |
| Product-specific personas (CAD, RF) | engineering-sdlc pack only | BRIDGE |

---

## MATM → Platform mapping

### Governance skills (`platform/imports/matm/skills/`)

| Skill | Platform role | Status |
|-------|---------------|--------|
| `independent-review-orchestrator` (via agent) | EIRC / governance pack | IMPORTED |
| `remediation-readiness` | Sprint gate skill | IMPORTED |
| `kpi-drift-analyst` | Program metrics alignment | IMPORTED |
| `requirements-baseline-steward` | REQ gate skill | IMPORTED |
| `traceability-blocker-planner` | Traceability skill merge | IMPORTED |
| `sprint-closeout-certifier` | Wave end gate | IMPORTED |
| `governance-policy-compiler` | Gate policy compiler | IMPORTED |
| All 26 MATM skills | Audit for overlap with FarmRTK imports | IMPORTED |

### Threat modeling runtime

| MATM asset | Platform action | Status |
|------------|-----------------|--------|
| A1–A9 LangGraph pipeline | `plugins/packs/threat-modeling/` WRAP | TODO R3 |
| Streamlit HMI | Viewer plugin / webview | WRAP |
| `python -m threat_modeler` API | Plugin `entry.api` | WRAP |

### MATM agents (`platform/imports/matm/agents/`)

All 24 `.agent.md` files → merge into platform governance agent registry; dedupe with FarmRTK EIRC/PM roles in R2.

---

## Legacy Agentic-SDLC-AI → Platform

| Legacy module | Action |
|---------------|--------|
| `src/graphs/supervisor.py` | BRIDGE → `src/platform/orchestration/langgraph_adapter.py` |
| `src/gates/*` | MERGE → `src/platform/gates/registry.py` + YAML |
| `src/agents/*` (12) | KEEP core SE agents; domain logic → packs |
| `src/skills/registry.py` | MERGE → `src/platform/plugins/skill_registry.py` |
| Streamlit dashboard | MOVE → `gui/viewers/legacy-streamlit/` |
| Docker Compose | OPTIONAL profile in installer |

---

## GUI / IDE refactor

| Item | Target | Phase |
|------|--------|-------|
| Zed ACP host config | `gui/shell/zed/` | R4 |
| Portable shell abstraction | `src/platform/gui/shell_host.py` | R4 |
| Work-product viewers | `gui/viewers/{markdown,mermaid,stix,icd,graph}/` | R2–R4 |
| Installer | `gui/installer/Install-AgenticPlatform.ps1` | R6 |
| Settings schema | `workspace/templates/platform-settings.schema.json` | R1 |

---

## GitHub integration

| Item | Target | Phase |
|------|--------|-------|
| Actions workflow templates | `plugins/packs/github-devops/workflows/` | R5 |
| PR check bridge | `src/platform/providers/github/` | R5 |
| `gh` CLI tasks | procedural skills in github-devops pack | R5 |

---

## Cross-repo consumption (end state)

```
FarmRTK/          → workspace product only; `.grok/skills` shrinks to farmrtk-pack extensions
MATM/             → threat-modeling plugin source; no governance duplication
Agentic-SDLC-AI/  → platform + installer + packs
```

---

## Revision history

| Rev | Date | Change |
|-----|------|--------|
| 0.1 | 2026-06-06 | Initial refactor map after import scaffold |