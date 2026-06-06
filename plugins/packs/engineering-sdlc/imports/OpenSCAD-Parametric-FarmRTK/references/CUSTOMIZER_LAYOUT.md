# OpenSCAD Customizer Layout — Mandatory

**Applies to:** all `Hardware/cad-parts/<PartId>/<PartId>.scad`  
**OpenSCAD target:** 2021.01+ (FarmRTK bench standard)

---

## Rule: parameters are line 1

The **first line** of every part `.scad` MUST be:

```openscad
// [FarmRTK PARAMS BEGIN]
```

Everything else — FarmRTK headers, `@req` tags, usage comments — goes **after** `// [FarmRTK PARAMS END]`.

OpenSCAD Customizer **does not reliably list** variables preceded by long comment blocks. Params buried below headers appear missing in the GUI (no toggles, holes not cut).

---

## Required file order

```openscad
// [FarmRTK PARAMS BEGIN]
// AUTO-SYNCED from <PartId>.md
/* [Group A] */
param_a = 1;
/* [Group B] */
param_b = true;
// [FarmRTK PARAMS END]

// --- FarmRTK header / traceability (comments only) ---
// @part <PartId>  @mechanical_id M-xx
// ...

$fn = 48;

// --- Geometry (agent-authored) ---
module part_body() { ... }
```

| Region | Line position | Editor |
|--------|---------------|--------|
| `PARAMS BEGIN` … `END` | **Top of file** | `parse_cad_params.ps1` |
| Header comments | After `PARAMS END` | Agent |
| `$fn`, modules, CSG | After header | Agent |

---

## Parser enforcement

`parse_cad_params.ps1` SHALL:

1. Patch content between `PARAMS BEGIN` and `END`
2. **Re-order** so the PARAMS block is the first lines of the file (moves any header that was above it to below `PARAMS END`)

Agents MUST run parse after MD param edits and MUST NOT hand-place comments above `PARAMS BEGIN`.

---

## Customizer groups

In Markdown `params` block:

```params
# group Insert hole
ENABLE_FEATURE = true
hole_d = 2.0 // [1:0.1:8]
```

Becomes in SCAD:

```openscad
/* [Insert hole] */
ENABLE_FEATURE = true;
hole_d = 2.0; // [1:0.1:8]
```

---

## Verification

After sync, confirm:

1. Line 1 = `// [FarmRTK PARAMS BEGIN]`
2. OpenSCAD → View → Customizer shows all groups
3. Console `echo()` includes a `FILE_REV` or part id string when debugging stale files

Optional sidecar: `<PartId>.json` parameter presets in the same folder as `<PartId>.scad`.