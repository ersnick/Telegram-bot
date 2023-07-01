from abc import ABC, abstractmethod

from core.deps import ComponentsContainer
from core.models import student

from ..models.student_dto import Student

ioc = ComponentsContainer()


class StudentService(ABC):
    @abstractmethod
    def get_all_students(self) -> list[Student]:
        pass

    @abstractmethod
    def get_student_by_id(self, student_id: int) -> Student:
        pass

    @abstractmethod
    def get_students_by_group(self, group_name: str) -> list[Student]:
        pass

    @abstractmethod
    def delete_student_by_id(self, student_id: int) -> None:
        pass

    @abstractmethod
    def update_student(self, update_student: Student) -> None:
        pass


class StudentServiceImpl(StudentService):
    def __init__(self) -> None:
        self.__student_service = ioc.student_service
        self.__group_service = ioc.group_service
        self.__user_service = ioc.user_service

    def get_all_students(self) -> list[Student]:
        saved_student = self.__student_service.get_all_students()
        students = []
        for student in saved_student:
            group = self.__group_service.get_group_by_id(group_id=student.group_id)
            students.append(Student(id=student.id,
                                    name=student.name,
                                    surname=student.surname,
                                    patronymic=student.patronymic,
                                    group=group.title))
        return students

    def get_student_by_id(self, student_id: int) -> Student:
        student = self.__student_service.get_student_by_id(student_id=student_id)
        group = self.__group_service.get_group_by_id(student.group_id)
        return Student(id=student.id,
                       name=student.name,
                       surname=student.surname,
                       patronymic=student.patronymic,
                       group=group.title)

    def get_students_by_group(self, group_name: str) -> list[Student]:
        saved_students = self.__student_service.get_students_by_filter(group_name=group_name)
        students = []
        for student in saved_students:
            group = self.__group_service.get_group_by_id(group_id=student.group_id)
            students.append(Student(id=student.id,
                                    name=student.name,
                                    surname=student.surname,
                                    patronymic=student.patronymic,
                                    group=group.title))
        return students

    def delete_student_by_id(self, student_id: int) -> None:
        self.__user_service.delete_student_by_id(student_id=student_id)

    def update_student(self, update_student: Student) -> None:
        saved_student = self.__student_service.get_student_by_id(student_id=update_student.id)
        group = self.__group_service.get_group_by_title(title=update_student.group)
        updated_student = student.Student(id=saved_student.id,
                                          user_id=saved_student.user_id,
                                          name=update_student.name,
                                          surname=update_student.surname,
                                          patronymic=update_student.patronymic,
                                          group_id=group.id)

        self.__student_service.update_student(update_student=updated_student)
