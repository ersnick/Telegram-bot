import logging

from ..repositories.student_repository import StudentRepository
from .group_service import GroupService
from ..models.student import Student
from ..models.statement import Statement
from abc import ABC, abstractmethod

logger = logging.getLogger()


class StudentService(ABC):
    @abstractmethod
    def save_student(self, student: Student) -> None:
        pass

    @abstractmethod
    def get_all_students(self) -> list[Student]:
        pass

    @abstractmethod
    def update_student(self, update_student: Student) -> None:
        pass

    @abstractmethod
    def delete_student_by_id(self, student_id: int) -> None:
        pass

    @abstractmethod
    def get_students_by_filter(self, fcs: str = '', group_name: str = '') -> list[Student]:
        pass

    @abstractmethod
    def get_student_by_id(self, student_id: int) -> Student:
        pass

    @staticmethod
    def convert_statement_to_student(statement: Statement) -> Student:
        student = Student()
        student.name = statement.name
        student.surname = statement.surname
        student.patronymic = statement.patronymic
        student.group_id = statement.group_id
        student.user_id = statement.user_id

        return student


class StudentServiceImpl(StudentService):
    def __init__(self,
                 repository: StudentRepository,
                 group_service: GroupService) -> None:
        self.__repository = repository
        self.__group_service = group_service

    def get_all_students(self) -> list[Student]:
        return self.__repository.get_all_students()

    def update_student(self, update_student: Student) -> None:
        self.__repository.update_student(student=update_student)

    def delete_student_by_id(self, student_id: int) -> None:
        self.__repository.delete_student(student_id=student_id)

    def get_students_by_filter(self,
                               name: str = '',
                               surname: str = '',
                               patronymic: str = '',
                               group_name: str = '') -> list[Student]:
        group = self.__group_service.get_group_by_title(group_name)
        return self.__repository.get_students_by_filter(name=name,
                                                        surname=surname,
                                                        patronymic=patronymic,
                                                        group_id=group.id)

    def save_student(self, student: Student) -> None:
        self.__repository.save_student(student=student)

    def get_student_by_id(self, student_id: int) -> Student:
        return self.__repository.get_student_by_id(student_id=student_id)
