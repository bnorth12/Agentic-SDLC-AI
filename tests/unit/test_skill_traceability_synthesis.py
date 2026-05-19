"""Unit tests for traceability synthesis skill."""

from __future__ import annotations

from src.config.skills import SkillBindingPolicy
from src.skills.traceability_synthesis import run_traceability_synthesis_skill
from src.state.schema import AgentState


def _policy() -> SkillBindingPolicy:
    return SkillBindingPolicy(
        agent_role="requirements_agent",
        gate="gate_2",
        discipline="traceability",
        skill_id="SKILL-TRACEABILITY",
        version="1.0.0",
        required=False,
    )


def test_traceability_synthesis_reports_ready_when_all_requirements_linked() -> None:
    state = AgentState(objective="traceability")
    updates = {
        "requirements": {
            "REQ-001": {"id": "REQ-001"},
            "REQ-002": {"id": "REQ-002"},
        },
        "traceability_links": [
            {"requirement_id": "REQ-001", "artifacts": ["req_baseline", "rtm"]},
            {"requirement_id": "REQ-002", "artifacts": ["rtm"]},
        ],
    }

    result = run_traceability_synthesis_skill(state, updates, _policy())

    assert result["status"] == "ready"
    assert result["missing_links"] == []
    assert result["trace_links_count"] == 3


def test_traceability_synthesis_reports_missing_links() -> None:
    state = AgentState(objective="traceability")
    updates = {
        "requirements": {
            "REQ-001": {"id": "REQ-001"},
            "REQ-002": {"id": "REQ-002"},
        },
        "traceability_links": [
            {"requirement_id": "REQ-001", "artifacts": ["req_baseline"]},
        ],
    }

    result = run_traceability_synthesis_skill(state, updates, _policy())

    assert result["status"] == "blocked"
    assert result["missing_links"] == ["REQ-002"]
