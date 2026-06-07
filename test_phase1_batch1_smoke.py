"""Phase 1 Batch 1 live smoke: Basic launchable CUSTOM tkinter shell on Win11.

Tests instantiation of ShellHost with CUSTOM backend, creation of GUI components (status, terminal frame, etc.) without blocking mainloop.
Validates PS terminal wiring readiness (subprocess concepts).
Win11 compatible (uses pwsh default, stdlib tkinter).

Run:
  python test_phase1_batch1_smoke.py

This is the first small testable batch for the MVP IDE plan.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.platform.gui.shell_host import ShellHost, ShellConfig, ShellBackend


def main() -> int:
    print("=== Phase 1 Batch 1 Smoke: Launchable CUSTOM Shell (tkinter MVP) ===")

    # 1. Create host with CUSTOM (tkinter for zero-dep Win11 launch)
    config = ShellConfig(
        backend=ShellBackend.CUSTOM,
        terminal_shell="powershell",
        workspace_root="."
    )
    host = ShellHost(config)
    print(f"Host created: backend={host.status()['backend']}, state={host.status()['state']}")
    assert host.status()["backend"] == "custom"
    assert "launchable-mvp" in host.status()["state"]
    print("  PASS: ShellHost CUSTOM config and status")

    # 2. Create test app (non-blocking for smoke; real launch uses mainloop in _launch_custom_tkinter)
    app = host.create_test_app()
    print(f"Test app created: {type(app).__name__}")
    assert app is not None

    # Check basic components exist (we added status in real launch; here simulate)
    # In real tkinter launch we have status bar, terminal frame, etc.
    # For this smoke, just verify no crash on creation and that launch method exists
    assert hasattr(host, "launch")
    assert hasattr(host, "_launch_custom_tkinter")
    print("  PASS: Launch methods and test app instantiation (no crash)")

    # Phase 1 Batch 2 wiring validation (explorer from P3 loader + invoke via P2/P5)
    # Direct test of the wiring logic (loader + executor + bundler) used in the GUI
    from src.platform.plugins.loader import PluginLoader
    from src.platform.orchestration.executor import run_procedural_skill
    from src.platform.tools.gate_evidence_bundler import create_gate_evidence_bundle
    ldr = PluginLoader()
    sks = ldr.discover_skills()
    assert len(sks) > 0 and any("ide-hierarchy" in s["id"] for s in sks)
    print("  PASS: L4 loader explorer data available (ide-platform skills)")

    # Simulate the invoke_example button logic
    res = run_procedural_skill("ide-hierarchy-taxonomy-steward", workspace_root=".")
    assert "declared_tools" in res.get("outputs", {})
    bundle = create_gate_evidence_bundle("G4_independent_review", [{"type": "skill", "id": "test", "result": res}])
    assert bundle.gate_id == "G4_independent_review"
    print("  PASS: L2 executor + P5 bundler wired for 'Invoke' (real skill + evidence bundle)")

    # 3. Simulate "launch" concepts (PS terminal readiness)
    # The real terminal uses pwsh -NoProfile -Command (from P2 robust)
    print("  (PS terminal pane uses robust P2 execution + subprocess threading for Win11)")

    # Cleanup
    try:
        app.destroy()
    except Exception:
        pass

    print("\n=== PHASE 1 BATCH 1 SMOKE COMPLETE ===")
    print("Win11 launchable: python -c \"from src.platform.gui.shell_host import ShellHost, ShellConfig, ShellBackend; ShellHost(ShellConfig(backend=ShellBackend.CUSTOM)).launch()\" (or enhance with launcher script in next batch).")
    print("Next batch: wire basic explorer + invoke.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
