// Modular base only — include params + lib
// Usage: openscad -D 'PART="base"' modular_base.scad

include <../../../Hardware/cad-parts/output/CYD_Large_Display_params.scad>
use <lib_farmrtk_mount.scad>

module farmrtk_base() {
    inner_w = pcb_w + 2*fit_clearance;
    inner_h = pcb_h + 2*fit_clearance;
    outer_w = inner_w + 2*wall_thickness;
    outer_h = inner_h + 2*wall_thickness;

    difference() {
        union() {
            translate([-wall_thickness, -wall_thickness, 0])
                cube([outer_w, outer_h, base_thickness + back_max_z]);
            for (p = hole_xy)
                translate([p[0], p[1], base_thickness])
                    standoff(standoff_od, standoff_id, standoff_h);
            // Snap tabs — top edge (y = pcb_h)
            for (x = tab_positions(tabs_top_count, pcb_w, tabs_edge_inset))
                translate([x, pcb_h - snap_tab_depth, base_thickness + back_max_z])
                    snap_tab(snap_tab_width, snap_tab_depth, snap_tab_height);
            for (x = tab_positions(tabs_bottom_count, pcb_w, tabs_edge_inset))
                translate([x, 0, base_thickness + back_max_z])
                    rotate([0, 0, 180]) snap_tab(snap_tab_width, snap_tab_depth, snap_tab_height);
        }
        translate([usb_slot_center_x - usb_slot_w/2, -0.1, base_thickness])
            cube([usb_slot_w, usb_slot_h + 0.2, back_max_z + 1]);
        translate([pcb_w - sd_slot_right_offset - sd_slot_w, pcb_h/2 - sd_slot_h/2, base_thickness])
            cube([sd_slot_w + 0.5, sd_slot_h, back_max_z + 1]);
    }
}

farmrtk_base();