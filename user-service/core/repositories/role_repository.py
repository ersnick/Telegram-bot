from abc import ABC, abstractmethod
from sqlalchemy.orm.session import Session
from ..models.role import Role


class RoleRepository(ABC):
    @abstractmethod
    def get_role_by_name(self, name: str) -> Role:
        pass

    @abstractmethod
    def get_role_by_id(self, role_id: int) -> Role:
        pass


class RoleRepositoryImpl(RoleRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_role_by_name(self, name: str) -> Role:
        # with self.__session.begin():
        role = self.__session.query(Role).filter(Role.name == name).one()
        self.__session.close()
        return role

    def get_role_by_id(self, role_id: int) -> Role:
        role = self.__session.query(Role).filter(Role.id == role_id).one()
        self.__session.close()
        return role
