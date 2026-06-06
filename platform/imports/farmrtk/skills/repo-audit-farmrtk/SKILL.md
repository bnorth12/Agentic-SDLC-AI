---
name: repo-audit-farmrtk
description: >
  FarmRTK repo organization audit — README coverage, BACKLOG index, plus
  traceability scan. Repo Organization Manager. Use for repo audit or folder
  hygiene check.
metadata:
  short-description: "Repo README and backlog audit"
---

# repo-audit-farmrtk

**Agent:** Repo Organization Manager

## Steps

1. `powershell -File Tools/ci/repo_audit.ps1`
2. Fix missing top-level READMEs (RH-01).
3. Update root [BACKLOG.md](../../../BACKLOG.md) segment index if needed.
4. Run `program-metrics-farmrtk` after remediation.