def validate_request(payload: dict) -> bool:
    return isinstance(payload, dict) and 'input' in payload
