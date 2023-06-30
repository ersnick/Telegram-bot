from abc import ABC, abstractmethod

from core.deps import ComponentsContainer
from core.models import group

from ..models.group_dto import Group

ioc = ComponentsContainer()


class GroupService(ABC):
    @abstractmethod
    def get_all_groups(self) -> list[Group]:
        pass

    @abstractmethod
    def get_group_by_id(self, group_id: int) -> Group:
        pass

    @abstractmethod
    def get_groups_by_filter(self, title: str) -> list[Group]:
        pass

    @abstractmethod
    def create_group(self, new_group: Group) -> None:
        pass

    @abstractmethod
    def update_group(self, update_group: Group) -> None:
        pass

    @abstractmethod
    def delete_group_by_id(self, group_id: int) -> None:
        pass


class GroupServiceImpl(GroupService):
    def __init__(self) -> None:
        self.__group_service = ioc.group_service

    def get_all_groups(self) -> list[Group]:
        saved_groups = self.__group_service.get_all_groups()
        groups = []
        for group in saved_groups:
            groups.append(Group(id=group.id, title=group.title))
        return groups

    def get_group_by_id(self, group_id: int) -> Group:
        saved_group = self.__group_service.get_group_by_id(group_id=group_id)
        return Group(id=saved_group.id, title=saved_group.title)

    def get_groups_by_filter(self, title: str) -> list[Group]:
        saved_groups = self.__group_service.get_group_by_filter(title=title)
        groups = []
        for group in saved_groups:
            groups.append(Group(id=group.id, title=group.title))
        return groups

    def create_group(self, new_group: Group) -> None:
        self.__group_service.create_group(group.Group(title=new_group.title))

    def update_group(self, update_group: Group) -> None:
        self.__group_service.update_group(group.Group(title=update_group.title))

    def delete_group_by_id(self, group_id: int) -> None:
        self.__group_service.delete_group(group_id=group_id)
