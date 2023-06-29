from abc import ABC, abstractmethod

from ..models.statement import Statement
from ..models.user import User
from ..repositories.statement_repository import StatementRepository
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


class UserServiceImpl(UserService):
    def __init__(self, user_repository: UserRepository, statement_repository: StatementRepository) -> None:
        self.__user_repository = user_repository
        self.__statement_repository = statement_repository

    def get_all_users(self) -> list[User]:
        pass

    def save_user(self, user: User):
        self.__user_repository.save_user(user)

    def register(self, statement: Statement) -> None:
        pass

    def accept_student(self, statement: Statement) -> None:
        pass

    def dismiss_user(self, statement_id: int) -> None:
        pass

    def create_manager(self, user_id: int) -> None:
        pass

    def delete_manager(self, user_id: int) -> None:
        pass
