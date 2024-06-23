import gzip
from pathlib import Path
from typing import Dict, List

from schematizer.json_records.codecs import encode_json


def create_jsonl_file(file: Path, records: List[Dict]):
    with open(str(file), 'w') as f:
        for r in records:
            f.write(encode_json(r) + '\n')


def create_jsonl_gz_file(file: Path, records: List[Dict]):
    with gzip.open(str(file), 'wt') as f:
        for r in records:
            f.write(encode_json(r) + '\n')
