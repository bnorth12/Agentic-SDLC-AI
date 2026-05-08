"""File operation tools for agents."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.utils.logging import get_logger

logger = get_logger(__name__)


def read_file(file_path: str) -> str:
    """
    Read content from a file.

    Args:
        file_path: Path to the file to read

    Returns:
        File contents as string
    """
    try:
        path = Path(file_path)
        content = path.read_text(encoding="utf-8")
        logger.debug(f"Read file: {file_path} ({len(content)} bytes)")
        return content
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")
        raise


def write_file(file_path: str, content: str) -> None:
    """
    Write content to a file.

    Args:
        file_path: Path to the file to write
        content: Content to write
    """
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        logger.debug(f"Wrote file: {file_path} ({len(content)} bytes)")
    except Exception as e:
        logger.error(f"Error writing file {file_path}: {e}")
        raise


def read_json(file_path: str) -> Any:
    """
    Read and parse JSON from a file.

    Args:
        file_path: Path to the JSON file

    Returns:
        Parsed JSON data
    """
    content = read_file(file_path)
    return json.loads(content)


def write_json(file_path: str, data: Any, indent: int = 2) -> None:
    """
    Write data as JSON to a file.

    Args:
        file_path: Path to the file to write
        data: Data to serialize as JSON
        indent: JSON indentation level
    """
    content = json.dumps(data, indent=indent, ensure_ascii=False)
    write_file(file_path, content)


def list_files(directory: str, pattern: str = "*") -> list[str]:
    """
    List files in a directory matching a pattern.

    Args:
        directory: Directory to search
        pattern: Glob pattern (default: all files)

    Returns:
        List of file paths
    """
    try:
        path = Path(directory)
        files = [str(f) for f in path.glob(pattern) if f.is_file()]
        logger.debug(f"Listed {len(files)} files in {directory}")
        return files
    except Exception as e:
        logger.error(f"Error listing files in {directory}: {e}")
        raise


def ensure_directory(directory: str) -> None:
    """
    Ensure a directory exists, creating it if necessary.

    Args:
        directory: Directory path to ensure exists
    """
    Path(directory).mkdir(parents=True, exist_ok=True)
    logger.debug(f"Ensured directory exists: {directory}")
