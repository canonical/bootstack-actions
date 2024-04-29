"""Configuration for Test charm functional tets."""

import pytest
from _pytest.config import argparsing
from _pytest.fixtures import FixtureRequest

DEFAULT_SERIES = "jammy"


def pytest_addoption(parser: argparsing.Parser) -> None:
    """Add custom CLI options."""
    parser.addoption(
        "--series",
        type=str,
        default=DEFAULT_SERIES,
        help="create lxd controllers with series",
    )


@pytest.fixture(scope="module")
def series(request: FixtureRequest) -> str:
    """Series fixture."""
    return request.config.getoption("--series")
