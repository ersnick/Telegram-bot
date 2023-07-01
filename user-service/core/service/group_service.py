from abc import ABC, abstractmethod

from ..exceptions.illegal_argument_exception import IllegalArgumentException
from ..models.group import Group
from ..repositories.group_repository import GroupRepository


class GroupService(ABC):
    @abstractmethod
    def get_all_groups(self) -> list[Group]:
        pass

    @abstractmethod
    def create_group(self, group: Group) -> None:
        pass

    @abstractmethod
    def update_group(self, group: Group) -> None:
        pass

    @abstractmethod
    def delete_group(self, group_id: int) -> None:
        pass

    @abstractmethod
    def get_group_by_title(self, title: str = '') -> Group:
        pass

    @abstractmethod
    def get_group_by_filter(self, title: str = '') -> list[Group]:
        pass

    @abstractmethod
    def get_group_by_id(self, group_id: int) -> Group:
        pass


class GroupServiceImpl(GroupService):
    def __init__(self, repository: GroupRepository) -> None:
        self.__repository = repository

    def get_all_groups(self) -> list[Group]:
        return self.__repository.get_all_groups()

    def create_group(self, group: Group) -> None:
        self.__repository.create_group(group=group)

    def update_group(self, group: Group) -> None:
        self.__repository.update_group(group=group)

    def delete_group(self, group_id: int) -> None:
        self.__repository.delete_group(group_id=group_id)

    def get_group_by_title(self, title: str = '') -> Group:
        group = self.__repository.get_group_by_title(title=title)
        if group is None:
            raise IllegalArgumentException(f'Group with title "{title}" not found')
        return group

    def get_group_by_filter(self, title: str = '') -> list[Group]:
        return self.__repository.get_group_by_filter(title=title)

    def get_group_by_id(self, group_id: int) -> Group:
        group = self.__repository.get_group_by_id(group_id=group_id)
        if group is None:
            raise IllegalArgumentException(f'Group with id {group_id} not found')
        return group
