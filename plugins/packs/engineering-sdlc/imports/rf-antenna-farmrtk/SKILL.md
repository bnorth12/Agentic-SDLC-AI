---
name: rf-antenna-farmrtk
description: >
  Audit FarmRTK GNSS ground plane RF design — DESIGN.md vs M-01 CAD params,
  antenna seat backlog, diameter reconciliation. RF / Antenna Engineer. Use for
  ground plane RF audit, antenna placement review, or cable routing check.
metadata:
  short-description: "Ground plane RF design audit"
---

# rf-antenna-farmrtk

**Agent:** RF / Antenna Engineer  
**Parent:** [Hardware/Ground-Plane/DESIGN.md](../../../Hardware/Ground-Plane/DESIGN.md) · [Ground_Plane.md](../../../Hardware/cad-parts/Ground_Plane/Ground_Plane.md)

## When to invoke

- M-01 ground plane parameter changes (`disk_d`, thickness)
- Before TC-001 open-sky campaign (R-003 mitigation)
- Antenna seat tolerance vs DFRobot patch (Hardware BACKLOG)
- Cable channel v0.2 CAD work

## Audit

```powershell
powershell -File Tools/ci/rf_ground_plane_audit.ps1
```

Pair with `openscad-parametric-farmrtk` for geometry edits and `csg_smoke.ps1` after SCAD changes.

## Procedure

1. Run audit — resolve DESIGN.md (110 mm) vs CAD `disk_d` (120 mm) after bench C/N0 check.
2. Confirm foil/conductor steps in DESIGN.md section 3 are in assembly notes.
3. Track cable channel (radial slot) — currently deferred in CAD v0.2; do not block print v0.1 disk+stud.
4. Antenna seat: flat top, 0-1 mm air gap; side-exit coax per DESIGN.md section 4.
5. Escalate diameter or keepout conflicts to Chief Engineer + Mechanical Engineer.

## Escalation

- RTK performance risk R-003 → Risk Manager + TC-001 planning
- Mechanical stud/adapter clash → FarmRTK CAD Engineer
- REQ conflict → Requirements Manager