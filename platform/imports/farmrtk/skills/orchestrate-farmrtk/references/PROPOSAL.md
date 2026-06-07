# Orchestration proposal (executed)

**Status:** Implemented 2026-06-06 as `orchestrate-farmrtk` + `Tools/orchestrate/`

## Problem

FarmRTK documents a LangGraph-style multi-agent SDLC but had no executable router from backlog → agent → skill.

## Solution

| Component | Path | Role |
|-----------|------|------|
| Skill | `.grok/skills/orchestrate-farmrtk/` | Procedure for PM/CE |
| Delegation map | `Tools/orchestrate/delegation_map.json` | Tag → agent → skills |
| Wave planner | `Tools/orchestrate/wave_plan.ps1` | Scans open backlog, writes plan |
| Readiness index | `Docs/System-Level/11-Agent-Readiness.md` | Agent ↔ skill readiness |

## What orchestration is NOT

- Not a standalone Grok subagent type
- Not a running LangGraph server
- Not auto-executing — **HITL G0** approves wave scope

## Success criteria

- [x] One command produces agent/skill assignments for open backlog
- [x] W2 project skills listed in delegation map
- [x] Program Manager + CE documented as orchestration owners