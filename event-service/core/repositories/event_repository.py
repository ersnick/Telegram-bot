from sqlalchemy import or_, and_

from .db.connections import DBConnection, PostgresConnection
from ..models.event import *

connections: DBConnection = PostgresConnection()
session = connections.session()


def get_all_events() -> list[Event]:
    return session.query(Event).all()


def get_event_by_id(event_id: int) -> Event:
    return session.query(Event).filter(Event.id == event_id).first()


def create_event(event: Event) -> None:
    session.query(Event).add(event)
    session.commit()


def update_event(event: Event) -> None:
    session.query(Event).filter(Event.id == event.id).update({'title': event.title,
                                                              'is_image_exist': event.is_image_exist,
                                                              'image_path': event.image_path,
                                                              'text': event.text,
                                                              'has_feedback': event.has_feedback,
                                                              'event_time': event.event_time,
                                                              'is_student_event': event.is_student_event,
                                                              'is_group_event': event.is_group_event})
    session.commit()


def delete_event(event_id: int) -> None:
    session.query(Event).filter(Event.id == event_id).delete()
    session.commit()


def get_all_students_by_event_id(event_id: int):
    return session.query(EventStudent).filter(EventStudent.event_id == event_id).all()


def get_all_groups_by_event_id(event_id: int) -> list:
    return session.query(EventGroup).filter(EventGroup.event_id == event_id).all()


def delete_all_students_from_event(event_id: int) -> None:
    session.query(EventStudent).filter(EventStudent.event_id == event_id).delete()
    session.commit()


def delete_student_from_event(event_id: int, student_id: int) -> None:
    session.query(EventStudent).filter(and_(EventStudent.event_id == event_id,
                                            EventStudent.student_id == student_id)).delete()
    session.commit()


def add_student_to_event(student: EventStudent) -> None:
    session.add(student)
    session.commit()


def delete_group_from_event(event_id: int, group_id: int) -> None:
    session.query(EventGroup).filter(and_(EventGroup.event_id == event_id,
                                          EventGroup.group_id == group_id)).delete()
    session.commit()


def delete_all_group_from_event(event_id: int) -> None:
    session.query(EventGroup).filter(EventGroup.event_id == event_id).delete()
    session.commit()


def add_group_to_event(group: EventGroup) -> None:
    session.add(group)
    session.commit()
