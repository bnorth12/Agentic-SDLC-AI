# Agentic-SDLC-AI — Platform Agent Registry

**Framework:** Plugin-adaptable agentic IDE + hybrid orchestration (procedural, LangGraph, ACP)  
**Charter:** [docs/charter/REBOOT_CHARTER.md](docs/charter/REBOOT_CHARTER.md)  
**Skills:** `platform/imports/` (staging) → `plugins/packs/*/skills/` (target)  
**Platform agents:** [agents/platform/PLATFORM_AGENTS.md](agents/platform/PLATFORM_AGENTS.md)

---

## Supervisor chain (target)

```mermaid
flowchart TB
    WO[Workspace Orchestrator] --> CE[Chief Engineer]
    CE --> PACK[Plugin pack agents]
    EIRC[Independent Review Committee] --> CE
    GATE[Gate engine] --> HITL[Human HITL]
```

---

## HITL governance

| Gate mode | Meaning |
|-----------|---------|
| **mandatory** | Human must approve before proceed |
| **optional** | Agent may proceed; human can intervene |
| **waived** | Auto-pass with evidence log |
| **maturity-gated** | Mandatory at M2+ only |

Gate registry: `platform/gates/registry.yaml`

---

## Slash commands (via Grok Build)

| Command | Skill (target) |
|---------|----------------|
| `/orchestrate-sdlc` | orchestrate-sdlc |
| `/review-sdlc` | independent-review-sdlc |
| `/threat-model` | threat-modeling pack |

---

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 0.2.0 | 2026-06-06 | Platform reboot scaffold; imports from FarmRTK + MATM |
| 0.3.0 | 2026-06 | Added **Planning Agent** and **Refactoring Agent** (in `agents/platform/`) with associated skills (`platform/skills/ide-portfolio-planning` and `ide-structural-refactoring`). These agents were used to produce the full [IDE_REFACTOR_PLAN.md](docs/charter/IDE_REFACTOR_PLAN.md) for turning the repo into the complete agentic AI IDE (editors, viewers, interaction agents, skills, PowerShell+GitHub, hybrid orchestration, packs). All copied MATM/FarmRTK agents are now explicitly in scope for generalization under the new agents. Starter `plugins/packs/ide-platform/` manifest added. |