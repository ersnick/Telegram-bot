from datetime import datetime, date, time
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN, DATE, ForeignKey, Table, TIMESTAMP

from ..repositories.db.base import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    title = Column(VARCHAR, nullable=False)
    is_image_exist = Column(BOOLEAN, nullable=False, default=False)
    image_path = Column(VARCHAR, nullable=True)
    text = Column(VARCHAR, nullable=True)
    has_feedback = Column(BOOLEAN, nullable=False, default=False)
    event_time = Column(TIMESTAMP, nullable=False)
    is_student_event = Column(BOOLEAN, nullable=False, default=False)
    is_group_event = Column(BOOLEAN, nullable=False, default=False)


class EventGroup(Base):
    __tablename__ = 'event_group'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    event_id = Column(INTEGER, ForeignKey('events.id'))
    group_id = Column(INTEGER, nullable=False)


class EventStudent(Base):
    __tablename__ = 'event_student'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    event_id = Column(INTEGER, ForeignKey('events.id'))
    student_id = Column(INTEGER, nullable=False)


class EventDTO(BaseModel):
    id: Optional[int]
    title: str
    is_image_exist: bool
    image_path: Optional[str]
    text: str
    has_feedback: bool
    event_time: datetime
    is_student_event: bool
    is_group_event: bool
    students: Optional[list]
    groups: Optional[list]


class EventRepeat(Base):
    __tablename__ = 'events_repeat'

    id = Column(INTEGER, primary_key=True)
    event_id: Column(INTEGER, ForeignKey('events.id'), nullable=False)
    send_time: Column(DATE, nullable=False)


class EventFeedback:
    id: int
    event_id: int
    send_time: datetime
