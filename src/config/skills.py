"""Skills binding configuration for supervisor execution."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SkillBindingPolicy:
    """Policy describing when and how a skill is bound to an agent execution."""

    agent_role: str
    gate: str
    discipline: str
    skill_id: str
    version: str
    required: bool = True


DEFAULT_SKILL_CONTRACTS: list[dict[str, Any]] = [
    {
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
        "confidence_score": 0.85,
        "escalation_conditions": ["invalid_requirement_format"],
        "output_schema": {
            "status": "str",
            "violations": "list[str]",
        },
    },
    {
        "metadata": {
            "skill_id": "SKILL-TRACEABILITY",
            "name": "Traceability Synthesis Skill",
            "discipline": "traceability",
            "version": "1.0.0",
            "owner_roles": ["requirements_agent", "verification_validation_agent"],
        },
        "inputs_required": ["requirements", "architecture"],
        "artifacts_produced": ["traceability_bundle"],
        "policy_checks": ["GOV-0002"],
        "traceability_links": ["AGT-0113"],
        "confidence_score": 0.8,
        "escalation_conditions": ["missing_trace_link"],
        "output_schema": {
            "status": "str",
            "missing_links": "list[str]",
        },
    },
]


DEFAULT_SKILL_BINDINGS: list[SkillBindingPolicy] = [
    SkillBindingPolicy(
        agent_role="requirements_agent",
        gate="gate_2",
        discipline="requirements",
        skill_id="SKILL-REQ-QUALITY",
        version="1.0.0",
        required=True,
    ),
    SkillBindingPolicy(
        agent_role="requirements_agent",
        gate="gate_2",
        discipline="traceability",
        skill_id="SKILL-TRACEABILITY",
        version="1.0.0",
        required=False,
    ),
]


def get_skill_binding_policies(agent_role: str, gate: str) -> list[SkillBindingPolicy]:
    """Return configured skill bindings for a specific role and gate."""
    return [
        policy
        for policy in DEFAULT_SKILL_BINDINGS
        if policy.agent_role == agent_role and policy.gate == gate
    ]
