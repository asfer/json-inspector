import orjson


def decode_json(s: str) -> dict:
    return orjson.loads(s)


def encode_json(o: dict) -> str:
    return orjson.dumps(o).decode()
