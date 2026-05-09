"""Governance evidence validation utilities."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

VALID_POLICY_STATUS = {"PASS", "CONDITIONAL", "FAIL"}
VALID_GATE_STATUS = {"READY", "READY_WITH_CONDITIONS", "NOT_READY"}

BASE_REQUIRED_FIELDS = [
    "policy_compliance",
    "traceability_links",
    "gate_readiness",
    "evidence_links",
    "risks_or_blockers",
]

GATE_REQUIRED_EVIDENCE_KEYS: dict[str, list[str]] = {
    "gate_1": [
        "objective_statement",
        "initial_backlog",
        "initial_risk_register",
    ],
    "gate_2": [
        "requirements_baseline",
        "requirements_traceability_matrix",
        "open_issues",
    ],
    "gate_3": [
        "architecture_baseline_package",
        "requirement_architecture_trace_matrix",
        "architecture_board_decision",
    ],
    "gate_4": [
        "change_set_summary",
        "test_report",
        "lint_report",
        "configuration_baseline_update",
    ],
    "gate_5": [
        "verification_validation_report",
        "coverage_summary",
        "defect_disposition_log",
    ],
    "gate_6": [
        "security_assessment_report",
        "safety_assessment_report",
    ],
    "gate_7": [
        "post_release_metrics_summary",
        "incident_problem_report",
        "updated_risk_register_action_plan",
    ],
}


def normalize_gate(gate: str) -> str:
    """Normalize gate identifiers to gate_1..gate_7 format."""
    cleaned = gate.strip().lower().replace("-", "_").replace(" ", "_")
    if cleaned.startswith("gate") and cleaned != "gate":
        suffix = cleaned.replace("gate", "", 1).strip("_")
        if suffix.isdigit():
            cleaned = f"gate_{suffix}"
    if cleaned.startswith("g") and len(cleaned) > 1 and cleaned[1:].isdigit():
        cleaned = f"gate_{cleaned[1:]}"
    return cleaned


def _is_non_empty(value: Any) -> bool:
    """Return True when value should be considered present for governance checks."""
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() != ""
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) > 0
    return True


def _extract_output_envelope(item: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    """Extract agent name and payload from either flat or wrapped input."""
    payload = item.get("output") if isinstance(item.get("output"), dict) else item
    agent_name = (
        item.get("agent")
        or payload.get("agent")
        or payload.get("agent_name")
        or "unknown_agent"
    )
    return str(agent_name), payload


def validate_agent_output(
    item: dict[str, Any],
    expected_gate: str | None = None,
    require_strict_ready: bool = True,
) -> dict[str, Any]:
    """Validate one agent output payload for governance readiness checks."""
    agent_name, payload = _extract_output_envelope(item)

    missing_fields = [field for field in BASE_REQUIRED_FIELDS if field not in payload]
    invalid_values: list[str] = []
    warnings: list[str] = []

    gate_from_payload = None
    gate_readiness = payload.get("gate_readiness")
    if isinstance(gate_readiness, Mapping):
        gate_from_payload = gate_readiness.get("gate")

    chosen_gate = expected_gate or gate_from_payload
    if not chosen_gate:
        warnings.append("No gate provided in input or gate_readiness.gate")
        chosen_gate = "unknown"
    else:
        chosen_gate = normalize_gate(str(chosen_gate))

    policy_compliance = payload.get("policy_compliance")
    if isinstance(policy_compliance, Mapping):
        status = str(policy_compliance.get("status", "")).upper()
        if status not in VALID_POLICY_STATUS:
            invalid_values.append(
                "policy_compliance.status must be PASS|CONDITIONAL|FAIL"
            )
    else:
        invalid_values.append("policy_compliance must be an object with status")

    gate_status = None
    if isinstance(gate_readiness, Mapping):
        gate_status = str(gate_readiness.get("status", "")).upper()
        if gate_status not in VALID_GATE_STATUS:
            invalid_values.append(
                "gate_readiness.status must be READY|READY_WITH_CONDITIONS|NOT_READY"
            )
    else:
        invalid_values.append("gate_readiness must be an object with status")

    traceability_links = payload.get("traceability_links")
    if not isinstance(traceability_links, list) or not traceability_links:
        invalid_values.append("traceability_links must be a non-empty list")

    risks_or_blockers = payload.get("risks_or_blockers")
    if not isinstance(risks_or_blockers, list):
        invalid_values.append("risks_or_blockers must be a list")

    evidence_links = payload.get("evidence_links")
    missing_evidence_keys: list[str] = []
    if not isinstance(evidence_links, Mapping):
        invalid_values.append("evidence_links must be an object")
    else:
        required_keys = GATE_REQUIRED_EVIDENCE_KEYS.get(chosen_gate, [])
        for key in required_keys:
            if key not in evidence_links or not _is_non_empty(evidence_links.get(key)):
                missing_evidence_keys.append(key)

    is_ready_status = gate_status == "READY"
    if not require_strict_ready and gate_status == "READY_WITH_CONDITIONS":
        is_ready_status = True

    valid = not missing_fields and not invalid_values and not missing_evidence_keys
    gate_ready = valid and is_ready_status

    return {
        "agent": agent_name,
        "gate": chosen_gate,
        "valid": valid,
        "gate_ready": gate_ready,
        "missing_fields": missing_fields,
        "invalid_values": invalid_values,
        "missing_evidence_keys": missing_evidence_keys,
        "warnings": warnings,
    }


def validate_outputs(
    outputs: list[dict[str, Any]],
    expected_gate: str | None = None,
    require_strict_ready: bool = True,
) -> dict[str, Any]:
    """Validate multiple agent outputs and provide aggregate readiness decision."""
    normalized_gate = normalize_gate(expected_gate) if expected_gate else None
    results = [
        validate_agent_output(
            item,
            expected_gate=normalized_gate,
            require_strict_ready=require_strict_ready,
        )
        for item in outputs
    ]

    overall_valid = all(result["valid"] for result in results)
    gate_can_be_marked_ready = overall_valid and all(
        result["gate_ready"] for result in results
    )

    return {
        "expected_gate": normalized_gate,
        "output_count": len(outputs),
        "overall_valid": overall_valid,
        "gate_can_be_marked_ready": gate_can_be_marked_ready,
        "results": results,
    }
