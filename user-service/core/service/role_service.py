from abc import ABC, abstractmethod
from ..repositories.role_repository import RoleRepository
from ..models.role import Role


class RoleService(ABC):
    @abstractmethod
    def get_role_by_name(self, name: str) -> Role:
        pass

    @abstractmethod
    def get_role_by_id(self, role_id: int) -> Role:
        pass


class RoleServiceImpl(RoleService):
    def __init__(self, repository: RoleRepository) -> None:
        self.__repository = repository

    def get_role_by_name(self, name: str) -> Role:
        return self.__repository.get_role_by_name(name=name)

    def get_role_by_id(self, role_id: int) -> Role:
        return self.__repository.get_role_by_id(role_id=role_id)
