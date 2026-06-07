---
name: traceability-audit-farmrtk
description: >
  Audit FarmRTK repo-native traceability: orphan REQ/TC IDs, broken markdown
  links, cad-part frontmatter. No DOORS/Jama. Use for traceability audit,
  REQ coverage check, or Traceability Manager workflow.
metadata:
  short-description: "Repo traceability audit (markdown matrices)"
---

# traceability-audit-farmrtk

**Agent:** Traceability Manager  
**Parent:** [Docs/System-Level/README.md](../../../Docs/System-Level/README.md) (INCOSE relationships)

## When to invoke

- Quarterly or before EIRC M-G1 (requirements freeze)
- After bulk REQ or backlog edits
- User: "traceability audit", "orphan REQ scan"

## Steps

1. Full repo scan:

```powershell
powershell -File Tools/ci/traceability_audit.ps1
```

2. Staged-only (pre-commit supplement):

```powershell
powershell -File Tools/ci/traceability_audit.ps1 -StagedOnly
```

3. Fix orphan IDs in `Docs/System-Level/01-System-Requirements.md` or remove typos.
4. Update parent/child matrix rows in the same PR as implementation.
5. Re-run until warnings = 0 or documented TBD at current M-phase.

## Enforce

```powershell
$env:FARMRTK_ENFORCE_CHECKS = "1"
powershell -File Tools/ci/traceability_audit.ps1
```

## Outputs

Stdout WARN/FAIL lines; no external database export.