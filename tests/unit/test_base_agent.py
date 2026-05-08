"""Unit tests for base agent functionality."""

import pytest

from src.agents.base_agent import BaseAgent
from src.state.schema import AgentState


class TestAgent(BaseAgent):
    """Concrete implementation of BaseAgent for testing."""

    def get_system_prompt(self, state: AgentState) -> str:
        return f"Test agent for: {state.objective}"

    def process(self, state: AgentState) -> dict:
        return {"messages": [f"[{self.name}] Processed"]}


def test_base_agent_initialization():
    """Test that BaseAgent initializes correctly."""
    agent = TestAgent(
        name="test_agent",
        role="Test Role",
        authority_level="MEDIUM",
    )

    assert agent.name == "test_agent"
    assert agent.role == "Test Role"
    assert agent.authority_level == "MEDIUM"
    assert agent.model is not None


def test_agent_escalation_on_safety_issue():
    """Test that agent escalates safety issues."""
    agent = TestAgent("test", "Test", "MEDIUM")
    state = AgentState(objective="Test")

    assert agent.should_escalate("Critical safety issue detected", state)
    assert agent.should_escalate("Unsafe condition found", state)


def test_agent_no_escalation_on_routine():
    """Test that agent does not escalate routine matters."""
    agent = TestAgent("test", "Test", "MEDIUM")
    state = AgentState(objective="Test")

    assert not agent.should_escalate("Updated documentation", state)
    assert not agent.should_escalate("Routine maintenance completed", state)


def test_agent_request_review_board():
    """Test that agent can request review board."""
    agent = TestAgent("test", "Test", "MEDIUM")

    updates = agent.request_review_board(
        board_name="test_board",
        item="Test item",
        rationale="Needs review",
    )

    assert updates["active_board"] == "test_board"
    assert updates["requires_human_approval"] is True
    assert len(updates["messages"]) == 1


def test_agent_call_method():
    """Test that agent can be called with state."""
    agent = TestAgent("test", "Test", "MEDIUM")
    state = AgentState(objective="Test objective")

    updates = agent(state)

    assert "messages" in updates
    assert len(updates["messages"]) == 1
    assert "[test]" in updates["messages"][0]
