from dataclasses import dataclass

from sqlalchemy import Column, INTEGER, VARCHAR

from .base import getBase

Base = getBase()


@dataclass
class Group(Base):
    __tablename__ = 'groups'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    title = Column(VARCHAR(10), nullable=False)
