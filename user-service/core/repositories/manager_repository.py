from abc import ABC, abstractmethod

from sqlalchemy.orm.session import Session

from ..models.manager import Manager


class ManagerRepository(ABC):
    @abstractmethod
    def save_manager(self, manager: Manager) -> None:
        pass

    @abstractmethod
    def delete_manager(self, user_id: int) -> None:
        pass

    @abstractmethod
    def get_manager_by_login(self, login: str) -> Manager:
        pass


class ManagerRepositoryImpl(ManagerRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def save_manager(self, manager: Manager) -> None:
        with self.__session.begin():
            self.__session.add(manager)
            self.__session.commit()

    def delete_manager(self, user_id: int) -> None:
        with self.__session.begin():
            self.__session.query(Manager).filter(Manager.user_id == user_id).delete()
            self.__session.commit()

    def get_manager_by_login(self, login: str) -> Manager:
        with self.__session.begin():
            manager = self.__session.query(Manager).filter(Manager.login == login).one()
            self.__session.commit()
        return manager
