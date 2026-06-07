# CAD Part Parameter Schema

**Parent:** `Hardware/cad-parts/<PartId>/`  
**Consumer:** `parse_cad_params.ps1`, FarmRTK CAD Engineer agent

---

## Directory layout (one part = one output)

```
Hardware/cad-parts/
  _template/
    part.md
  <PartId>/
    <PartId>.md       # Human + agent source of truth
    <PartId>.scad     # Single render file (params at top + geometry)
    STL/              # Local exports (gitignored)
```

**Do not** split params into a separate `*_params.scad` include. The parser patches the PARAMS block inside `<PartId>.scad`.

---

## Frontmatter (YAML)

```yaml
---
part_id: CYD_Large_Display
mechanical_id: M-08
variant: ESP32-2432S028R
units: mm
req: ROVER-REQ-003, UI-REQ-016
param_source: caliper + witnessmenow CYD community dims
status: draft
---
```

`part_id` MUST match directory name and `.scad` basename.

---

## Section: Critical Measurements

Narrative + table for humans. Parser ignores unless duplicated in **OpenSCAD Parameters**.

---

## Section: OpenSCAD Parameters

Machine-readable block inside ` ```params ` fence.

```markdown
## OpenSCAD Parameters

```params
# group Export
PART = "all" // [all, base, bezel, proxy]
# group PCB
pcb_w = 86.0
hole_xy = [[3.5, 3.5], [82.5, 3.5], [82.5, 46.5], [3.5, 46.5]]
```
```

| Syntax | Effect in `.scad` |
|--------|------------------|
| `# group Name` | `/* [Name] */` Customizer section |
| `key = val // [a, b, c]` | Dropdown hint for strings |
| `float`, `int`, `bool`, `array` | Standard OpenSCAD types |

---

## SCAD PARAMS markers (line 1)

**Mandatory:** `// [FarmRTK PARAMS BEGIN]` is the **first line** of `<PartId>.scad`.  
Full rules: [CUSTOMIZER_LAYOUT.md](CUSTOMIZER_LAYOUT.md)

```openscad
// [FarmRTK PARAMS BEGIN]
/* [Export] */
PART = "all"; // [all, base, bezel, proxy]
...
// [FarmRTK PARAMS END]

// FarmRTK header comments (@part, @req) — ONLY below PARAMS END
// Geometry below — agent-authored, not overwritten by parser
```

**Anti-pattern:** comments or headers above `PARAMS BEGIN` → OpenSCAD Customizer hides variables.

---

## Parser

```powershell
Tools/cad/parse_cad_params.ps1 -PartFile Hardware/cad-parts/<PartId>/<PartId>.md
```

- Patches `// [FarmRTK PARAMS BEGIN]` … `END` in `<PartId>/<PartId>.scad`
- **Re-orders** file so PARAMS block is always line 1 (moves stray header above it to below `END`)
- Creates `.scad` from `templates/part.scad` if missing
- UTF-8 without BOM

---

## New part scaffold

```powershell
Tools/cad/init_cad_part.ps1 -PartId Pack_Box -MechanicalId M-09
```

---

## Version History

Required in every `<PartId>.md`. Bump when caliper values or geometry intent changes.