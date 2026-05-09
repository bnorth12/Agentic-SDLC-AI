"""Shared state schema for the Agentic SDLC orchestration graph."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Phase(str, Enum):
    """SDLC phases."""

    INTAKE = "intake"
    REQUIREMENTS = "requirements"
    ARCHITECTURE = "architecture"
    DESIGN = "design"
    IMPLEMENTATION = "implementation"
    VERIFICATION = "verification"
    DEPLOYMENT = "deployment"
    MAINTENANCE = "maintenance"


class WorkItemStatus(str, Enum):
    """Work item status."""

    BACKLOG = "backlog"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    BLOCKED = "blocked"
    COMPLETED = "completed"


class WorkPackageStatus(str, Enum):
    """Work package status in the orchestration queue."""

    QUEUED = "queued"
    IN_PROGRESS = "in_progress"
    AWAITING_GATE = "awaiting_gate"
    GATE_PASSED = "gate_passed"
    GATE_FAILED = "gate_failed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class DecisionStatus(str, Enum):
    """Decision approval status."""

    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    DEFERRED = "deferred"


class Requirement(BaseModel):
    """A system requirement."""

    id: str
    text: str
    category: str  # functional, non-functional, constraint
    priority: str  # critical, high, medium, low
    verification_method: str  # test, analysis, inspection, demonstration
    status: str = "draft"
    parent_id: str | None = None
    rationale: str = ""
    created_by: str = ""
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Decision(BaseModel):
    """An engineering decision record."""

    id: str
    title: str
    description: str
    made_by: str
    rationale: str
    alternatives_considered: list[str] = Field(default_factory=list)
    consequences: list[str] = Field(default_factory=list)
    status: DecisionStatus = DecisionStatus.PENDING
    decision_date: datetime = Field(default_factory=datetime.utcnow)
    tags: list[str] = Field(default_factory=list)


class Risk(BaseModel):
    """A program risk."""

    id: str
    title: str
    description: str
    category: str  # technical, schedule, resource, external
    probability: str  # low, medium, high
    impact: str  # low, medium, high, critical
    mitigation: str = ""
    owner: str = ""
    status: str = "open"
    identified_by: str = ""
    identified_at: datetime = Field(default_factory=datetime.utcnow)


class WorkItem(BaseModel):
    """A work item for an agent."""

    id: str
    title: str
    description: str
    assigned_to: str
    status: WorkItemStatus = WorkItemStatus.BACKLOG
    priority: int = 0
    dependencies: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class WorkPackage(BaseModel):
    """A work package tracking discrete work units through SDLC phases."""

    id: str = Field(description="Unique work package identifier")
    title: str = Field(description="Work package title")
    description: str = Field(description="Detailed description")
    assigned_to: str = Field(description="Agent or team responsible")
    status: WorkPackageStatus = Field(
        default=WorkPackageStatus.QUEUED,
        description="Current status in orchestration queue",
    )
    priority: int = Field(default=0, description="Priority for execution")
    dependencies: list[str] = Field(
        default_factory=list, description="IDs of dependent work packages"
    )
    traceability_links: list[str] = Field(
        default_factory=list, description="Linked requirement IDs"
    )
    gate_evidence: dict[str, Any] = Field(
        default_factory=dict, description="Evidence artifacts for gate validation"
    )
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: datetime | None = Field(default=None)


class BoardDecision(BaseModel):
    """Result from a review board."""

    board_name: str
    decision: str  # approved, rejected, deferred, approved_with_conditions
    votes: dict[str, str] = Field(default_factory=dict)
    conditions: list[str] = Field(default_factory=list)
    rationale: str = ""
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class VerificationStatus(BaseModel):
    """Overall verification status."""

    total_requirements: int = 0
    verified_requirements: int = 0
    failed_requirements: int = 0
    coverage_percentage: float = 0.0
    last_updated: datetime = Field(default_factory=datetime.utcnow)


class StateMetadata(BaseModel):
    """Metadata about the state."""

    session_id: str = ""
    started_at: datetime = Field(default_factory=datetime.utcnow)
    last_updated: datetime = Field(default_factory=datetime.utcnow)
    iteration_count: int = 0
    active_agents: list[str] = Field(default_factory=list)


class AgentState(BaseModel):
    """Represents shared graph state exchanged across supervisor and specialist agents."""

    # Core workflow
    objective: str = ""
    phase: Phase = Phase.INTAKE
    work_queue: list[WorkItem] = Field(default_factory=list)
    work_packages: dict[str, WorkPackage] = Field(
        default_factory=dict, description="Work packages indexed by ID"
    )
    active_board: str | None = None

    # Engineering artifacts
    requirements: dict[str, Requirement] = Field(
        default_factory=dict, description="Requirements indexed by ID"
    )
    architecture: dict[str, Any] = Field(
        default_factory=dict, description="Architecture documents and diagrams"
    )
    risks: dict[str, Risk] = Field(default_factory=dict, description="Risk register")
    decisions: dict[str, Decision] = Field(
        default_factory=dict, description="Decision log"
    )

    # Communication
    messages: list[str] = Field(
        default_factory=list, description="Inter-agent messages"
    )
    agent_outputs: dict[str, Any] = Field(
        default_factory=dict, description="Latest output from each agent"
    )

    # Governance
    board_results: dict[str, BoardDecision] = Field(
        default_factory=dict, description="Review board decisions"
    )
    current_gate: str | None = None
    gate_readiness: dict[str, Any] = Field(
        default_factory=dict,
        description="Current governance gate readiness declaration",
    )
    governance_validation: dict[str, Any] = Field(
        default_factory=dict,
        description="Latest governance validation report",
    )
    governance_metrics: dict[str, Any] = Field(
        default_factory=dict,
        description="KPI tracking and gate outcome metrics",
    )
    requires_human_approval: bool = False
    human_feedback: str | None = None

    # Status tracking
    verification_status: VerificationStatus = Field(
        default_factory=VerificationStatus
    )
    backlog: list[str] = Field(
        default_factory=list, description="General backlog items"
    )

    # Metadata
    metadata: StateMetadata = Field(default_factory=StateMetadata)
