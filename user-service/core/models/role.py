from dataclasses import dataclass

from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.orm import relationship

from .base import getBase

Base = getBase()


@dataclass
class Role(Base):
    __tablename__ = 'roles'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    users = relationship("User")
