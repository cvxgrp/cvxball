from pathlib import Path

import pytest


@pytest.fixture(name="root_dir")
def root_fixture() -> Path:
    return Path(__file__).parent.parent.parent
