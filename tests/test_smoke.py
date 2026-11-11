"""Smoke tests: the package installs and imports, and its runtime dependencies are present."""

from importlib.metadata import version

import numpy
import scipy

import langbio


def _major_minor(release: str) -> tuple[int, int]:
    major, minor = release.split(".")[:2]
    return int(major), int(minor)


def test_version_matches_installed_metadata() -> None:
    assert langbio.__version__ == version("langbio")


def test_runtime_dependencies_meet_lower_bounds() -> None:
    assert _major_minor(numpy.__version__) >= (2, 0)
    assert _major_minor(scipy.__version__) >= (1, 13)
