// FarmRTK shared mount library — use with modular templates
// @param_source Hardware/cad-parts/CYD_Large_Display.md

function tab_positions(count, span, inset) =
    count <= 1 ? [span/2] :
    [for (i = [0 : count-1]) inset + i * (span - 2*inset) / (count - 1)];

module standoff(od, id, h) {
    difference() {
        cylinder(h=h, d=od, $fn=32);
        translate([0, 0, -0.1])
            cylinder(h=h+0.2, d=id, $fn=24);
    }
}

module snap_tab(width, depth, height) {
    translate([-width/2, 0, 0])
        cube([width, depth, height]);
}

module snap_notch(width, depth, height, clearance=0.15) {
    translate([-width/2 - clearance, -clearance, -clearance])
        cube([width + 2*clearance, depth + 2*clearance, height + 2*clearance]);
}

module pcb_proxy(w, h, t, hole_xy, hole_d) {
    color("DimGray", 0.35)
    difference() {
        translate([0, 0, 0]) cube([w, h, t]);
        for (p = hole_xy)
            translate([p[0], p[1], -0.1])
                cylinder(h=t+0.2, d=hole_d, $fn=24);
    }
}

module window_bevel(w, h, lip, bevel_deg, clearance) {
    // Inner opening = visible area + 2*touch clearance; outer lip for bezel
    inner_w = w + 2*clearance;
    inner_h = h + 2*clearance;
    bevel_z = tan(bevel_deg) * lip;
    difference() {
        cube([inner_w + 2*lip, inner_h + 2*lip, lip]);
        translate([lip, lip, -0.1])
            cube([inner_w, inner_h, lip + 0.2]);
        // Stylus corner bevel (4 corners)
        for (dx = [0, inner_w], dy = [0, inner_h])
            translate([lip + dx, lip + dy, lip])
                rotate([0, 0, (dx==0 && dy==0) ? 0 : (dx==inner_w && dy==0) ? 90 : (dx==0 && dy==inner_h) ? 270 : 180])
                linear_extrude(height=bevel_z, scale=0.85)
                    polygon(points=[[0,0],[lip,0],[0,lip]]);
    }
}