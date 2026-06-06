---
name: data-storage-farmrtk
description: >
  Audit FarmRTK SD card layout — DATA-STORAGE.md vs sd_paths.h macros and CSV
  headers. Data Manager. Use for data storage audit, SD schema change, or
  field verification path check.
metadata:
  short-description: "SD layout doc vs header audit"
---

# data-storage-farmrtk

**Agent:** Data Manager  
**Parent:** [DATA-STORAGE.md](../../../Software/DATA-STORAGE.md) · [05-Data-Storage-and-Field-Verification-Plan.md](../../../Docs/System-Level/05-Data-Storage-and-Field-Verification-Plan.md)

## When to invoke

- Before firmware changes to rover logging or positions CSV
- Field kit prep — verify `/FarmRTK/` layout on microSD
- SYS-DOC-05 phase tracking in segment backlogs

## Audit

```powershell
powershell -File Tools/ci/data_storage_audit.ps1
```

Use `-Enforce` or `FARMRTK_ENFORCE_CHECKS=1` to fail on missing artifacts (M2+).

## Procedure

1. Run audit — align [sd_paths.h](../../../Segments/Shared/Software/lib/FarmRTK_Sd/src/sd_paths.h) macros with DATA-STORAGE.md path table.
2. On schema change: update header, DATA-STORAGE.md, and any firmware writers; run golden NMEA / logging bench if rover paths touched.
3. Coordinate with Firmware Engineer for CSV header constants (`FARMRTK_POSITIONS_HEADER`, `FARMRTK_POINTS_HEADER`).
4. Notify V&V Lead if verification artifacts reference changed paths.

## Escalation

- REQ conflict on field data → Requirements Manager + `requirements-management-farmrtk`
- Bench logging failure → Integration Engineer + `integration-bench-farmrtk`