# CAD Iteration Loop — FarmRTK OpenSCAD

Use this loop when geometry is wrong in preview or after first print.

---

## 1. Document intent before coding

Every `<PartId>.md` MUST include **## Geometry Intent** (see [GEOMETRY_INTENT.md](GEOMETRY_INTENT.md)).

Agents read intent first. Numbers alone do not define subtractive chamfers, plate vs wall, or tab seat height.

---

## 2. OpenSCAD GUI cache (common)

If Customizer shows **old params** or **no hole** after an agent update:

1. **Close OpenSCAD completely** (not just a new window)
2. Reopen the `.scad` from `Hardware/cad-parts/<PartId>/`
3. **File → Reload** if the file stayed open during edits
4. Confirm `FILE_REV` or console echo matches the latest version

Opening a new window first, then the updated file, can reload a **cached** older compile state.

---

## 3. Isolate the body

```powershell
# GUI — Customizer PART dropdown, or:
powershell -File Tools/cad/preview_part.ps1 `
  -ScadFile Hardware/cad-parts/CYD_Large_Display/CYD_Large_Display.scad `
  -Part bezel

powershell -File Tools/cad/preview_part.ps1 `
  -ScadFile Hardware/cad-parts/CYD_Large_Display/CYD_Large_Display.scad `
  -Part base -Render
```

| PART | Inspect |
|------|---------|
| `base` | Plate thickness, tab height above plate, cutouts |
| `bezel` | Through-hole, inner chamfer, glass lip ring |
| `proxy` | PCB + display outline vs bezel hole |
| `all` | Assembly stack Z heights only |

---

## 4. Describe the defect (HITL feedback template)

Copy into chat or part MD **## Open Issues**:

```
Body: bezel
Expected: through opening; 25 deg inner chamfer as CUT; lip overlaps glass passive margin
Actual: solid frustum in hole; chamfer on 2 sides only; no lip
Suspect: union() added chamfer solid instead of difference() subtraction
```

Agents MUST map feedback → CSG operation (union vs difference, extrude direction, seat Z).

---

## 5. Fix → preview → repeat

1. Confirm **line 1** = `// [FarmRTK PARAMS BEGIN]` ([CUSTOMIZER_LAYOUT.md](CUSTOMIZER_LAYOUT.md))
2. Edit geometry **below** header comments after `// [FarmRTK PARAMS END]` only
2. If dims change, edit MD `params` → `parse_cad_params.ps1`
3. `preview_part.ps1 -Part <body>` (agent runs this; do not ask user to run)
4. Optional GUI: `open_in_openscad.ps1` — F5 preview, F6 export single body
5. User confirms G2 → `export_stl.ps1`

---

## 6. Agent rules for CSG

| Pattern | Use |
|---------|-----|
| `difference() { plate(); cutout(); }` | Holes, windows, chamfers |
| `union() { plate(); tabs(); }` | Add protrusions above a seat surface |
| `linear_extrude(h, scale>1)` inside **difference** | Widen hole toward top = inner chamfer |
| `linear_extrude(h, scale<1)` inside **union** on top of hole | WRONG — plugs the opening |

---

## 7. Z-stack checklist (assembly parts)

Echo or comment expected stack in SCAD:

```
plate_top_z = base_plate_thickness
pcb_bottom_z = plate_top_z + standoff_h
bezel_bottom_z = pcb_bottom_z + pcb_thickness
```

Verify with `SHOW_PCB_PROXY = true` and `PART = all`.

---

## 8. Version history

Bump part MD version when geometry intent or caliper dims change after a fit iteration.