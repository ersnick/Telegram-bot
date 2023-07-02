from ..exceptions.illegal_argument_exception import IllegalArgumentException
from ..models.event import *
from ..repositories import event_repository as repository


def get_all_events() -> list[EventDTO]:
    saved_events = repository.get_all_events()
    events = []
    for event in saved_events:
        events.append(EventDTO(id=event.id,
                               title=event.title,
                               is_image_exist=event.is_image_exist,
                               image_path=event.image_path,
                               text=event.text,
                               has_feedback=event.has_feedback,
                               event_time=event.event_time,
                               is_student_event=event.is_student_event,
                               is_group_event=event.is_group_event,
                               students=[],
                               groups=[]))
    return events


def get_event_by_id(event_id: int) -> EventDTO:
    event = repository.get_event_by_id(event_id=event_id)
    students_id = []
    if event.is_student_event:
        students = repository.get_all_students_by_event_id(event_id=event_id)
        students_id = [st.student_id for st in students]
    groups_id = []
    if event.is_group_event:
        groups = repository.get_all_groups_by_event_id(event_id=event_id)
        groups_id = [gr.group_id for gr in groups]
    return EventDTO(id=event.id,
                    title=event.title,
                    is_image_exist=event.is_image_exist,
                    image_path=event.image_path,
                    text=event.text,
                    has_feedback=event.has_feedback,
                    event_time=event.event_time,
                    is_student_event=event.is_student_event,
                    is_group_event=event.is_group_event,
                    students=students_id,
                    groups=groups_id)


def create_event(event: EventDTO) -> None:
    new_event = Event(title=event.title,
                      is_image_exist=event.is_image_exist,
                      image_path=event.image_path,
                      text=event.text,
                      has_feedback=event.has_feedback,
                      event_time=event.event_time,
                      is_student_event=event.is_student_event,
                      is_group_event=event.is_group_event)
    check_event_time(new_event.event_time)
    saved_event_id = repository.create_event(event=new_event)
    if new_event.is_student_event:
        for student in event.students:
            repository.add_student_to_event(EventStudent(student_id=student, event_id=saved_event_id))
    if new_event.is_group_event:
        for group in event.groups:
            repository.add_group_to_event(EventGroup(group_id=group, event_id=saved_event_id))


def check_event_time(event_time: datetime):
    if event_time < datetime.now():
        raise IllegalArgumentException('Event must be after than now')


def update_event(event: EventDTO) -> None:
    u_event = Event(id=event.id,
                    title=event.title,
                    is_image_exist=event.is_image_exist,
                    image_path=event.image_path,
                    text=event.text,
                    has_feedback=event.has_feedback,
                    event_time=event.event_time,
                    is_student_event=event.is_student_event,
                    is_group_event=event.is_group_event)
    check_event_time(u_event.event_time)
    update_student_event(event=event)
    update_group_event(event=event)
    repository.update_event(event=u_event)


def update_student_event(event: EventDTO):
    students = repository.get_all_students_by_event_id(event_id=event.id)
    students_id = [st.student_id for st in students]
    if event.is_student_event:
        for student in students_id:
            if not (student in event.students):
                repository.delete_student_from_event(event_id=event.id, student_id=student)
        for student in event.students:
            if not (student in students_id):
                repository.add_student_to_event(EventStudent(student_id=student, event_id=event.id))
    else:
        repository.delete_all_students_from_event(event_id=event.id)


def update_group_event(event: EventDTO):
    groups = repository.get_all_groups_by_event_id(event_id=event.id)
    groups_id = [gr.group_id for gr in groups]
    if event.is_group_event:
        for group in groups_id:
            if not (group in event.groups):
                repository.delete_group_from_event(event_id=event.id, group_id=group)
        for group in event.groups:
            if not (group in groups_id):
                repository.add_group_to_event(EventGroup(group_id=group, event_id=event.id))
    else:
        repository.delete_all_group_from_event(event_id=event.id)


def delete_event_by_id(event_id: int) -> None:
    repository.delete_all_group_from_event(event_id=event_id)
    repository.delete_all_students_from_event(event_id=event_id)
    repository.delete_event(event_id=event_id)
