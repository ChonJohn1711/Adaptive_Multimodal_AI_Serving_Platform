def to_json(obj) -> str:
    import json
    return json.dumps(obj, default=str)
