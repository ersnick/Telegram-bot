from abc import ABC, abstractmethod

from core.models.student import Student
from sqlalchemy.orm import Session


class StudentRepository(ABC):
    @abstractmethod
    def save_student(self, student: Student) -> None:
        pass

    @abstractmethod
    def get_all_students(self) -> list[Student]:
        pass

    @abstractmethod
    def update_student(self, student: Student) -> None:
        pass

    @abstractmethod
    def delete_student(self, student_id: int) -> None:
        pass

    @abstractmethod
    def get_student_by_filter(self, student: Student) -> list[Student]:
        pass


class StudentRepositoryImpl(StudentRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def save_student(self, student: Student) -> None:
        with self.__session.begin():
            self.__session.add(student)
            self.__session.commit()

    def get_all_students(self) -> list[Student]:
        students: list[Student] = []
        with self.__session.begin():
            students = self.__session.query(Student).get
            self.__session.commit()

        return students

    def update_student(self, student: Student) -> None:
        with self.__session.begin():
            self.__session.add(student)
            self.__session.commit()

    def delete_student(self, student_id: int) -> None:
        with self.__session.begin():
            student = self.__session.query(Student).filter(Student.id == student_id).one()
            self.__session.delete(student)
            self.__session.commit()

    def get_student_by_filter(self, student: Student) -> list[Student]:
        students: list[Student] = []
        with self.__session.begin():
            students = self.__session.query(Student).filter(Student.name == student.name
                                                 or Student.patronymic == student.patronymic
                                                 or Student.surname == student.surname).all()
            self.__session.commit()
        return students
