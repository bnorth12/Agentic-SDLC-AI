# Geometry Intent — Required MD Section

Add to every `Hardware/cad-parts/<PartId>/<PartId>.md` after **Requirements**.

Agents SHALL implement geometry to match this section. If intent conflicts with a param, fix geometry and propose param update.

---

## Template

```markdown
## Geometry Intent

### PART=base (export body)
- **Plate:** flat slab `base_plate_thickness` mm; no perimeter wall box
- **Top surface:** Z = `base_plate_thickness` — tabs and standoffs start here
- **Tabs:** male snap tabs; height `snap_tab_height` above plate top only
- **Standoffs:** at `hole_xy`; total height `standoff_h` above plate top
- **Cutouts:** USB/SD through plate edge only

### PART=bezel (export body)
- **Frame:** flat ring; thickness `bezel_body_h`
- **Window:** through-hole `display + 2*touch_clearance`; must be empty
- **Inner chamfer:** SUBTRACTIVE at top inner edge; angle `stylus_bevel_deg`
- **Glass lip:** underside ring overlaps passive glass `bezel_glass_overlap` mm; does not reduce touch opening
- **Seat:** bottom face at PCB top (computed Z from base stack)

### PART=proxy
- PCB solid + `%` display outline for collision check

### Assembly (PART=all)
- Bodies separated in X for preview; Z stack per comments in .scad
```

---

## Anti-patterns (do not implement)

- Bezel chamfer as `union()` + `linear_extrude(scale<1)` on top of window
- Base as plate + full-height `back_max_z` wall cube (unless intent says enclosure)
- Tabs starting above a fictional wall — tabs seat on plate top