"""Architecture Review Board implementation."""

from __future__ import annotations

from typing import Any

from src.boards.base_board import (
    BaseReviewBoard,
    BoardMemberAssessment,
    BoardVote,
)
from src.state.schema import AgentState, BoardDecision
from src.utils.logging import log_board_activity


class ArchitectureReviewBoard(BaseReviewBoard):
    """
    Architecture Review Board (ARB) that reviews:
    - System architecture proposals
    - Major design decisions
    - Interface definitions
    - Technology selections
    """

    def __init__(self):
        super().__init__(
            name="Architecture Review Board",
            required_roles=[
                "chief_engineer",
                "architecture_agent",
                "requirements_agent",
                "safety_agent",
            ],
        )

    def evaluate(
        self, state: AgentState, item_to_review: dict[str, Any]
    ) -> BoardDecision:
        """
        Evaluate architecture proposal.

        Args:
            state: Current shared state
            item_to_review: Architecture to review

        Returns:
            BoardDecision
        """
        log_board_activity(self.name, "Convened for architecture review")

        # Simulate board member assessments
        # In production, each agent would provide real assessment
        assessments = self._gather_assessments(state, item_to_review)

        # Tally votes
        overall_vote = self.tally_votes(assessments)

        # Compile decision
        decision = self.compile_decision(assessments, overall_vote)

        return decision

    def _gather_assessments(
        self, state: AgentState, item: dict[str, Any]
    ) -> list[BoardMemberAssessment]:
        """Gather assessments from board members (simplified)."""

        assessments = []

        # Chief Engineer assessment
        assessments.append(
            BoardMemberAssessment(
                member_name="chief_engineer",
                assessment="Architecture is technically sound and follows best practices",
                concerns=[],
                questions=[],
                vote=BoardVote.APPROVE,
                rationale="Meets all technical requirements and design principles",
            )
        )

        # Architecture agent assessment
        assessments.append(
            BoardMemberAssessment(
                member_name="architecture_agent",
                assessment="Architecture satisfies all functional requirements",
                concerns=[],
                questions=[],
                vote=BoardVote.APPROVE,
                rationale="All components are properly defined with clear interfaces",
            )
        )

        # Requirements agent assessment
        req_count = len(state.requirements)
        traced_reqs = len(item.get("traced_requirements", []))

        if traced_reqs < req_count:
            assessments.append(
                BoardMemberAssessment(
                    member_name="requirements_agent",
                    assessment=f"Not all requirements are traced to architecture ({traced_reqs}/{req_count})",
                    concerns=["Incomplete requirements traceability"],
                    questions=["Which requirements are not addressed?"],
                    vote=BoardVote.APPROVE_WITH_CONDITIONS,
                    rationale="Traceability must be complete before final approval",
                    conditions=["Complete requirements traceability matrix"],
                )
            )
        else:
            assessments.append(
                BoardMemberAssessment(
                    member_name="requirements_agent",
                    assessment="All requirements are properly traced",
                    concerns=[],
                    questions=[],
                    vote=BoardVote.APPROVE,
                    rationale="Complete traceability established",
                )
            )

        return assessments
