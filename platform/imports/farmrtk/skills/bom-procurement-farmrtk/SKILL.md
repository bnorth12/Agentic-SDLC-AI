---
name: bom-procurement-farmrtk
description: >
  Audit FarmRTK BOM pending lines vs PROC: backlog items; track connector and
  CYD variant orders. Procurement Coordinator. Use for BOM procurement audit,
  PROC backlog sync, or alternates review.
metadata:
  short-description: "BOM vs PROC backlog audit"
---

# bom-procurement-farmrtk

**Agent:** Procurement Coordinator  
**Parent:** [BOM-Full.md](../../../BOM/BOM-Full.md) · [BACKLOG.md](../../../BACKLOG.md)

## When to invoke

- Before hardware waves that need connectors or second CYD
- Monthly procurement review with Program Manager
- After BOM § Pending edits

## Audit

```powershell
powershell -File Tools/ci/bom_procurement_audit.ps1
```

## Procedure

1. Run audit — reconcile BOM pending connector rows with open `PROC:` items in root [BACKLOG.md](../../../BACKLOG.md) and segment backlogs.
2. For each pending BOM line, ensure a matching `PROC:` checkbox exists (or close the BOM line when ordered).
3. Document CYD vs Hosyond variant choice in BOM 2.1 notes; escalate alternates to Chief Engineer.
4. When orders ship, update BOM status and close `PROC:` rows; notify Configuration Manager before baseline tag.

## Escalation

- Lead-time block on wave scope → Program Manager + G0 wave doc
- BOM ↔ mechanical conflict → Chief Engineer + Mechanical Engineer