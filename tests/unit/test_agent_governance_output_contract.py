"""Contract tests for governance_output emitted by core agents."""

from __future__ import annotations

from types import SimpleNamespace

from src.agents.architecture_agent import ArchitectureAgent
from src.agents.program_manager import ProgramManagerAgent
from src.agents.requirements_agent import RequirementsAgent
from src.state.schema import AgentState, Phase, WorkItem, WorkItemStatus


REQUIRED_KEYS = {
    "policy_compliance",
    "traceability_links",
    "gate_readiness",
    "evidence_links",
    "risks_or_blockers",
}


def _assert_governance_contract(updates: dict, expected_gate: str) -> None:
    assert "governance_output" in updates

    payload = updates["governance_output"]
    assert REQUIRED_KEYS.issubset(payload.keys())
    assert payload["gate_readiness"]["gate"] == expected_gate
    assert payload["gate_readiness"]["status"] == "READY"

    assert updates["policy_compliance"] == payload["policy_compliance"]
    assert updates["traceability_links"] == payload["traceability_links"]
    assert updates["gate_readiness"] == payload["gate_readiness"]
    assert updates["evidence_links"] == payload["evidence_links"]
    assert updates["risks_or_blockers"] == payload["risks_or_blockers"]


def test_program_manager_emits_gate1_governance_output() -> None:
    agent = ProgramManagerAgent()
    state = AgentState(objective="Build governed SDLC workflow", phase=Phase.INTAKE)

    updates = agent.process(state)

    _assert_governance_contract(updates, "gate_1")


def test_requirements_agent_emits_gate2_governance_output() -> None:
    agent = RequirementsAgent()

    # Avoid external model calls and keep processing deterministic.
    agent.model = SimpleNamespace(invoke=lambda _: SimpleNamespace(content="[]"))

    state = AgentState(
        objective="Build governed SDLC workflow",
        phase=Phase.REQUIREMENTS,
        work_queue=[
            WorkItem(
                id="req-001",
                title="Requirements",
                description="Develop requirements",
                assigned_to="requirements_agent",
                status=WorkItemStatus.IN_PROGRESS,
            )
        ],
    )

    updates = agent.process(state)

    _assert_governance_contract(updates, "gate_2")


def test_architecture_agent_emits_gate3_governance_output() -> None:
    agent = ArchitectureAgent()

    state = AgentState(
        objective="Build governed SDLC workflow",
        phase=Phase.ARCHITECTURE,
        requirements={
            "REQ-001": {
                "id": "REQ-001",
                "text": "System shall support governance checks",
                "category": "functional",
                "priority": "high",
                "verification_method": "test",
            }
        },
    )

    updates = agent.process(state)

    _assert_governance_contract(updates, "gate_3")
