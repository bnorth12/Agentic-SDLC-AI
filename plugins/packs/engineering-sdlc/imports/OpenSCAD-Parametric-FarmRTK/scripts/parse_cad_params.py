#!/usr/bin/env python3
"""Sync Markdown params block into the PARAMS section of a single-part .scad file."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

BEGIN = "// [FarmRTK PARAMS BEGIN]"
END = "// [FarmRTK PARAMS END]"


def parse_params_block(text: str) -> tuple[str, list[str]]:
    part_id = "Unknown"
    fm = re.search(r"^---\s*\n(.*?)\n---", text, re.M | re.S)
    if fm:
        m = re.search(r"part_id:\s*(\S+)", fm.group(1))
        if m:
            part_id = m.group(1)
    block = re.search(r"```params\s*\n(.*?)```", text, re.S)
    if not block:
        raise SystemExit("No ```params block in part file")

    lines = [
        f"// AUTO-SYNCED from part markdown",
        f"// part_id: {part_id} — edit {part_id}.md then re-run parse_cad_params",
        "",
    ]
    for raw in block.group(1).splitlines():
        line = raw.strip()
        if not line or line.startswith("//"):
            continue
        gm = re.match(r"^#\s*group\s+(.+)$", line)
        if gm:
            lines.append(f"/* [{gm.group(1).strip()}] */")
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+)$", line)
        if not m:
            continue
        key, rest = m.group(1), m.group(2)
        cm = re.match(r"^(.+?)\s*//\s*(.+)$", rest)
        if cm:
            val = cm.group(1).rstrip(";").strip()
            comment = cm.group(2).strip()
            lines.append(f"{key} = {val}; // {comment}")
        else:
            val = rest.rstrip(";").strip()
            lines.append(f"{key} = {val};")
    return part_id, lines


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("part_file", type=Path)
    ap.add_argument("--scad-file", type=Path, default=None)
    args = ap.parse_args()

    part_path = args.part_file.resolve()
    text = part_path.read_text(encoding="utf-8")
    part_id, param_lines = parse_params_block(text)
    param_lines[0] = f"// AUTO-SYNCED from {part_path.as_posix()}"

    scad_path = args.scad_file or part_path.parent / f"{part_id}.scad"
    params_block = "\n".join(param_lines)
    new_block = f"{BEGIN}\n{params_block}\n{END}"

    template = Path(__file__).resolve().parent.parent / "templates" / "part.scad"
    if not scad_path.exists():
        if not template.exists():
            raise SystemExit(f"SCAD not found ({scad_path}) and no template at {template}")
        stub = template.read_text(encoding="utf-8")
        stub = stub.replace("@part_id@", part_id)
        stub = stub.replace("@param_source@", str(part_path))
        stub = stub.replace("@mechanical_id@", "M-XX")
        stub = stub.replace("@req@", "SYS-REQ-006")
        if re.search(r"// \[FarmRTK PARAMS BEGIN\].*?// \[FarmRTK PARAMS END\]", stub, re.S):
            stub = re.sub(
                r"// \[FarmRTK PARAMS BEGIN\].*?// \[FarmRTK PARAMS END\]",
                new_block,
                stub,
                flags=re.S,
            )
        else:
            stub = f"{stub}\n{new_block}\n"
        scad_path.parent.mkdir(parents=True, exist_ok=True)
        scad_path.write_text(stub, encoding="utf-8")
        print(f"Created {scad_path} from template ({len(param_lines)} param lines)")
        return

    scad_content = scad_path.read_text(encoding="utf-8")
    if not re.search(r"// \[FarmRTK PARAMS BEGIN\].*?// \[FarmRTK PARAMS END\]", scad_content, re.S):
        raise SystemExit(f"Missing PARAMS markers in {scad_path}")
    scad_content = re.sub(
        r"// \[FarmRTK PARAMS BEGIN\].*?// \[FarmRTK PARAMS END\]",
        new_block,
        scad_content,
        flags=re.S,
    )
    scad_path.write_text(scad_content, encoding="utf-8")
    print(f"Synced params into {scad_path} ({len(param_lines)} lines)")


if __name__ == "__main__":
    main()