import tempfile
from pathlib import Path
from typing import Generator

from pytest import fixture


@fixture
def tmp_dir() -> Generator[Path, None, None]:
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)
