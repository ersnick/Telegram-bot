import logging

from ..repositories.student_repository import StudentRepository
from ..models.student import Student

logger = logging.getLogger()


class StudentService:
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
