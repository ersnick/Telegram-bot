import logging

from ..repositories.student_repository import StudentRepository
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
    def update_student(self, update_student: Student):
        pass

    @abstractmethod
    def delete_student_by_id(self, student_id: int):
        pass

    @abstractmethod
    def get_students_by_filter(self, fcs: str = '', group_name: str = '') -> list[Student]:
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
    def __init__(self, repository: StudentRepository) -> None:
        self.__repository = repository

    def get_all_students(self) -> list[Student]:
        pass

    def update_student(self, update_student: Student):
        pass

    def delete_student_by_id(self, student_id: int):
        pass

    def get_students_by_filter(self, fcs: str = '', group_name: str = '') -> list[Student]:
        pass

    def save_student(self, student: Student) -> None:
        self.__repository.save_student(student=student)
