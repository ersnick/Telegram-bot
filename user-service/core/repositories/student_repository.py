from abc import ABC, abstractmethod

from core.models.student import Student
from sqlalchemy import or_
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
    def get_student_by_filter(self,
                              name: str,
                              surname: str,
                              patronymic: str,
                              group_id: int) -> list[Student]:
        pass


class StudentRepositoryImpl(StudentRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def save_student(self, student: Student) -> None:
        with self.__session.begin():
            self.__session.add(student)
            self.__session.commit()

    def get_all_students(self) -> list[Student]:
        with self.__session.begin():
            students = self.__session.query(Student).all()
            self.__session.commit()

        return students

    def update_student(self, student: Student) -> None:
        with self.__session.begin():
            self.__session.query(Student).filter(Student.id == student.id).update(student)
            self.__session.commit()

    def delete_student(self, student_id: int) -> None:
        with self.__session.begin():
            student = self.__session.query(Student).filter(Student.id == student_id).one()
            self.__session.delete(student)
            self.__session.commit()

    def get_student_by_filter(self,
                              name: str,
                              surname: str,
                              patronymic: str,
                              group_id: int) -> list[Student]:
        with self.__session.begin():
            students = self.__session.query(Student) \
                .filter(or_(Student.name.like(f'%{name}%'),
                            Student.patronymic.like(f'%{patronymic}%'),
                            Student.surname.like(f'%{surname}%'),
                            Student.group_id == group_id)).all()

            self.__session.commit()
        return students
