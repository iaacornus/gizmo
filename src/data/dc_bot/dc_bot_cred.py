from dataclasses import dataclass


@dataclass
class DCBot:
    """Bot credentials."""

    token: str
    ref_uid: int
