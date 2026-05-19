"""Integration tests for agent-skill binding behavior in supervisor execution."""

from __future__ import annotations

from src.config.skills import SkillBindingPolicy
from src.graphs.supervisor import apply_skill_binding_hook
from src.skills import SkillBinding, SkillRegistry, validate_skill_contract
from src.state.schema import AgentState


def _contract(skill_id: str, discipline: str, version: str) -> dict:
    return {
        "metadata": {
            "skill_id": skill_id,
            "name": skill_id,
            "discipline": discipline,
            "version": version,
            "owner_roles": ["requirements_agent"],
        },
        "inputs_required": ["requirements"],
        "artifacts_produced": [f"{skill_id.lower()}_artifact"],
        "policy_checks": ["RMP-001"],
        "traceability_links": ["AGT-0101"],
        "confidence_score": 0.8,
        "escalation_conditions": ["missing_artifact"],
        "output_schema": {
            "status": "str",
        },
    }


def test_apply_skill_binding_hook_executes_mandatory_before_optional() -> None:
    state = AgentState(objective="Binding order test")
    updates = {
        "phase": state.phase,
        "gate_readiness": {"gate": "gate_2", "status": "READY"},
        "messages": [],
    }

    registry = SkillRegistry()
    mandatory = validate_skill_contract(_contract("SKILL-MANDATORY", "requirements", "1.0.0"))
    optional = validate_skill_contract(_contract("SKILL-OPTIONAL", "traceability", "1.0.0"))
    registry.register(mandatory)
    registry.register(optional)

    registry.bind(
        SkillBinding(
            agent_role="requirements_agent",
            gate="gate_2",
            discipline="requirements",
            skill_id="SKILL-MANDATORY",
            version="1.0.0",
        )
    )
    registry.bind(
        SkillBinding(
            agent_role="requirements_agent",
            gate="gate_2",
            discipline="traceability",
            skill_id="SKILL-OPTIONAL",
            version="1.0.0",
        )
    )

    execution_order: list[str] = []

    def mandatory_exec(_state: AgentState, _updates: dict, _policy: SkillBindingPolicy) -> dict:
        execution_order.append("SKILL-MANDATORY")
        return {"status": "executed"}

    def optional_exec(_state: AgentState, _updates: dict, _policy: SkillBindingPolicy) -> dict:
        execution_order.append("SKILL-OPTIONAL")
        return {"status": "executed"}

    policies = [
        SkillBindingPolicy(
            agent_role="requirements_agent",
            gate="gate_2",
            discipline="requirements",
            skill_id="SKILL-MANDATORY",
            version="1.0.0",
            required=True,
        ),
        SkillBindingPolicy(
            agent_role="requirements_agent",
            gate="gate_2",
            discipline="traceability",
            skill_id="SKILL-OPTIONAL",
            version="1.0.0",
            required=False,
        ),
    ]

    result = apply_skill_binding_hook(
        state,
        updates,
        "requirements_agent",
        registry=registry,
        executors={
            "SKILL-MANDATORY": mandatory_exec,
            "SKILL-OPTIONAL": optional_exec,
        },
        policies=policies,
    )

    assert execution_order == ["SKILL-MANDATORY", "SKILL-OPTIONAL"]
    assert result["skill_execution"][0]["required"] is True
    assert result["skill_execution"][1]["required"] is False
    assert "skill_execution_log" in result["evidence_links"]


def test_apply_skill_binding_hook_preserves_phase_and_approval_flags() -> None:
    state = AgentState(objective="Authority preservation test")
    updates = {
        "phase": state.phase,
        "requires_human_approval": False,
        "gate_readiness": {"gate": "gate_2", "status": "READY"},
    }

    result = apply_skill_binding_hook(state, updates, "requirements_agent", policies=[])

    assert result["phase"] == state.phase
    assert result["requires_human_approval"] is False
