"""Smoke tests for platform reboot scaffold."""

from pathlib import Path

from src.platform.gates import GateEngine
from src.platform.plugins import PluginLoader
from src.platform.orchestration import OrchestrationRouter, ExecutionMode, WorkPackage
from src.platform.workspace import load_workspace


ROOT = Path(__file__).resolve().parents[2]


def test_gate_engine_loads_registry():
    engine = GateEngine()
    gates = engine.list_gates()
    assert len(gates) >= 5
    assert engine.requires_hitl("G0_wave_charter", maturity="M1")


def test_plugin_loader_discovers_packs():
    loader = PluginLoader()
    packs = loader.discover()
    ids = {p.id for p in packs}
    assert "engineering-sdlc" in ids
    assert "threat-modeling" in ids
    assert "github-devops" in ids


def test_workspace_template_loads():
    path = ROOT / "workspace" / "templates" / "example-farmrtk.workspace.yaml"
    ws = load_workspace(path)
    assert ws.id == "farmrtk-program"
    assert "engineering-sdlc" in ws.packs


def test_orchestration_router_scaffold():
    router = OrchestrationRouter()
    pkg = WorkPackage(id="wp-1", skill_id="traceability-audit-sdlc")
    result = router.execute(pkg)
    assert result["status"] == "scaffold"
    assert router.resolve_mode(pkg) == ExecutionMode.PROCEDURAL