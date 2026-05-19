"""Runtime skill registry and deterministic skill resolution."""

from __future__ import annotations

from dataclasses import dataclass

from src.skills.contracts import SkillContract, parse_semver


@dataclass(frozen=True)
class SkillBinding:
    """Maps an agent context to a skill contract version."""

    agent_role: str
    gate: str
    discipline: str
    skill_id: str
    version: str


class SkillRegistry:
    """In-memory registry for skill contracts and role/gate bindings."""

    def __init__(self) -> None:
        self._contracts: dict[tuple[str, str], SkillContract] = {}
        self._deprecated: set[tuple[str, str]] = set()
        self._bindings: dict[tuple[str, str, str], list[tuple[str, str]]] = {}

    def register(self, contract: SkillContract) -> None:
        """Register a skill contract version."""
        key = (contract.metadata.skill_id, contract.metadata.version)
        if key in self._contracts:
            raise ValueError(
                "Duplicate skill registration is not allowed for the same skill_id/version"
            )
        self._contracts[key] = contract

    def bind(self, binding: SkillBinding) -> None:
        """Bind a registered skill to an agent-role/gate/discipline context."""
        contract_key = (binding.skill_id, binding.version)
        if contract_key not in self._contracts:
            raise KeyError("Skill must be registered before it can be bound")

        lookup_key = (binding.agent_role, binding.gate, binding.discipline)
        bound = self._bindings.setdefault(lookup_key, [])
        if contract_key not in bound:
            bound.append(contract_key)

    def get(self, skill_id: str, version: str) -> SkillContract:
        """Return a specific skill version."""
        key = (skill_id, version)
        if key not in self._contracts:
            raise KeyError(f"Skill contract not found: {skill_id}@{version}")
        return self._contracts[key]

    def list(self, include_deprecated: bool = False) -> list[SkillContract]:
        """List contracts, optionally including deprecated versions."""
        if include_deprecated:
            return list(self._contracts.values())

        return [
            contract
            for key, contract in self._contracts.items()
            if key not in self._deprecated
        ]

    def deprecate(self, skill_id: str, version: str) -> None:
        """Mark a registered skill version as deprecated."""
        key = (skill_id, version)
        if key not in self._contracts:
            raise KeyError(f"Skill contract not found: {skill_id}@{version}")
        self._deprecated.add(key)

    def resolve(self, agent_role: str, gate: str, discipline: str) -> SkillContract | None:
        """Resolve a bound skill deterministically using highest semantic version."""
        key = (agent_role, gate, discipline)
        candidates = [
            binding_key
            for binding_key in self._bindings.get(key, [])
            if binding_key not in self._deprecated
        ]
        if not candidates:
            return None

        selected = sorted(candidates, key=lambda item: parse_semver(item[1]), reverse=True)[0]
        return self._contracts[selected]
