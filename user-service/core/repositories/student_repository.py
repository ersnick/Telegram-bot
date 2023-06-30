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
    def get_student_by_id(self, student_id: int) -> Student:
        pass

    @abstractmethod
    def get_students_by_filter(self,
                               name: str,
                               surname: str,
                               patronymic: str,
                               group_id: int) -> list[Student]:
        pass


class StudentRepositoryImpl(StudentRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def save_student(self, student: Student) -> None:
        self.__session.add(student)
        self.__session.commit()
        self.__session.close()

    def get_all_students(self) -> list[Student]:
        students = self.__session.query(Student).all()
        self.__session.close()

        return students

    def update_student(self, student: Student) -> None:
        self.__session.query(Student).filter(Student.id == student.id).update({'id': student.id,
                                                                               'user_id': student.user_id,
                                                                               'name': student.name,
                                                                               'surname': student.surname,
                                                                               'patronymic': student.patronymic,
                                                                               'group_id': student.group_id})
        self.__session.commit()
        self.__session.close()

    def delete_student(self, student_id: int) -> None:
        student = self.__session.query(Student).filter(Student.id == student_id).one()
        self.__session.delete(student)
        self.__session.commit()
        self.__session.close()

    def get_student_by_id(self, student_id: int) -> Student:
        student = self.__session.query(Student).filter(Student.id == student_id).one()
        self.__session.close()
        return student

    def get_students_by_filter(self,
                               name: str,
                               surname: str,
                               patronymic: str,
                               group_id: int) -> list[Student]:
        students = self.__session.query(Student) \
            .filter(or_(Student.name.like(f'%{name}%'),
                        Student.patronymic.like(f'%{patronymic}%'),
                        Student.surname.like(f'%{surname}%'),
                        Student.group_id == group_id)).all()

        self.__session.close()
        return students
