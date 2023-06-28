from ..repositories.group_repository import GroupRepository
from ..models.group import Group


class GroupService:
    def __init__(self, repository: GroupRepository) -> None:
        self.__repository = repository

    def get_all_groups(self) -> list[Group]:
        pass

    def create_group(self, group: Group) -> Group:
        pass

    def update_group(self, group: Group) -> Group:
        pass

    def delete_group(self, group_id: int) -> None:
        pass

    def get_group_by_title(self, title: str = '') -> list[Group]:
        pass
