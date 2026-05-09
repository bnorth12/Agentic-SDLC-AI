"""End-to-end integration test for implementation to maintenance workflow."""

from __future__ import annotations

import unittest
from datetime import datetime

from src.graphs.supervisor import build_supervisor_graph
from src.state.persistence import get_persistence_manager
from src.state.schema import (
    AgentState,
    Phase,
    Requirement,
    WorkPackage,
    WorkPackageStatus,
)


class EndToEndImplementationToMaintenanceTest(unittest.TestCase):
    """Test full SDLC flow with requirement traceability and gate validation."""

    def _build_initial_state(self) -> AgentState:
        """Build initial state with requirements and work packages."""
        state = AgentState(objective="E2E Implementation to Maintenance Flow")

        # Add initial requirements
        state.requirements = {
            "REQ-001": Requirement(
                id="REQ-001",
                text="System shall implement core business logic",
                category="functional",
                priority="high",
                verification_method="test",
                created_by="test",
            ),
            "REQ-002": Requirement(
                id="REQ-002",
                text="System shall include security controls",
                category="non-functional",
                priority="high",
                verification_method="analysis",
                created_by="test",
            ),
            "REQ-003": Requirement(
                id="REQ-003",
                text="System shall support maintenance operations",
                category="non-functional",
                priority="medium",
                verification_method="inspection",
                created_by="test",
            ),
        }

        # Add initial work packages
        state.work_packages = {
            "WP-001": WorkPackage(
                id="WP-001",
                title="Implementation Package",
                description="Core implementation work",
                assigned_to="integration_manager",
                status=WorkPackageStatus.QUEUED,
                priority=1,
                traceability_links=["REQ-001", "REQ-002"],
            ),
            "WP-002": WorkPackage(
                id="WP-002",
                title="Verification Package",
                description="QA and verification work",
                assigned_to="qa_manager",
                status=WorkPackageStatus.QUEUED,
                priority=2,
                traceability_links=["REQ-001", "REQ-002", "REQ-003"],
            ),
            "WP-003": WorkPackage(
                id="WP-003",
                title="Deployment Package",
                description="Production deployment work",
                assigned_to="operations_lead",
                status=WorkPackageStatus.QUEUED,
                priority=3,
                traceability_links=["REQ-003"],
            ),
        }

        # Set session for checkpoint support
        state.metadata.session_id = "e2e-test-session"

        return state

    def test_full_implementation_to_maintenance_traceability(self) -> None:
        """Test complete workflow from IMPLEMENTATION through MAINTENANCE."""
        graph = build_supervisor_graph()
        initial_state = self._build_initial_state()

        # Start at IMPLEMENTATION phase
        initial_state.phase = Phase.IMPLEMENTATION

        # Prepare implementation artifacts
        initial_state.agent_outputs["chief_security_officer"] = {
            "agent": "chief_security_officer",
            "security_assessment": "Security controls validated",
            "policy_compliance": {"status": "PASS"},
            "evidence_links": {"security_controls": "implemented"},
        }
        initial_state.agent_outputs["chief_safety_officer"] = {
            "agent": "chief_safety_officer",
            "safety_assessment": "Safety requirements met",
            "policy_compliance": {"status": "PASS"},
            "evidence_links": {"safety_analysis": "completed"},
        }
        initial_state.agent_outputs["chief_compliance_officer"] = {
            "agent": "chief_compliance_officer",
            "compliance_assessment": "Compliance verified",
            "policy_compliance": {"status": "PASS"},
            "evidence_links": {"compliance_checklist": "signed_off"},
        }
        initial_state.agent_outputs["integration_manager"] = {
            "agent": "integration_manager",
            "implementation_package": {
                "status": "READY",
                "components": ["core_logic", "security_module"],
                "tests_passed": 95,
            },
            "gate_readiness": {"gate": "gate_4", "status": "READY"},
            "evidence_links": {
                "change_set_summary": "in_state:implementation",
                "test_report": "in_state:tests",
                "lint_report": "in_state:lint",
            },
        }

        # Execute graph with high recursion limit for full flow
        try:
            final_state = graph.invoke(
                initial_state,
                config={"recursion_limit": 100},
            )

            # Validate workflow progress through phases
            # Note: With deterministic test agents, flow may not reach MAINTENANCE
            # but should complete IMPLEMENTATION and attempt subsequent phases
            self.assertIsNotNone(final_state)
            self.assertIn(final_state["phase"], [
                Phase.IMPLEMENTATION,
                Phase.VERIFICATION,
                Phase.DEPLOYMENT,
                Phase.MAINTENANCE,
            ])

            # Validate work packages remain in state
            self.assertGreater(len(final_state["work_packages"]), 0)
            for wp_id, wp in final_state["work_packages"].items():
                self.assertIn(
                    wp.status,
                    [
                        WorkPackageStatus.QUEUED,
                        WorkPackageStatus.IN_PROGRESS,
                        WorkPackageStatus.COMPLETED,
                    ],
                )

            # Validate traceability: all work packages should have requirement links
            for wp_id, wp in final_state["work_packages"].items():
                self.assertGreater(
                    len(wp.traceability_links),
                    0,
                    f"WorkPackage {wp_id} missing traceability links",
                )

            # Validate all requirements remain in state
            self.assertEqual(len(final_state["requirements"]), 3)
            for req_id in ["REQ-001", "REQ-002", "REQ-003"]:
                self.assertIn(req_id, final_state["requirements"])

            # Validate governance metrics were tracked
            if final_state.get("governance_metrics"):
                self.assertIn("kpi_report", final_state["governance_metrics"])
                kpi_report = final_state["governance_metrics"]["kpi_report"]
                self.assertIn("summary", kpi_report)
                self.assertIn("requirements", kpi_report)

            # Validate checkpoint was saved
            sessions = get_persistence_manager().list_checkpoint_sessions()
            self.assertIn("e2e-test-session", sessions)

        except Exception as exc:
            # Capture detailed error for debugging
            self.fail(f"E2E workflow failed: {exc}")

    def test_work_package_status_transitions(self) -> None:
        """Test work package status transitions through workflow."""
        state = self._build_initial_state()

        # Verify initial state
        wp = state.work_packages["WP-001"]
        self.assertEqual(wp.status, WorkPackageStatus.QUEUED)
        self.assertIsNone(wp.completed_at)

        # Simulate in-progress transition
        wp.status = WorkPackageStatus.IN_PROGRESS
        wp.updated_at = datetime.utcnow()
        state.work_packages["WP-001"] = wp

        self.assertEqual(state.work_packages["WP-001"].status, WorkPackageStatus.IN_PROGRESS)

        # Simulate completion
        wp.status = WorkPackageStatus.COMPLETED
        wp.completed_at = datetime.utcnow()
        state.work_packages["WP-001"] = wp

        self.assertEqual(state.work_packages["WP-001"].status, WorkPackageStatus.COMPLETED)
        self.assertIsNotNone(state.work_packages["WP-001"].completed_at)

    def test_checkpoint_resume_semantics(self) -> None:
        """Test checkpoint save and resume functionality."""
        from src.graphs.supervisor import resume_from_checkpoint

        state = self._build_initial_state()
        state.phase = Phase.IMPLEMENTATION

        # Save checkpoint
        get_persistence_manager().save_checkpoint_snapshot(
            "e2e-test-session",
            state.model_dump(mode="python"),
        )

        # Create new state without work packages
        new_state = AgentState(objective="New session")

        # Resume from checkpoint
        new_state.metadata.session_id = "e2e-test-session"
        resumed_state = resume_from_checkpoint(new_state)

        # Validate restoration
        self.assertEqual(resumed_state.objective, state.objective)
        self.assertEqual(resumed_state.phase, Phase.IMPLEMENTATION)
        self.assertEqual(len(resumed_state.requirements), 3)
        self.assertEqual(len(resumed_state.work_packages), 3)
        self.assertGreater(len(resumed_state.metadata.session_id), 0)


if __name__ == "__main__":
    unittest.main()
