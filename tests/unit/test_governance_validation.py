"""Unit tests for governance evidence validation."""

from __future__ import annotations

from src.tools.governance_validation import validate_outputs


def _valid_gate2_output(agent: str = "requirements_agent") -> dict:
    return {
        "agent": agent,
        "policy_compliance": {
            "status": "PASS",
            "policies": ["RMP-001", "SEMP-001"],
        },
        "traceability_links": [
            {
                "requirement_id": "REQ-001",
                "artifacts": ["requirements_baseline_v1"],
            }
        ],
        "gate_readiness": {
            "gate": "gate_2",
            "status": "READY",
            "notes": "All required requirement artifacts present",
        },
        "evidence_links": {
            "requirements_baseline": "docs/artifacts/requirements-baseline-v1.md",
            "requirements_traceability_matrix": "docs/artifacts/rtm-v1.csv",
            "open_issues": "docs/artifacts/open-issues.md",
        },
        "risks_or_blockers": [],
    }


def test_gate_ready_when_required_fields_and_evidence_exist() -> None:
    report = validate_outputs([_valid_gate2_output()], expected_gate="gate_2")

    assert report["overall_valid"] is True
    assert report["gate_can_be_marked_ready"] is True
    assert report["results"][0]["missing_evidence_keys"] == []


def test_gate_not_ready_when_required_evidence_is_missing() -> None:
    broken = _valid_gate2_output()
    del broken["evidence_links"]["open_issues"]

    report = validate_outputs([broken], expected_gate="gate_2")

    assert report["overall_valid"] is False
    assert report["gate_can_be_marked_ready"] is False
    assert "open_issues" in report["results"][0]["missing_evidence_keys"]


def test_gate_not_ready_when_status_not_ready() -> None:
    not_ready = _valid_gate2_output()
    not_ready["gate_readiness"]["status"] = "NOT_READY"

    report = validate_outputs([not_ready], expected_gate="gate_2")

    assert report["overall_valid"] is True
    assert report["gate_can_be_marked_ready"] is False


def test_allow_conditional_flag_for_gate_readiness() -> None:
    conditional = _valid_gate2_output()
    conditional["gate_readiness"]["status"] = "READY_WITH_CONDITIONS"

    strict_report = validate_outputs([conditional], expected_gate="gate_2")
    relaxed_report = validate_outputs(
        [conditional],
        expected_gate="gate_2",
        require_strict_ready=False,
    )

    assert strict_report["gate_can_be_marked_ready"] is False
    assert relaxed_report["gate_can_be_marked_ready"] is True
