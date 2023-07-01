from dataclasses import dataclass

from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN, ForeignKey

from ..repositories.db.base import Base


@dataclass
class Statement(Base):
    __tablename__ = 'statements'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    user_id = Column(INTEGER, ForeignKey('users.id'), unique=True)
    name = Column(VARCHAR(35), nullable=False)
    surname = Column(VARCHAR(35), nullable=False)
    patronymic = Column(VARCHAR(35), nullable=False)
    group_id = Column(INTEGER, ForeignKey('groups.id'))
    is_checked = Column(BOOLEAN, nullable=False, default=False)
