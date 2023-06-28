from dataclasses import dataclass
from sqlalchemy import Column


@dataclass
class User:
    id = Column()
    username: str
