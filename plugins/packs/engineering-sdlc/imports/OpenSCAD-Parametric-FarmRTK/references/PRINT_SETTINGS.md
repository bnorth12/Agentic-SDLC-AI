# FarmRTK OpenSCAD Print Settings

**Parent:** SYS-REQ-006, TC-006 · Material: PETG or ABS outdoor

---

## Defaults (CYD mount / bezel)

| Setting | Base / mount | Bezel / thin walls |
|---------|--------------|-------------------|
| Material | PETG | PETG |
| Layer height | 0.2 mm | 0.2 mm |
| Perimeters | 4 | 4 |
| Infill | 20% gyroid | 15% gyroid |
| Orientation | Base flat on bed | Front face down (bezel lip up) |
| Brim | 8 mm if tall | 5 mm |
| Support | None if designed split | None |

## Snap-fit tuning

- First print: `snap_tab_oversize = 0.0`
- Too loose: +0.05 mm tab width per edge
- Too tight: −0.05 mm or increase `fit_clearance`

## Field ruggedness

- `wall_thickness` ≥ 2.4 mm for staff mounts (M-08)
- Drain holes: print with hole axis vertical
- XT30 / panel cutouts: print test slice in PLA before PETG commit

## OpenSCAD CLI (PowerShell)

```powershell
openscad -o Hardware/Rover-Housing/STL/cyd_mount_v0.1.stl `
  Hardware/cad-parts/output/FarmRTK_CYD_Mount_Parametric.scad `
  -D 'PART="base"'
```

Use `-D 'PART="bezel"'` for separate STL exports.