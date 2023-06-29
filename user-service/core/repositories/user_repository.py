from abc import ABC, abstractmethod

from core.models.user import User
from sqlalchemy.orm import Session


class UserRepository(ABC):
    @abstractmethod
    def save_user(self, user: User):
        pass

    @abstractmethod
    def get_user(self, user_id: int):
        pass

    @abstractmethod
    def get_all_user(self):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int):
        pass

    @abstractmethod
    def get_user_by_username(self, username: str):
        pass


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_user(self, user_id: int):
        pass

    def get_all_user(self):
        pass

    def get_user_by_id(self, user_id: int):
        pass

    def get_user_by_username(self, username: str):
        pass

    def save_user(self, user: User):
        with self.__session.begin():
            self.__session.add(user)
            self.__session.commit()
