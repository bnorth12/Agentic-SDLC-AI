// Modular bezel only — snap notches + touch-safe window
include <../../../Hardware/cad-parts/output/CYD_Large_Display_params.scad>
use <lib_farmrtk_mount.scad>

module farmrtk_bezel() {
    frame_w = display_vis_w + 2*touch_clearance_mm + 2*bezel_lip_thickness;
    frame_h = display_vis_h + 2*touch_clearance_mm + 2*bezel_lip_thickness;
    bezel_depth = 8;

    translate([display_offset_x - touch_clearance_mm - bezel_lip_thickness,
                 display_offset_y - touch_clearance_mm - bezel_lip_thickness,
                 base_thickness + back_max_z + pcb_thickness])
    difference() {
        union() {
            cube([frame_w, frame_h, bezel_depth]);
            // Matching notches
            for (x = tab_positions(tabs_top_count, pcb_w, tabs_edge_inset))
                translate([x - (display_offset_x - touch_clearance_mm - bezel_lip_thickness),
                           pcb_h - display_offset_y + touch_clearance_mm + bezel_lip_thickness - snap_tab_depth,
                           0])
                    snap_notch(snap_tab_width, snap_tab_depth, snap_tab_height);
        }
        translate([bezel_lip_thickness, bezel_lip_thickness, -0.1])
            cube([display_vis_w + 2*touch_clearance_mm,
                  display_vis_h + 2*touch_clearance_mm,
                  bezel_depth + 0.2]);
    }
}

farmrtk_bezel();