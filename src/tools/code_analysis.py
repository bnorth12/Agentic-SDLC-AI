"""Code analysis tools for agents."""

from __future__ import annotations

import ast
from typing import Any

from src.utils.logging import get_logger

logger = get_logger(__name__)


def parse_python_code(code: str) -> dict[str, Any]:
    """
    Parse Python code and extract structure information.

    Args:
        code: Python source code

    Returns:
        Dictionary with code structure information
    """
    try:
        tree = ast.parse(code)

        functions = []
        classes = []
        imports = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(
                    {
                        "name": node.name,
                        "args": [arg.arg for arg in node.args.args],
                        "lineno": node.lineno,
                    }
                )
            elif isinstance(node, ast.ClassDef):
                methods = [
                    n.name for n in node.body if isinstance(n, ast.FunctionDef)
                ]
                classes.append(
                    {"name": node.name, "methods": methods, "lineno": node.lineno}
                )
            elif isinstance(node, (ast.Import, ast.ImportFrom)):
                if isinstance(node, ast.Import):
                    imports.extend([alias.name for alias in node.names])
                else:
                    module = node.module or ""
                    imports.extend([f"{module}.{alias.name}" for alias in node.names])

        result = {
            "functions": functions,
            "classes": classes,
            "imports": list(set(imports)),
            "valid": True,
        }

        logger.debug(
            f"Parsed Python code: {len(functions)} functions, {len(classes)} classes"
        )
        return result

    except SyntaxError as e:
        logger.warning(f"Syntax error parsing Python code: {e}")
        return {
            "functions": [],
            "classes": [],
            "imports": [],
            "valid": False,
            "error": str(e),
        }


def count_lines_of_code(code: str) -> dict[str, int]:
    """
    Count lines of code, comments, and blank lines.

    Args:
        code: Source code

    Returns:
        Dictionary with line counts
    """
    lines = code.split("\n")
    total = len(lines)
    blank = sum(1 for line in lines if not line.strip())
    comments = sum(1 for line in lines if line.strip().startswith("#"))
    code_lines = total - blank - comments

    return {
        "total": total,
        "code": code_lines,
        "comments": comments,
        "blank": blank,
    }


def extract_docstrings(code: str) -> list[str]:
    """
    Extract docstrings from Python code.

    Args:
        code: Python source code

    Returns:
        List of docstrings found
    """
    try:
        tree = ast.parse(code)
        docstrings = []

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
                docstring = ast.get_docstring(node)
                if docstring:
                    docstrings.append(docstring)

        return docstrings
    except SyntaxError:
        return []


def validate_code_style(code: str) -> dict[str, Any]:
    """
    Perform basic code style validation.

    Args:
        code: Source code to validate

    Returns:
        Dictionary with style issues found
    """
    issues = []
    lines = code.split("\n")

    for i, line in enumerate(lines, 1):
        # Check line length
        if len(line) > 100:
            issues.append({"line": i, "type": "line_too_long", "length": len(line)})

        # Check trailing whitespace
        if line.endswith(" ") or line.endswith("\t"):
            issues.append({"line": i, "type": "trailing_whitespace"})

        # Check mixed tabs and spaces
        if "\t" in line and "    " in line:
            issues.append({"line": i, "type": "mixed_indentation"})

    return {"total_issues": len(issues), "issues": issues}
