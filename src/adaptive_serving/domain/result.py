from dataclasses import dataclass

@dataclass
class Result:
    status: str
    output: str | None = None
