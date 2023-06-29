import random
import string
from abc import ABC, abstractmethod

import bcrypt

from ..models.manager import Manager
from ..models.user import User
from ..repositories.manager_repository import ManagerRepository


class ManagerService(ABC):
    @abstractmethod
    def create_manager(self, user: User, password: str) -> None:
        pass

    @abstractmethod
    def delete_manager(self, user_id: int) -> None:
        pass

    @abstractmethod
    def get_manager_by_login(self, login: str) -> Manager:
        pass


class ManagerServiceImpl(ManagerService):
    def __init__(self, repository: ManagerRepository) -> None:
        self.__repository = repository

    def create_manager(self, user: User, password: str = '') -> None:
        manager = Manager()
        manager.user_id = user.id
        manager.login = user.username
        if password == '':
            password = self.__generate_password()

        manager.password = bcrypt.hashpw(bytearray(password.encode('utf-8')), bcrypt.gensalt(14))
        self.__repository.save_manager(manager)

    def delete_manager(self, user_id: int) -> None:
        self.__repository.delete_manager(user_id=user_id)

    def get_manager_by_login(self, login: str) -> Manager:
        return self.__repository.get_manager_by_login(login=login)

    @staticmethod
    def __generate_password() -> str:
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(7))
