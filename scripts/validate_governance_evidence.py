"""Validate governance evidence in agent outputs before marking a gate ready."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from rich.console import Console
from rich.table import Table

from src.tools.governance_validation import validate_outputs

console = Console()


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate governance evidence fields in agent outputs before a gate can be marked ready."
        )
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to a JSON file containing one output object or a list of outputs.",
    )
    parser.add_argument(
        "--gate",
        help="Gate identifier (for example: gate_2, gate-2, Gate 2, g2).",
    )
    parser.add_argument(
        "--allow-conditional",
        action="store_true",
        help="Allow READY_WITH_CONDITIONS to count as gate-ready.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print full JSON validation report.",
    )
    return parser.parse_args()


def _load_input(path: Path) -> list[dict[str, Any]]:
    raw = json.loads(path.read_text(encoding="utf-8"))

    if isinstance(raw, list):
        return [item for item in raw if isinstance(item, dict)]

    if isinstance(raw, dict):
        if isinstance(raw.get("outputs"), list):
            return [item for item in raw["outputs"] if isinstance(item, dict)]
        return [raw]

    raise ValueError("Input JSON must be an object, an object with 'outputs', or a list.")


def _print_summary(report: dict[str, Any]) -> None:
    table = Table(title="Governance Evidence Validation")
    table.add_column("Agent", style="cyan")
    table.add_column("Gate", style="magenta")
    table.add_column("Valid", style="bold")
    table.add_column("Gate Ready", style="bold")
    table.add_column("Details")

    for result in report["results"]:
        issues = []
        if result["missing_fields"]:
            issues.append(f"missing fields: {', '.join(result['missing_fields'])}")
        if result["invalid_values"]:
            issues.append(f"invalid values: {', '.join(result['invalid_values'])}")
        if result["missing_evidence_keys"]:
            issues.append(
                "missing evidence: " + ", ".join(result["missing_evidence_keys"])
            )
        if result["warnings"]:
            issues.append(f"warnings: {', '.join(result['warnings'])}")

        table.add_row(
            result["agent"],
            result["gate"],
            "[green]PASS[/]" if result["valid"] else "[red]FAIL[/]",
            "[green]READY[/]" if result["gate_ready"] else "[yellow]NOT READY[/]",
            "; ".join(issues) if issues else "All required fields and evidence present",
        )

    console.print(table)
    console.print(
        f"\nOverall valid: {'YES' if report['overall_valid'] else 'NO'} | "
        f"Gate can be marked ready: {'YES' if report['gate_can_be_marked_ready'] else 'NO'}"
    )


def main() -> None:
    args = _parse_args()
    input_path = Path(args.input)

    if not input_path.exists():
        console.print(f"[bold red]Input file not found:[/] {input_path}")
        sys.exit(2)

    try:
        outputs = _load_input(input_path)
        if not outputs:
            console.print("[bold red]No valid output objects found in input file.[/]")
            sys.exit(2)

        report = validate_outputs(
            outputs,
            expected_gate=args.gate,
            require_strict_ready=not args.allow_conditional,
        )

        _print_summary(report)

        if args.json:
            console.print_json(json.dumps(report, indent=2))

        sys.exit(0 if report["gate_can_be_marked_ready"] else 1)

    except Exception as exc:
        console.print(f"[bold red]Validation error:[/] {exc}")
        sys.exit(2)


if __name__ == "__main__":
    main()
