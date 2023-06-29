from dataclasses import dataclass

from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey

from ..repositories.db.base import Base


@dataclass
class Manager(Base):
    __tablename__ = 'managers'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    login = Column(VARCHAR(35), nullable=False)
    password = Column(VARCHAR, nullable=False)
    user_id = Column(INTEGER, ForeignKey('users.id'))
