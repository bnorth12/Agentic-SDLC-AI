"""Base review board interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from src.state.schema import AgentState, BoardDecision
from src.utils.logging import log_board_activity


class BoardVote(str, Enum):
    """Board member vote options."""

    APPROVE = "approve"
    APPROVE_WITH_CONDITIONS = "approve_with_conditions"
    REJECT = "reject"
    DEFER = "defer"


class BoardMemberAssessment(BaseModel):
    """Assessment from a board member."""

    member_name: str
    assessment: str
    concerns: list[str] = Field(default_factory=list)
    questions: list[str] = Field(default_factory=list)
    vote: BoardVote
    rationale: str
    conditions: list[str] = Field(default_factory=list)


class BaseReviewBoard(ABC):
    """Base class for review boards."""

    def __init__(self, name: str, required_roles: list[str]):
        """
        Initialize a review board.

        Args:
            name: Board name (e.g., "Architecture Review Board")
            required_roles: List of agent roles that must participate
        """
        self.name = name
        self.required_roles = required_roles

    @abstractmethod
    def evaluate(self, state: AgentState, item_to_review: dict[str, Any]) -> BoardDecision:
        """
        Evaluate an item and produce a board decision.

        Args:
            state: Current shared state
            item_to_review: Item submitted for review

        Returns:
            BoardDecision with votes and recommendation
        """
        pass

    def tally_votes(self, assessments: list[BoardMemberAssessment]) -> BoardVote:
        """
        Tally votes and determine overall board decision.

        Args:
            assessments: List of member assessments

        Returns:
            Overall board vote
        """
        votes = [a.vote for a in assessments]

        # If any REJECT, board rejects
        if BoardVote.REJECT in votes:
            return BoardVote.REJECT

        # If any DEFER, board defers
        if BoardVote.DEFER in votes:
            return BoardVote.DEFER

        # If any conditions, approve with conditions
        has_conditions = any(a.conditions for a in assessments)
        if has_conditions:
            return BoardVote.APPROVE_WITH_CONDITIONS

        # Otherwise approve
        return BoardVote.APPROVE

    def compile_decision(
        self, assessments: list[BoardMemberAssessment], overall_vote: BoardVote
    ) -> BoardDecision:
        """
        Compile individual assessments into a board decision.

        Args:
            assessments: List of member assessments
            overall_vote: Tallied board vote

        Returns:
            BoardDecision
        """
        votes_dict = {a.member_name: a.vote.value for a in assessments}

        # Collect all conditions
        all_conditions = []
        for a in assessments:
            all_conditions.extend(a.conditions)

        # Compile rationale
        rationale_parts = []
        for a in assessments:
            rationale_parts.append(f"{a.member_name}: {a.rationale}")

        rationale = "\n".join(rationale_parts)

        decision = BoardDecision(
            board_name=self.name,
            decision=overall_vote.value,
            votes=votes_dict,
            conditions=all_conditions,
            rationale=rationale,
        )

        log_board_activity(self.name, f"Decision: {overall_vote.value}")

        return decision
