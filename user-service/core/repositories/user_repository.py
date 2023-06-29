from abc import ABC, abstractmethod

from core.models.user import User
from sqlalchemy.orm import Session


class UserRepository(ABC):
    @abstractmethod
    def save_user(self, user: User) -> None:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_all_user(self) -> list[User]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def update_user_role(self, user_id: int, role_id) -> None:
        pass


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_user(self, user_id: int) -> User:
        with self.__session.begin():
            user = self.__session.query(User).filter(User.id == user_id).one()
            self.__session.commit()
        return user

    def get_all_user(self) -> list[User]:
        with self.__session.begin():
            users = self.__session.query(User)
            self.__session.commit()
        return users

    def get_user_by_id(self, user_id: int) -> User:
        with self.__session.begin():
            user = self.__session.query(User).filter(User.id == user_id).one()
            self.__session.commit()
        return user

    def get_user_by_username(self, username: str) -> User:
        with self.__session.begin():
            user = self.__session.query(User).filter(User.login == username).one()
            self.__session.commit()
        return user

    def save_user(self, user: User) -> None:
        with self.__session.begin():
            self.__session.add(user)
            self.__session.commit()

    def update_user_role(self, user_id: int, role_id) -> None:
        with self.__session.begin():
            self.__session.query(User).filter(User.id == user_id).update({'role_id': role_id})
            self.__session.commit()
