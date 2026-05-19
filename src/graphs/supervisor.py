"""Supervisor graph orchestrating the multi-agent system."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import Any

from langgraph.graph import StateGraph

from src.agents import (
    ArchitectureAgent,
    ChiefComplianceOfficerAgent,
    ChiefEngineerAgent,
    ChiefReliabilityOfficerAgent,
    ChiefSafetyOfficerAgent,
    ChiefSecurityOfficerAgent,
    ConfigurationManagementAgent,
    CyberArchitectAgent,
    DataManagementAgentStub,
    IntegrationAndTestAgentStub,
    IntegrationManagerAgent,
    OperationsLeadAgent,
    ProgramManagerAgent,
    QAManagerAgent,
    RequirementsAgent,
    SoftwareDevelopmentAgent,
    SoftwareQualityManagerAgent,
    VerificationValidationAgent,
)
from src.boards import ArchitectureReviewBoard
from src.config.skills import (
    DEFAULT_SKILL_CONTRACTS,
    SkillBindingPolicy,
    get_skill_binding_policies,
)
from src.gates import (
    evaluate_architecture_gate,
    evaluate_deployment_gate,
    evaluate_implementation_gate,
    evaluate_requirements_gate,
)
from src.metrics import KPITracker
from src.state.persistence import get_persistence_manager
from src.state.schema import AgentState, Phase
from src.skills import (
    SkillBinding,
    SkillRegistry,
    run_requirements_quality_skill,
    run_traceability_synthesis_skill,
    validate_skill_contract,
)
from src.tools.governance_validation import validate_outputs
from src.utils.logging import get_logger

logger = get_logger(__name__)


# Global KPI tracker instance
_kpi_tracker: KPITracker | None = None
_skill_registry: SkillRegistry | None = None


SkillExecutor = Callable[[AgentState, dict[str, Any], SkillBindingPolicy], dict[str, Any]]


def get_kpi_tracker() -> KPITracker:
    """Get the global KPI tracker instance."""
    global _kpi_tracker
    if _kpi_tracker is None:
        _kpi_tracker = KPITracker()
    return _kpi_tracker


def get_skill_registry() -> SkillRegistry:
    """Get the global skill registry seeded with default contracts and bindings."""
    global _skill_registry
    if _skill_registry is not None:
        return _skill_registry

    registry = SkillRegistry()
    for payload in DEFAULT_SKILL_CONTRACTS:
        contract = validate_skill_contract(payload)
        registry.register(contract)

    for policy in get_skill_binding_policies("requirements_agent", "gate_2"):
        registry.bind(
            SkillBinding(
                agent_role=policy.agent_role,
                gate=policy.gate,
                discipline=policy.discipline,
                skill_id=policy.skill_id,
                version=policy.version,
            )
        )

    _skill_registry = registry
    return _skill_registry


def _default_skill_executors() -> dict[str, SkillExecutor]:
    """Default skill executors mapped to concrete skill implementations."""
    return {
        "SKILL-REQ-QUALITY": run_requirements_quality_skill,
        "SKILL-TRACEABILITY": run_traceability_synthesis_skill,
    }


def apply_skill_binding_hook(
    state: AgentState,
    updates: dict[str, Any],
    source_agent: str,
    registry: SkillRegistry | None = None,
    executors: dict[str, SkillExecutor] | None = None,
    policies: list[SkillBindingPolicy] | None = None,
) -> dict[str, Any]:
    """Apply bound skills before governance gate evaluation and capture execution order."""
    if not updates:
        return updates

    candidate = dict(updates)
    gate_readiness = candidate.get("gate_readiness")
    if not isinstance(gate_readiness, dict):
        return candidate

    gate = gate_readiness.get("gate")
    if not gate:
        return candidate

    active_policies = (
        list(policies)
        if policies is not None
        else get_skill_binding_policies(source_agent, str(gate))
    )
    if not active_policies:
        return candidate

    ordered_policies = sorted(active_policies, key=lambda policy: (not policy.required))
    active_registry = registry or get_skill_registry()
    active_executors = executors or _default_skill_executors()

    execution_log: list[dict[str, Any]] = []
    skill_outputs = dict(candidate.get("skill_outputs", {}))

    for index, policy in enumerate(ordered_policies, start=1):
        contract = active_registry.resolve(
            policy.agent_role,
            policy.gate,
            policy.discipline,
        )

        if contract is None:
            execution_log.append(
                {
                    "order": index,
                    "skill_id": policy.skill_id,
                    "required": policy.required,
                    "status": "missing_binding",
                }
            )
            continue

        executor = active_executors.get(contract.metadata.skill_id)
        if executor is None:
            execution_log.append(
                {
                    "order": index,
                    "skill_id": contract.metadata.skill_id,
                    "required": policy.required,
                    "status": "skipped_no_executor",
                }
            )
            continue

        result = executor(state, candidate, policy)
        skill_outputs[contract.metadata.skill_id] = result
        execution_log.append(
            {
                "order": index,
                "skill_id": contract.metadata.skill_id,
                "required": policy.required,
                "status": "executed",
            }
        )

    candidate["skill_outputs"] = skill_outputs
    candidate["skill_execution"] = execution_log

    governance_metrics = dict(state.governance_metrics)
    governance_metrics.update(dict(candidate.get("governance_metrics", {})))
    existing_log = governance_metrics.get("skill_execution_log", [])
    if not isinstance(existing_log, list):
        existing_log = []
    governance_metrics["skill_execution_log"] = [*existing_log, *execution_log]
    candidate["governance_metrics"] = governance_metrics

    evidence_links = dict(candidate.get("evidence_links", {}))
    evidence_links["skill_execution_log"] = (
        f"in_state:skill_execution:{source_agent}:{str(gate)}"
    )
    candidate["evidence_links"] = evidence_links

    messages = _ensure_messages(candidate)
    messages.append(
        f"[skill_hook] Executed {len(execution_log)} bound skill(s) for {source_agent}"
    )

    return candidate


def _save_checkpoint_snapshot(state: AgentState, updates: dict[str, Any]) -> None:
    """Persist a lightweight in-memory checkpoint snapshot for session resume."""
    session_id = state.metadata.session_id
    if not session_id:
        return

    try:
        payload = state.model_dump(mode="python")
        payload.update(updates)
        get_persistence_manager().save_checkpoint_snapshot(session_id, payload, label="auto")
    except Exception as exc:  # pragma: no cover - defensive logging only
        logger.warning("Unable to save checkpoint snapshot: %s", exc)


def _run_with_metrics(
    state: AgentState,
    source_name: str,
    producer: Callable[[], dict[str, Any]],
) -> dict[str, Any]:
    """Execute a node producer and record execution metrics and observability events."""
    start = time.perf_counter()
    initial_phase = state.phase
    manager = get_persistence_manager()

    try:
        produced_updates = producer()
        skill_augmented = apply_skill_binding_hook(state, produced_updates, source_name)
        updates = apply_governance_gate_hook(state, skill_augmented, source_name)
        elapsed = time.perf_counter() - start

        get_kpi_tracker().record_agent_execution(source_name, elapsed)
        manager.record_observability_event(
            "agent_execution",
            {
                "agent": source_name,
                "duration_seconds": round(elapsed, 4),
                "result_keys": sorted(list(updates.keys())),
            },
            session_id=state.metadata.session_id or None,
        )

        model_routing = updates.get("model_routing")
        if isinstance(model_routing, dict):
            get_kpi_tracker().record_model_routing(
                agent_name=source_name,
                model_name=str(model_routing.get("selected_model", "unknown")),
                complexity=str(model_routing.get("complexity", "unknown")),
                fallback_used=bool(model_routing.get("fallback_used", False)),
                duration_seconds=float(model_routing.get("duration_seconds", elapsed)),
                failed=bool(model_routing.get("failed", False)),
            )
            manager.record_observability_event(
                "model_routing",
                {
                    "agent": source_name,
                    **model_routing,
                },
                session_id=state.metadata.session_id or None,
            )

        next_phase = updates.get("phase", initial_phase)
        if next_phase != initial_phase:
            get_kpi_tracker().record_phase_transition(
                from_phase=str(initial_phase),
                to_phase=str(next_phase),
                duration_seconds=elapsed,
            )
            manager.record_observability_event(
                "phase_transition",
                {
                    "from_phase": str(initial_phase),
                    "to_phase": str(next_phase),
                    "duration_seconds": round(elapsed, 4),
                },
                session_id=state.metadata.session_id or None,
            )

        return updates
    except Exception as exc:
        get_kpi_tracker().record_error(source_name)
        manager.record_observability_event(
            "agent_error",
            {
                "agent": source_name,
                "error": str(exc),
            },
            session_id=state.metadata.session_id or None,
        )
        raise


def _ensure_messages(updates: dict[str, Any]) -> list[str]:
    """Ensure updates has a mutable messages list and return it."""
    messages = updates.get("messages")
    if not isinstance(messages, list):
        messages = []
        updates["messages"] = messages
    return messages


def _build_governance_output(
    updates: dict[str, Any], source_agent: str
) -> dict[str, Any]:
    """Build a governance output payload expected by the validator."""
    provided = updates.get("governance_output")
    if isinstance(provided, dict):
        payload = dict(provided)
        payload.setdefault("agent", source_agent)
        return payload

    return {
        "agent": source_agent,
        "policy_compliance": updates.get("policy_compliance"),
        "traceability_links": updates.get("traceability_links"),
        "gate_readiness": updates.get("gate_readiness"),
        "evidence_links": updates.get("evidence_links"),
        "risks_or_blockers": updates.get("risks_or_blockers", []),
    }


def apply_governance_gate_hook(
    state: AgentState,
    updates: dict[str, Any],
    source_agent: str,
) -> dict[str, Any]:
    """Validate gate readiness claims before allowing READY transitions."""
    if not updates:
        return updates

    candidate = dict(updates)
    gate_readiness = candidate.get("gate_readiness")
    if not isinstance(gate_readiness, dict):
        _save_checkpoint_snapshot(state, candidate)
        return candidate

    gate_status = str(gate_readiness.get("status", "")).upper()
    if gate_status != "READY":
        _save_checkpoint_snapshot(state, candidate)
        return candidate

    output = _build_governance_output(candidate, source_agent)
    stored_outputs = dict(state.agent_outputs)
    candidate_outputs = candidate.get("agent_outputs")
    if isinstance(candidate_outputs, dict):
        stored_outputs.update(candidate_outputs)
    stored_outputs[source_agent] = output
    candidate["agent_outputs"] = stored_outputs

    report = validate_outputs(
        [output],
        expected_gate=gate_readiness.get("gate"),
        require_strict_ready=True,
    )
    candidate["governance_validation"] = report

    # Record metrics for this gate evaluation
    gate_name = report["results"][0]["gate"] if report["results"] else "unknown"
    evidence_completeness = 1.0 - (
        len(report["results"][0]["missing_evidence_keys"])
        / max(1, len(report["results"][0].get("expected_evidence_keys", [])))
        if report["results"]
        else 0.0
    )
    get_kpi_tracker().record_gate_outcome(
        gate_name=gate_name,
        status="READY" if report["gate_can_be_marked_ready"] else "NOT_READY",
        evidence_completeness=evidence_completeness,
        was_ready_on_first_attempt=True,
    )
    get_kpi_tracker().record_checkpoint_snapshot()

    # Update governance metrics in state
    governance_metrics = dict(candidate.get("governance_metrics", {}))
    governance_metrics["last_gate_evaluation"] = {
        "gate": gate_name,
        "status": "READY" if report["gate_can_be_marked_ready"] else "NOT_READY",
        "evidence_completeness": evidence_completeness,
    }
    governance_metrics["kpi_report"] = get_kpi_tracker().get_metrics_report()
    candidate["governance_metrics"] = governance_metrics

    if report["gate_can_be_marked_ready"]:
        messages = _ensure_messages(candidate)
        messages.append(
            f"[governance_hook] {source_agent} passed validation for "
            f"{report['results'][0]['gate']}"
        )
        _save_checkpoint_snapshot(state, candidate)
        return candidate

    # Block READY transition and prevent associated phase transition.
    blocked_readiness = dict(gate_readiness)
    blocked_readiness["status"] = "NOT_READY"
    blocked_readiness["reason"] = "Governance evidence validation failed"
    candidate["gate_readiness"] = blocked_readiness
    candidate.pop("phase", None)
    candidate["requires_human_approval"] = True

    details = report["results"][0]
    issues: list[str] = []
    if details["missing_fields"]:
        issues.append("missing fields: " + ", ".join(details["missing_fields"]))
    if details["invalid_values"]:
        issues.append("invalid values: " + ", ".join(details["invalid_values"]))
    if details["missing_evidence_keys"]:
        issues.append(
            "missing evidence: " + ", ".join(details["missing_evidence_keys"])
        )

    messages = _ensure_messages(candidate)
    messages.append(
        "[governance_hook] READY transition blocked until governance evidence is complete"
    )
    if issues:
        messages.append("[governance_hook] " + " | ".join(issues))

    logger.warning(
        "Blocked READY transition for %s due to governance validation failure",
        source_agent,
    )
    _save_checkpoint_snapshot(state, candidate)
    return candidate


def should_continue(state: AgentState) -> str:
    """
    Determine the next node in the graph.

    Args:
        state: Current state

    Returns:
        Next node name
    """
    if state.active_board:
        return "review_board"

    if state.requires_human_approval:
        return "human_approval"

    # Route based on phase with gate checkpoints.
    if state.phase == Phase.INTAKE:
        return "program_manager"

    if state.phase == Phase.REQUIREMENTS:
        if not state.requirements:
            return "requirements_agent"
        return "requirements_gate"

    if state.phase == Phase.ARCHITECTURE:
        if not state.architecture:
            return "architecture_agent"
        if "architecture_security_assessment" not in state.agent_outputs:
            return "chief_security_officer"
        if "architecture_safety_assessment" not in state.agent_outputs:
            return "chief_safety_officer"
        if "architecture_reliability_assessment" not in state.agent_outputs:
            return "chief_reliability_officer"
        return "architecture_gate"

    if state.phase == Phase.DESIGN:
        return "cyber_architect"

    if state.phase == Phase.IMPLEMENTATION:
        assessments = state.agent_outputs
        if "security_assessment" not in assessments:
            return "chief_security_officer"
        if "safety_assessment" not in assessments:
            return "chief_safety_officer"
        if "reliability_assessment" not in assessments:
            return "chief_reliability_officer"
        if "compliance_assessment" not in assessments:
            return "chief_compliance_officer"
        if "software_development_package" not in assessments:
            return "software_development_agent"
        if "configuration_management_package" not in assessments:
            return "configuration_management_agent"
        if "implementation_package" not in assessments:
            return "integration_manager"
        return "implementation_gate"

    if state.phase == Phase.VERIFICATION:
        if "verification_validation_package" not in state.agent_outputs:
            return "verification_validation_agent"
        if "verification_package" not in state.agent_outputs:
            return "qa_manager"
        return "END"

    if state.phase == Phase.DEPLOYMENT:
        if "deployment_package" not in state.agent_outputs:
            return "operations_lead"
        return "deployment_gate"

    if state.phase == Phase.MAINTENANCE:
        if "maintenance_quality_package" not in state.agent_outputs:
            return "software_quality_manager"
        return "END"

    return "END"


def program_manager_node(state: AgentState) -> dict[str, Any]:
    """Execute program manager agent."""
    agent = ProgramManagerAgent()
    return _run_with_metrics(state, "program_manager", lambda: agent(state))


def chief_engineer_node(state: AgentState) -> dict[str, Any]:
    """Execute chief engineer agent."""
    agent = ChiefEngineerAgent()
    return _run_with_metrics(state, "chief_engineer", lambda: agent(state))


def requirements_node(state: AgentState) -> dict[str, Any]:
    """Execute requirements agent."""
    agent = RequirementsAgent()
    return _run_with_metrics(state, "requirements_agent", lambda: agent(state))


def architecture_node(state: AgentState) -> dict[str, Any]:
    """Execute architecture agent."""
    agent = ArchitectureAgent()
    return _run_with_metrics(state, "architecture_agent", lambda: agent(state))


def cyber_architect_node(state: AgentState) -> dict[str, Any]:
    """Execute cyber architect agent."""
    agent = CyberArchitectAgent()
    return _run_with_metrics(state, "cyber_architect", lambda: agent(state))


def chief_security_officer_node(state: AgentState) -> dict[str, Any]:
    """Execute chief security officer agent."""
    agent = ChiefSecurityOfficerAgent()
    return _run_with_metrics(state, "chief_security_officer", lambda: agent(state))


def chief_safety_officer_node(state: AgentState) -> dict[str, Any]:
    """Execute chief safety officer agent."""
    agent = ChiefSafetyOfficerAgent()
    return _run_with_metrics(state, "chief_safety_officer", lambda: agent(state))


def chief_reliability_officer_node(state: AgentState) -> dict[str, Any]:
    """Execute chief reliability officer agent."""
    agent = ChiefReliabilityOfficerAgent()
    return _run_with_metrics(state, "chief_reliability_officer", lambda: agent(state))


def chief_compliance_officer_node(state: AgentState) -> dict[str, Any]:
    """Execute chief compliance officer agent."""
    agent = ChiefComplianceOfficerAgent()
    return _run_with_metrics(state, "chief_compliance_officer", lambda: agent(state))


def software_development_agent_node(state: AgentState) -> dict[str, Any]:
    """Execute software development agent."""
    agent = SoftwareDevelopmentAgent()
    return _run_with_metrics(state, "software_development_agent", lambda: agent(state))


def configuration_management_agent_node(state: AgentState) -> dict[str, Any]:
    """Execute configuration management agent."""
    agent = ConfigurationManagementAgent()
    return _run_with_metrics(
        state,
        "configuration_management_agent",
        lambda: agent(state),
    )


def integration_manager_node(state: AgentState) -> dict[str, Any]:
    """Execute integration manager agent."""
    agent = IntegrationManagerAgent()
    return _run_with_metrics(state, "integration_manager", lambda: agent(state))


def qa_manager_node(state: AgentState) -> dict[str, Any]:
    """Execute QA manager agent."""
    agent = QAManagerAgent()
    return _run_with_metrics(state, "qa_manager", lambda: agent(state))


def verification_validation_agent_node(state: AgentState) -> dict[str, Any]:
    """Execute verification and validation agent."""
    agent = VerificationValidationAgent()
    return _run_with_metrics(
        state,
        "verification_validation_agent",
        lambda: agent(state),
    )


def operations_lead_node(state: AgentState) -> dict[str, Any]:
    """Execute operations lead agent."""
    agent = OperationsLeadAgent()
    return _run_with_metrics(state, "operations_lead", lambda: agent(state))


def software_quality_manager_node(state: AgentState) -> dict[str, Any]:
    """Execute software quality manager agent."""
    agent = SoftwareQualityManagerAgent()
    return _run_with_metrics(state, "software_quality_manager", lambda: agent(state))


def integration_and_test_agent_node(state: AgentState) -> dict[str, Any]:
    """Execute integration and test agent."""
    agent = IntegrationAndTestAgentStub()
    return _run_with_metrics(state, "integration_and_test_agent", lambda: agent(state))


def data_management_agent_node(state: AgentState) -> dict[str, Any]:
    """Execute data management agent."""
    agent = DataManagementAgentStub()
    return _run_with_metrics(state, "data_management_agent", lambda: agent(state))


def requirements_gate_node(state: AgentState) -> dict[str, Any]:
    """Execute requirements gate evaluation."""
    return _run_with_metrics(
        state,
        "requirements_gate",
        lambda: evaluate_requirements_gate(state),
    )


def architecture_gate_node(state: AgentState) -> dict[str, Any]:
    """Execute architecture gate evaluation."""
    return _run_with_metrics(
        state,
        "architecture_gate",
        lambda: evaluate_architecture_gate(state),
    )


def implementation_gate_node(state: AgentState) -> dict[str, Any]:
    """Execute implementation gate evaluation."""
    return _run_with_metrics(
        state,
        "implementation_gate",
        lambda: evaluate_implementation_gate(state),
    )


def deployment_gate_node(state: AgentState) -> dict[str, Any]:
    """Execute deployment gate evaluation."""
    return _run_with_metrics(
        state,
        "deployment_gate",
        lambda: evaluate_deployment_gate(state),
    )


def review_board_node(state: AgentState) -> dict[str, Any]:
    """Execute review board."""
    if not state.active_board:
        return {}

    logger.info(f"Convening {state.active_board}")

    # Instantiate the appropriate board
    if state.active_board == "architecture_review":
        board = ArchitectureReviewBoard()
        decision = board.evaluate(state, state.architecture)
    else:
        # Placeholder for other boards
        logger.warning(f"Board {state.active_board} not implemented yet")
        return {"active_board": None}

    # Store board decision
    board_results = state.board_results.copy()
    board_results[state.active_board] = decision

    updates = {
        "board_results": board_results,
        "active_board": None,
        "requires_human_approval": False,
        "messages": [
            f"[{state.active_board}] Decision: {decision.decision}",
            f"Rationale: {decision.rationale}",
        ],
    }

    if state.phase == Phase.ARCHITECTURE and isinstance(
        state.agent_outputs.get("architecture_agent"), dict
    ):
        outputs = dict(state.agent_outputs)
        architecture_payload = dict(outputs["architecture_agent"])
        evidence_links = dict(architecture_payload.get("evidence_links", {}))
        evidence_links["architecture_board_decision"] = (
            f"in_state:architecture_review:{decision.decision}"
        )
        architecture_payload["evidence_links"] = evidence_links
        outputs["architecture_agent"] = architecture_payload
        updates["agent_outputs"] = outputs

        if decision.decision in {"reject", "defer"}:
            updates["requires_human_approval"] = True
            updates["messages"].append(
                "[review_board] Architecture board did not approve; human review required"
            )

    return _run_with_metrics(state, "review_board", lambda: updates)


def human_approval_node(state: AgentState) -> dict[str, Any]:
    """
    Human approval gate (simplified - just auto-approves for now).

    In production, this would use HITL utilities to pause and wait for human input.
    """
    logger.info("Human approval checkpoint")

    # For now, auto-approve
    updates = {
        "requires_human_approval": False,
        "human_feedback": "Auto-approved for demo",
        "messages": ["[HUMAN] Approved"],
    }
    return _run_with_metrics(state, "human_approval", lambda: updates)


def resume_from_checkpoint(state: AgentState) -> AgentState:
    """
    Resume execution from a checkpoint snapshot.

    If the state has a session_id, attempt to load the last saved checkpoint
    and restore the state to that point. This enables resuming work after
    interruptions or for incremental progress tracking.

    Args:
        state: Current state (may be initial or partial)

    Returns:
        Restored state from checkpoint, or original state if no checkpoint found
    """
    session_id = state.metadata.session_id
    if not session_id:
        logger.debug("No session_id in state metadata; skipping checkpoint restore")
        return state

    resume_point = state.metadata.resume_point

    try:
        checkpoint = get_persistence_manager().load_checkpoint_snapshot(
            session_id,
            resume_point=resume_point,
        )
        if checkpoint:
            logger.info(f"Restoring state from checkpoint for session {session_id}")
            # Reconstruct AgentState from checkpoint payload
            restored = AgentState(**checkpoint)
            logger.info(
                f"Restored state: phase={restored.phase}, "
                f"requirements={len(restored.requirements)}, "
                f"work_packages={len(restored.work_packages)}"
            )
            return restored
        else:
            logger.debug(
                f"No checkpoint found for session {session_id}; using current state"
            )
    except Exception as exc:  # pragma: no cover - defensive logging
        logger.warning(f"Unable to restore checkpoint: {exc}; using current state")

    return state


def build_supervisor_graph() -> StateGraph:
    """
    Build the supervisor graph that orchestrates all agents.

    Returns:
        Compiled StateGraph
    """
    workflow = StateGraph(AgentState)

    # Agent and gate nodes
    workflow.add_node("program_manager", program_manager_node)
    workflow.add_node("chief_engineer", chief_engineer_node)
    workflow.add_node("requirements_agent", requirements_node)
    workflow.add_node("architecture_agent", architecture_node)
    workflow.add_node("cyber_architect", cyber_architect_node)
    workflow.add_node("chief_security_officer", chief_security_officer_node)
    workflow.add_node("chief_safety_officer", chief_safety_officer_node)
    workflow.add_node("chief_reliability_officer", chief_reliability_officer_node)
    workflow.add_node("chief_compliance_officer", chief_compliance_officer_node)
    workflow.add_node("software_development_agent", software_development_agent_node)
    workflow.add_node(
        "configuration_management_agent", configuration_management_agent_node
    )
    workflow.add_node("integration_manager", integration_manager_node)
    workflow.add_node(
        "verification_validation_agent", verification_validation_agent_node
    )
    workflow.add_node("qa_manager", qa_manager_node)
    workflow.add_node("operations_lead", operations_lead_node)
    workflow.add_node("software_quality_manager", software_quality_manager_node)
    workflow.add_node("integration_and_test_agent", integration_and_test_agent_node)
    workflow.add_node("data_management_agent", data_management_agent_node)
    workflow.add_node("requirements_gate", requirements_gate_node)
    workflow.add_node("architecture_gate", architecture_gate_node)
    workflow.add_node("implementation_gate", implementation_gate_node)
    workflow.add_node("deployment_gate", deployment_gate_node)
    workflow.add_node("review_board", review_board_node)
    workflow.add_node("human_approval", human_approval_node)

    workflow.set_entry_point("program_manager")

    route_map = {
        "program_manager": "program_manager",
        "chief_engineer": "chief_engineer",
        "requirements_agent": "requirements_agent",
        "architecture_agent": "architecture_agent",
        "cyber_architect": "cyber_architect",
        "chief_security_officer": "chief_security_officer",
        "chief_safety_officer": "chief_safety_officer",
        "chief_reliability_officer": "chief_reliability_officer",
        "chief_compliance_officer": "chief_compliance_officer",
        "software_development_agent": "software_development_agent",
        "configuration_management_agent": "configuration_management_agent",
        "integration_manager": "integration_manager",
        "verification_validation_agent": "verification_validation_agent",
        "qa_manager": "qa_manager",
        "operations_lead": "operations_lead",
        "software_quality_manager": "software_quality_manager",
        "integration_and_test_agent": "integration_and_test_agent",
        "data_management_agent": "data_management_agent",
        "requirements_gate": "requirements_gate",
        "architecture_gate": "architecture_gate",
        "implementation_gate": "implementation_gate",
        "deployment_gate": "deployment_gate",
        "review_board": "review_board",
        "human_approval": "human_approval",
        "END": "__end__",
    }

    for node_name in [
        "program_manager",
        "chief_engineer",
        "requirements_agent",
        "architecture_agent",
        "cyber_architect",
        "chief_security_officer",
        "chief_safety_officer",
        "chief_reliability_officer",
        "chief_compliance_officer",
        "software_development_agent",
        "configuration_management_agent",
        "integration_manager",
        "verification_validation_agent",
        "qa_manager",
        "operations_lead",
        "software_quality_manager",
        "integration_and_test_agent",
        "data_management_agent",
        "requirements_gate",
        "architecture_gate",
        "implementation_gate",
        "deployment_gate",
        "review_board",
        "human_approval",
    ]:
        workflow.add_conditional_edges(node_name, should_continue, route_map)

    graph = workflow.compile()
    logger.info("Supervisor graph compiled successfully")
    return graph
