from dataclasses import dataclass


@dataclass
class User:
    id: int
    telegram_nick: str
