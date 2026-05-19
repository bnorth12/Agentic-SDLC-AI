"""Unit tests for skill registry behavior and deterministic resolution."""

from __future__ import annotations

import pytest

from src.skills.contracts import validate_skill_contract
from src.skills.registry import SkillBinding, SkillRegistry


def _contract(version: str) -> dict:
    return {
        "metadata": {
            "skill_id": "SKILL-REQ-QUALITY",
            "name": "Requirements Quality Skill",
            "discipline": "requirements",
            "version": version,
            "owner_roles": ["requirements_agent"],
        },
        "inputs_required": ["requirements"],
        "artifacts_produced": ["requirements_quality_report"],
        "policy_checks": ["RMP-001"],
        "traceability_links": ["AGT-0110"],
        "confidence_score": 0.85,
        "escalation_conditions": ["invalid_format"],
        "output_schema": {
            "violations": "list[str]",
        },
    }


def test_registry_register_and_get_contract() -> None:
    registry = SkillRegistry()
    contract = validate_skill_contract(_contract("1.0.0"))

    registry.register(contract)

    loaded = registry.get("SKILL-REQ-QUALITY", "1.0.0")
    assert loaded.metadata.version == "1.0.0"


def test_registry_rejects_duplicate_skill_version() -> None:
    registry = SkillRegistry()
    contract = validate_skill_contract(_contract("1.0.0"))

    registry.register(contract)
    with pytest.raises(ValueError, match="Duplicate skill registration"):
        registry.register(contract)


def test_registry_resolves_highest_semver_for_binding() -> None:
    registry = SkillRegistry()
    v1 = validate_skill_contract(_contract("1.0.0"))
    v2 = validate_skill_contract(_contract("1.1.0"))

    registry.register(v1)
    registry.register(v2)

    registry.bind(
        SkillBinding(
            agent_role="requirements_agent",
            gate="gate_2",
            discipline="requirements",
            skill_id="SKILL-REQ-QUALITY",
            version="1.0.0",
        )
    )
    registry.bind(
        SkillBinding(
            agent_role="requirements_agent",
            gate="gate_2",
            discipline="requirements",
            skill_id="SKILL-REQ-QUALITY",
            version="1.1.0",
        )
    )

    resolved = registry.resolve("requirements_agent", "gate_2", "requirements")

    assert resolved is not None
    assert resolved.metadata.version == "1.1.0"


def test_registry_ignores_deprecated_bindings_during_resolution() -> None:
    registry = SkillRegistry()
    v1 = validate_skill_contract(_contract("1.0.0"))
    v2 = validate_skill_contract(_contract("1.1.0"))

    registry.register(v1)
    registry.register(v2)

    common = {
        "agent_role": "requirements_agent",
        "gate": "gate_2",
        "discipline": "requirements",
        "skill_id": "SKILL-REQ-QUALITY",
    }
    registry.bind(SkillBinding(version="1.0.0", **common))
    registry.bind(SkillBinding(version="1.1.0", **common))
    registry.deprecate("SKILL-REQ-QUALITY", "1.1.0")

    resolved = registry.resolve("requirements_agent", "gate_2", "requirements")

    assert resolved is not None
    assert resolved.metadata.version == "1.0.0"
