from abc import ABC, abstractmethod

from .statement_service import StatementService
from .student_service import StudentService
from ..models.statement import Statement
from ..models.user import User
from ..repositories.user_repository import UserRepository


class UserService(ABC):
    @abstractmethod
    def get_all_users(self) -> list[User]:
        pass

    @abstractmethod
    def save_user(self, user: User):
        pass

    @abstractmethod
    def register(self, statement: Statement) -> None:
        pass

    @abstractmethod
    def accept_student(self, statement: Statement) -> None:
        pass

    @abstractmethod
    def dismiss_user(self, statement_id: int) -> None:
        pass

    @abstractmethod
    def create_manager(self, user_id: int) -> None:
        pass

    @abstractmethod
    def delete_manager(self, user_id: int) -> None:
        pass

    @abstractmethod
    def update_user_role(self, user_id: int, role_id: int) -> None:
        pass


class UserServiceImpl(UserService):
    def __init__(self,
                 repository: UserRepository,
                 statement_service: StatementService,
                 student_service: StudentService) -> None:
        self.__repository = repository
        self.__statement_service = statement_service
        self.__student_service = student_service

    def get_all_users(self) -> list[User]:
        return self.__repository.get_all_user()

    def save_user(self, user: User) -> None:
        self.__repository.save_user(user)

    def register(self, statement: Statement) -> None:
        self.__statement_service.save_statement(statement)

    def accept_student(self, statement: Statement) -> None:
        statement.is_checked = True
        self.__statement_service.check_statement(statement_id=statement.id)
        student = self.__student_service.convert_statement_to_student(statement=statement)
        self.__student_service.save_student(student=student)
        # self.update_user_role(user_id=student.user_id, role_id=?)#TODO сделать получение роли студента

    def dismiss_user(self, statement_id: int) -> None:
        self.__statement_service.check_statement(statement_id=statement_id)

    def create_manager(self, user_id: int) -> None:
        pass

    def delete_manager(self, user_id: int) -> None:
        pass

    def update_user_role(self, user_id: int, role_id: int) -> None:
        self.__repository.update_user_role(user_id=user_id, role_id=role_id)
