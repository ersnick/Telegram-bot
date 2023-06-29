from abc import ABC, abstractmethod

from .manager_service import ManagerService
from .role_service import RoleService
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
    def create_manager(self, user_id: int = 0, username: str = '', password: str = '') -> None:
        pass

    @abstractmethod
    def delete_manager_by_id(self, user_id: int) -> None:
        pass

    @abstractmethod
    def update_user_role(self, user_id: int, role_id: int) -> None:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        pass


class UserServiceImpl(UserService):
    def __init__(self,
                 repository: UserRepository,
                 statement_service: StatementService,
                 student_service: StudentService,
                 role_service: RoleService,
                 manager_service: ManagerService) -> None:
        self.__repository = repository
        self.__statement_service = statement_service
        self.__student_service = student_service
        self.__role_service = role_service
        self.__manager_service = manager_service

    def get_all_users(self) -> list[User]:
        return self.__repository.get_all_user()

    def save_user(self, user: User) -> None:
        self.__repository.save_user(user)

    def register(self, statement: Statement) -> None:
        self.__statement_service.save_statement(statement)

    def accept_student(self, statement: Statement) -> None:
        saved_statement: Statement = self.__statement_service.get_statement_by_user_id(statement.user_id)
        if saved_statement.is_checked:
            raise Exception('Statement already checked')

        statement.is_checked = True
        self.__statement_service.check_statement(statement_id=statement.id)

        student = self.__student_service.convert_statement_to_student(statement=statement)
        self.__student_service.save_student(student=student)

        role = self.__role_service.get_role_by_name('STUDENT')
        self.update_user_role(user_id=student.user_id, role_id=role.id)

    def dismiss_user(self, statement_id: int) -> None:
        self.__statement_service.check_statement(statement_id=statement_id)

    def create_manager(self, user_id: int = 0, username: str = '', password: str = '') -> None:
        user: User
        if user_id == 0:
            user = self.__repository.get_user_by_id(user_id=user_id)
        elif username == '':
            user = self.get_user_by_username(username=username)
        else:
            raise Exception('user_id and username is empty')

        self.__manager_service.create_manager(user=user, password=password)
        role = self.__role_service.get_role_by_name('MANAGER')
        self.update_user_role(user_id=user_id, role_id=role.id)

    def delete_manager_by_id(self, user_id: int = 0, username: str = '') -> None:
        user: User
        if user_id == 0:
            user = self.__repository.get_user_by_id(user_id=user_id)
        elif username == '':
            user = self.get_user_by_username(username=username)
        else:
            raise Exception('user_id and username is empty')

        self.__manager_service.delete_manager(user_id=user.id)
        role = self.__role_service.get_role_by_name('USER')
        self.update_user_role(user_id=user_id, role_id=role.id)

    def update_user_role(self, user_id: int, role_id: int) -> None:
        self.__repository.update_user_role(user_id=user_id, role_id=role_id)

    def get_user_by_username(self, username: str) -> User:
        return self.__repository.get_user_by_username(username=username)
