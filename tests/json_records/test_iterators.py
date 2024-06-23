import sys
from io import StringIO

from schematizer.json_records.codecs import encode_json
from schematizer.json_records.iterators import jsonl_file_iterator, jsonl_gz_file_iterator, stdin_json_iterator
from tests import test_utils

RECORDS = [{'foo': 'bar'}, {'baz': 'qux'}]
ENCODED_RECORDS = '\n'.join(encode_json(r) for r in RECORDS)


def test_stdin_json_iterator():
    tmp_stdin = sys.stdin
    try:
        sys.stdin = StringIO(ENCODED_RECORDS)

        gen = stdin_json_iterator()
        assert next(gen) == RECORDS[0]
        assert next(gen) == RECORDS[1]
    finally:
        sys.stin = tmp_stdin


def test_jsonl_file_iterator(tmp_dir):
    file = tmp_dir / 'foo.jsonl'
    test_utils.create_jsonl_file(file, RECORDS)

    gen = jsonl_file_iterator(file)
    assert next(gen) == RECORDS[0]
    assert next(gen) == RECORDS[1]


def test_jsonl_gz_file_iterator(tmp_dir):
    file = tmp_dir / 'foo.jsonl.gz'
    test_utils.create_jsonl_gz_file(file, RECORDS)

    gen = jsonl_gz_file_iterator(file)
    assert next(gen) == RECORDS[0]
    assert next(gen) == RECORDS[1]
