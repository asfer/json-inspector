"""
JSON Schematizer

Usage:
    schematizer [--file=<file>]
    schematizer --help

Options:
    -f=<file> --file=<file>     JSON file (otherwise assumes stdin)
    -h --help                   Shows this screen
"""

import sys
from pathlib import Path
from typing import Dict, Iterator

from docopt import docopt

from schematizer.json_records.iterators import jsonl_file_iterator, jsonl_gz_file_iterator, stdin_json_iterator


def parse_args(args: Dict) -> Path | None:
    file = args['--file']
    path = Path(file) if file else None
    if path and not path.exists():
        print(f'File does not exist: {file}')
        sys.exit()
    return path


def json_records_iterator(file: Path) -> Iterator[Dict]:
    if not file:
        yield from stdin_json_iterator()
    elif any(file.name.endswith(ext) for ext in ['.json', '.jsonl']):
        yield from jsonl_file_iterator(file)
    elif any(file.name.endswith(ext) for ext in ['.json.gz', '.jsonl.gz']):
        yield from jsonl_gz_file_iterator(file)
    else:
        raise Exception(f'File extension not supported: {file.name}')


def main():
    args = docopt(__doc__)
    file = parse_args(args)

    for r in json_records_iterator(file):
        print(r)


if __name__ == '__main__':
    main()
