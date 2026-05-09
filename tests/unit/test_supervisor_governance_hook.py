"""Unit tests for supervisor governance gate hook behavior."""

from __future__ import annotations

from src.graphs.supervisor import apply_governance_gate_hook
from src.state.schema import AgentState, Phase


def _base_ready_update() -> dict:
    return {
        "phase": Phase.ARCHITECTURE,
        "gate_readiness": {"gate": "gate_2", "status": "READY"},
        "policy_compliance": {"status": "PASS", "policies": ["RMP-001"]},
        "traceability_links": [
            {"requirement_id": "REQ-001", "artifacts": ["requirements-baseline-v1"]}
        ],
        "evidence_links": {
            "requirements_baseline": "docs/artifacts/requirements-baseline-v1.md",
            "requirements_traceability_matrix": "docs/artifacts/rtm-v1.csv",
            "open_issues": "docs/artifacts/open-issues.md",
        },
        "risks_or_blockers": [],
        "messages": ["candidate update"],
    }


def test_hook_allows_ready_transition_with_complete_evidence() -> None:
    state = AgentState(objective="Validate gate hook")
    updates = _base_ready_update()

    result = apply_governance_gate_hook(state, updates, "requirements_agent")

    assert result["gate_readiness"]["status"] == "READY"
    assert result["phase"] == Phase.ARCHITECTURE
    assert result["governance_validation"]["gate_can_be_marked_ready"] is True


def test_hook_blocks_ready_transition_with_missing_evidence() -> None:
    state = AgentState(objective="Validate gate hook")
    updates = _base_ready_update()
    del updates["evidence_links"]["open_issues"]

    result = apply_governance_gate_hook(state, updates, "requirements_agent")

    assert result["gate_readiness"]["status"] == "NOT_READY"
    assert "phase" not in result
    assert result["requires_human_approval"] is True
    assert result["governance_validation"]["gate_can_be_marked_ready"] is False


def test_hook_ignores_non_ready_updates() -> None:
    state = AgentState(objective="No ready status")
    updates = {
        "phase": Phase.REQUIREMENTS,
        "gate_readiness": {"gate": "gate_1", "status": "NOT_READY"},
        "messages": ["still working"],
    }

    result = apply_governance_gate_hook(state, updates, "program_manager")

    assert result == updates
