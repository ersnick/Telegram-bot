import logging

from ..repositories.student_repository import StudentRepository
from .group_service import GroupService
from ..models.student import Student
from ..models.statement import Statement
from ..exceptions.illegal_argument_exception import IllegalArgumentException
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
                               name: str = None,
                               surname: str = None,
                               patronymic: str = None,
                               group_name: str = None) -> list[Student]:
        groups = self.__group_service.get_group_by_filter(title=group_name)
        students: list[Student] = []
        for group in groups:
            saved_students = self.__repository.get_students_by_filter(name=name,
                                                                      surname=surname,
                                                                      patronymic=patronymic,
                                                                      group_id=group.id)
            students.extend(saved_students)
        return students

    def save_student(self, student: Student) -> None:
        self.__repository.save_student(student=student)

    def get_student_by_id(self, student_id: int) -> Student:
        student = self.__repository.get_student_by_id(student_id=student_id)
        if student is None:
            raise IllegalArgumentException(f'Student with id {student_id} not found')
        return student
