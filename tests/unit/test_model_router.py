"""Unit tests for adaptive model router behavior."""

from __future__ import annotations

import unittest

from src.config.settings import Settings
from src.routing import ModelRouter
from src.state.schema import AgentState, Phase, Requirement, Risk


class ModelRouterUnitTest(unittest.TestCase):
    def test_uses_role_policy_for_known_agent_alias(self) -> None:
        settings = Settings(
            ollama_model="default-model",
            model_requirements="requirements-model",
        )
        router = ModelRouter(settings)

        decision = router.choose_model(
            "requirements_agent",
            AgentState(objective="Draft requirements", phase=Phase.REQUIREMENTS),
        )

        self.assertEqual(decision.selected_model, "requirements-model")
        self.assertEqual(decision.reason, "policy_default")

    def test_prefers_complexity_tier_when_role_specific_missing(self) -> None:
        settings = Settings(
            ollama_model="default-model",
            model_low_complexity="small-model",
        )
        router = ModelRouter(settings)

        decision = router.choose_model(
            "qa_manager",
            AgentState(objective="quick verification", phase=Phase.INTAKE),
        )

        self.assertEqual(decision.complexity, "low")
        self.assertEqual(decision.selected_model, "small-model")

    def test_adaptive_fallback_on_error_threshold(self) -> None:
        settings = Settings(
            ollama_model="default-model",
            model_program_manager="primary-model",
            model_low_complexity="fallback-model",
            adaptive_error_threshold=2,
        )
        router = ModelRouter(settings)
        runtime_metrics = {
            "primary-model": {"calls": 3, "errors": 2, "avg_duration": 3.2},
            "fallback-model": {"calls": 4, "errors": 0, "avg_duration": 1.1},
        }

        decision = router.choose_model(
            "program_manager",
            AgentState(objective="intake summary", phase=Phase.INTAKE),
            runtime_metrics=runtime_metrics,
        )

        self.assertEqual(decision.selected_model, "fallback-model")
        self.assertTrue(decision.fallback_used)
        self.assertEqual(decision.reason, "adaptive_error_fallback")

    def test_complexity_estimation_handles_heavy_state(self) -> None:
        state = AgentState(objective="complex work", phase=Phase.IMPLEMENTATION)
        state.requires_human_approval = True

        for idx in range(1, 11):
            req_id = f"REQ-{idx:03d}"
            state.requirements[req_id] = Requirement(
                id=req_id,
                text="System shall maintain traceable implementation evidence",
                category="functional",
                priority="high",
                verification_method="test",
                created_by="test",
            )

        for idx in range(1, 7):
            risk_id = f"RISK-{idx:03d}"
            state.risks[risk_id] = Risk(
                id=risk_id,
                title="Performance risk",
                description="Potential execution slowdown",
                category="technical",
                probability="medium",
                impact="high",
            )

        router = ModelRouter(Settings())
        self.assertEqual(router.estimate_complexity(state), "high")


if __name__ == "__main__":
    unittest.main()