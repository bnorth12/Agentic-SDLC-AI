"""Unit tests for skill contract schema validation."""

from __future__ import annotations

import pytest

from src.skills.contracts import parse_semver, validate_skill_contract


def _valid_payload() -> dict:
    return {
        "metadata": {
            "skill_id": "SKILL-REQ-QUALITY",
            "name": "Requirements Quality Skill",
            "discipline": "requirements",
            "version": "1.0.0",
            "owner_roles": ["requirements_agent", "chief_engineer"],
        },
        "inputs_required": ["requirements"],
        "artifacts_produced": ["requirements_quality_report"],
        "policy_checks": ["RMP-001"],
        "traceability_links": ["AGT-0110"],
        "confidence_score": 0.9,
        "escalation_conditions": ["missing_required_fields"],
        "output_schema": {
            "violations": "list[str]",
            "status": "str",
        },
    }


def test_validate_skill_contract_accepts_valid_payload() -> None:
    contract = validate_skill_contract(_valid_payload())

    assert contract.metadata.skill_id == "SKILL-REQ-QUALITY"
    assert contract.output_schema["status"] == "str"


def test_parse_semver_returns_numeric_tuple() -> None:
    assert parse_semver("2.3.4") == (2, 3, 4)


def test_validate_skill_contract_rejects_invalid_version() -> None:
    payload = _valid_payload()
    payload["metadata"]["version"] = "v1"

    with pytest.raises(ValueError, match="semantic version"):
        validate_skill_contract(payload)


def test_validate_skill_contract_rejects_missing_skill_id() -> None:
    payload = _valid_payload()
    payload["metadata"]["skill_id"] = ""

    with pytest.raises(ValueError, match="Invalid skill contract"):
        validate_skill_contract(payload)


def test_validate_skill_contract_rejects_empty_output_schema() -> None:
    payload = _valid_payload()
    payload["output_schema"] = {}

    with pytest.raises(ValueError, match="output_schema"):
        validate_skill_contract(payload)
