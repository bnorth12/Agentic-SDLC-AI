"""Unit tests for requirements quality skill."""

from __future__ import annotations

from src.config.skills import SkillBindingPolicy
from src.skills.requirements_quality import run_requirements_quality_skill
from src.state.schema import AgentState, Requirement


def _policy() -> SkillBindingPolicy:
    return SkillBindingPolicy(
        agent_role="requirements_agent",
        gate="gate_2",
        discipline="requirements",
        skill_id="SKILL-REQ-QUALITY",
        version="1.0.0",
        required=True,
    )


def test_requirements_quality_passes_valid_requirements() -> None:
    state = AgentState(objective="quality skill")
    updates = {
        "requirements": {
            "REQ-001": Requirement(
                id="REQ-001",
                text="The system shall enforce requirement quality checks",
                category="functional",
                priority="high",
                verification_method="test",
                created_by="test",
            )
        }
    }

    result = run_requirements_quality_skill(state, updates, _policy())

    assert result["status"] == "ready"
    assert result["violations"] == []
    assert result["requirement_count"] == 1


def test_requirements_quality_reports_format_and_field_violations() -> None:
    state = AgentState(objective="quality skill")
    updates = {
        "requirements": {
            "REQ-001": {
                "id": "REQ-001",
                "text": "System must be validated",
                "category": "",
                "priority": "high",
                "verification_method": "test",
            }
        }
    }

    result = run_requirements_quality_skill(state, updates, _policy())

    assert result["status"] == "blocked"
    rules = {item["rule"] for item in result["violations"]}
    assert "noun_shall_verb" in rules
    assert "mandatory_field" in rules


def test_requirements_quality_reports_missing_parent() -> None:
    state = AgentState(objective="quality skill")
    updates = {
        "requirements": {
            "REQ-001": {
                "id": "REQ-001",
                "text": "The system shall validate hierarchy links",
                "category": "functional",
                "priority": "high",
                "verification_method": "analysis",
                "parent_id": "REQ-999",
            }
        }
    }

    result = run_requirements_quality_skill(state, updates, _policy())

    assert result["status"] == "blocked"
    assert any(item["rule"] == "hierarchy_parent_exists" for item in result["violations"])
