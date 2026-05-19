"""Smoke tests for sprint 4 skill integration path."""

from __future__ import annotations

from src.graphs.supervisor import apply_skill_binding_hook
from src.state.schema import AgentState, Phase, Requirement


def test_skills_smoke_executes_bound_skills_and_merges_evidence() -> None:
    state = AgentState(
        objective="skills smoke",
        phase=Phase.REQUIREMENTS,
        requirements={
            "REQ-001": Requirement(
                id="REQ-001",
                text="The system shall provide auditable skill execution evidence",
                category="functional",
                priority="high",
                verification_method="test",
                created_by="test",
            )
        },
    )

    updates = {
        "phase": Phase.REQUIREMENTS,
        "gate_readiness": {"gate": "gate_2", "status": "READY"},
        "traceability_links": [
            {
                "requirement_id": "REQ-001",
                "artifacts": ["requirements_baseline", "requirements_traceability_matrix"],
            }
        ],
        "evidence_links": {
            "requirements_baseline": "in_state:requirements",
            "requirements_traceability_matrix": "in_state:requirements_traceability",
            "open_issues": "in_state:open_issues:none",
        },
        "requires_human_approval": False,
    }

    result = apply_skill_binding_hook(state, updates, "requirements_agent")

    assert "SKILL-REQ-QUALITY" in result["skill_outputs"]
    assert "SKILL-TRACEABILITY" in result["skill_outputs"]
    assert result["skill_execution"][0]["required"] is True
    assert result["skill_execution"][1]["required"] is False
    assert result["evidence_links"]["skill_execution_log"].startswith("in_state:skill_execution")
    assert result["phase"] == Phase.REQUIREMENTS
    assert result["requires_human_approval"] is False
