// [FarmRTK PARAMS BEGIN]
// AUTO-SYNCED - run parse_cad_params.ps1 after editing @part_id@.md
/* [Export] */
PART = "all"; // [all, body]
/* [Visibility] */
SHOW_BASE = true;
// [FarmRTK PARAMS END]

// FarmRTK @part_id@ - parametric part (single-file)
// Params MUST stay at top of file (lines 1-8) for OpenSCAD Customizer

$fn = 48;

module part_body() {
    color("RoyalBlue") cube([10, 10, 10]);
}

if (PART == "all") {
    part_body();
} else {
    part_body();
}

echo(str("FarmRTK @part_id@ PART=", PART));