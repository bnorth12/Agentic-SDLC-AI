"""Win11 launch entry for Agentic IDE MVP (Phase 4 packaging/validation).

Usage (from repo root):
  python -m src.platform.gui.launch_ide
  or
  python src/platform/gui/launch_ide.py

Launches the CUSTOM tkinter shell (L0) with full Phase 1-3 surfaces:
- Explorer (L4 loader)
- PS terminal (P2 robust)
- Editor + Invoke (L2 executor)
- Viewers (P5 bundler md/json)
- Status with gates (L3)
- Self-hosting demo via real generalized skills (P1-P5 tools wired).

PS is primary execution. Custom unique impl (tkinter stdlib for initial; no source reuse).

For full production: evolve CUSTOM to Dear PyGui / Tauri per GUI_DESIGN.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure root on path when run directly
ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.gui.shell_host import ShellHost, ShellConfig, ShellBackend


def main() -> None:
    print("Launching Agentic IDE MVP on Windows 11 (CUSTOM tkinter shell)...")
    print("  - Explorer, Editor, Viewers, PS Terminal, Governance wired to P1-P5 tools + L2/L3/L4.")
    print("  - Self-hosting: invoke generalized skills from this platform (e.g. ide-hierarchy).")
    print("  - Close window to exit.")
    config = ShellConfig(
        backend=ShellBackend.CUSTOM,
        terminal_shell="powershell",
        workspace_root=".",
    )
    host = ShellHost(config)
    host.launch()


if __name__ == "__main__":
    main()
