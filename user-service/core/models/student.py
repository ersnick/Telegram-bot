from dataclasses import dataclass

from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey

from ..repositories.db.base import Base


@dataclass
class Student(Base):
    __tablename__ = 'students'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    user_id = Column(INTEGER, ForeignKey('users.id'))
    name = Column(VARCHAR(35), nullable=False)
    surname = Column(VARCHAR(35), nullable=False)
    patronymic = Column(VARCHAR(35), nullable=False)
    group_id = Column(INTEGER, ForeignKey('groups.id'))
