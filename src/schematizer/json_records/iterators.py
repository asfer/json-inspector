import gzip
import sys
from pathlib import Path
from typing import Dict, Iterator

from schematizer.json_records.codecs import decode_json


def stdin_json_iterator() -> Iterator[Dict]:
    for line in sys.stdin:
        yield decode_json(line.strip())


def jsonl_file_iterator(file: Path) -> Iterator[Dict]:
    with open(str(file), 'r') as f:
        for line in f:
            yield decode_json(line.strip())


def jsonl_gz_file_iterator(file: Path) -> Iterator[Dict]:
    with gzip.open(str(file), 'rt') as f:
        for line in f:
            yield decode_json(line.strip())
