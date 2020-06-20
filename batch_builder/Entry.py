from dataclasses import dataclass

@dataclass
class Entry:
    Id: str
    MessageBody: str
    DelaySeconds: int
    MessageAttributes: dict