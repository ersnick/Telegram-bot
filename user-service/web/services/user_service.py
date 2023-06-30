from abc import ABC, abstractmethod
from core.deps import ComponentsContainer
from ..models.user_dto import User

ioc = ComponentsContainer()


class UserService(ABC):
    @abstractmethod
    def get_all_users(self) -> list[User]:
        pass


class UserServiceImpl(UserService):
    def __init__(self) -> None:
        self.__user_service = ioc.statement_service
        self.__role_service = ioc.role_service

    def get_all_users(self) -> list[User]:
        saved_user = self.__user_service.get_all_users()
        users = []
        for user in saved_user:
            role = self.__role_service.get_role_by_id(role_id=user.role_id)
            users.append(User(id=user.id, username=user.username, role=role.name))
        return users
