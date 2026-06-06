// REFERENCE — FarmRTK single-file parametric mount pattern
// New parts: use templates/part.scad + init_cad_part.ps1
// Params live at top inside // [FarmRTK PARAMS BEGIN/END] — synced from <PartId>.md

// [FarmRTK PARAMS BEGIN]
/* [Export] */
PART = "all"; // [all, base, bezel, proxy]
/* [Visibility] */
SHOW_BASE = true;
SHOW_BEZEL = true;
SHOW_PCB_PROXY = false;
/* [Dimensions] */
pcb_w = 86.0;
pcb_h = 50.0;
pcb_thickness = 3.2;
touch_clearance_mm = 0.7;
// [FarmRTK PARAMS END]

$fn = 48;

module render_part() {
    if (PART == "base" || PART == "all") if (SHOW_BASE) children(0);
    if (PART == "bezel" || PART == "all") if (SHOW_BEZEL) translate([90,0,0]) children(1);
    if (PART == "proxy" || PART == "all") if (SHOW_PCB_PROXY) translate([0,60,0]) children(2);
}

render_part() {
    color("RoyalBlue") cube([10,10,10]);
    color("Orange") cube([10,10,5]);
    color("DimGray", 0.4) cube([pcb_w, pcb_h, pcb_thickness]);
}

echo(str("FarmRTK reference — PART=", PART, " pcb=", pcb_w, "x", pcb_h));