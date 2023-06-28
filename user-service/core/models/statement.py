from dataclasses import dataclass

from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN, ForeignKey

from .base import getBase

Base = getBase()


@dataclass
class Statement(Base):
    __tablename__ = 'statements'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    user_id = Column(INTEGER, ForeignKey('users.id'))
    name = Column(VARCHAR(35), nullable=False)
    surname = Column(VARCHAR(35), nullable=False)
    patronymic = Column(VARCHAR(35), nullable=False)
    group = Column(VARCHAR(10), nullable=False)
    is_checked = Column(BOOLEAN, nullable=False)
