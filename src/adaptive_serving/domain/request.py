from dataclasses import dataclass

@dataclass
class Request:
    input_data: str
    request_id: str | None = None
