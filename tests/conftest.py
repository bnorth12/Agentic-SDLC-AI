"""Pytest configuration and fixtures."""

import pytest

from src.config import get_settings
from src.state.schema import AgentState
from src.utils.logging import setup_logging


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Setup test environment once for entire session."""
    setup_logging()


@pytest.fixture
def settings():
    """Provide test settings."""
    return get_settings()


@pytest.fixture
def clean_state():
    """Provide a fresh AgentState for each test."""
    return AgentState(objective="Test objective")


@pytest.fixture
def state_with_objective():
    """Provide a state with a defined objective."""
    return AgentState(objective="Build a REST API for task management")


def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--slow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "slow: mark test as slow to run")
    config.addinivalue_line("markers", "integration: mark test as integration test")
    config.addinivalue_line("markers", "e2e: mark test as end-to-end test")


def pytest_collection_modifyitems(config, items):
    """Modify test collection based on command line options."""
    if config.getoption("--slow"):
        # Run all tests if --slow is specified
        return

    skip_slow = pytest.mark.skip(reason="need --slow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)
