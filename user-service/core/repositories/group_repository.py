from abc import ABC, abstractmethod

from sqlalchemy.orm.session import Session

from ..models.group import Group


class GroupRepository(ABC):
    @abstractmethod
    def get_all_groups(self) -> list[Group]:
        pass

    @abstractmethod
    def get_group_by_title(self, title: str) -> Group:
        pass

    @abstractmethod
    def get_group_by_filter(self, title: str) -> list[Group]:
        pass

    @abstractmethod
    def create_group(self, group: Group) -> None:
        pass

    @abstractmethod
    def delete_group(self, group_id: int) -> None:
        pass

    @abstractmethod
    def update_group(self, group: Group) -> None:
        pass

    @abstractmethod
    def get_group_by_id(self, group_id: int) -> Group:
        pass


class GroupRepositoryImpl(GroupRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_all_groups(self) -> list[Group]:
        groups = self.__session.query(Group).all()
        self.__session.commit()
        return groups

    def get_group_by_title(self, title: str) -> Group:
        group = self.__session.query(Group).filter(Group.title == title).first()
        self.__session.commit()
        return group

    def get_group_by_filter(self, title: str) -> list[Group]:
        groups = self.__session.query(Group).filter(Group.title.like(f'%{title}%'))
        if not groups:
            groups = []
        else:
            groups = groups.all()
        self.__session.commit()
        return groups

    def create_group(self, group: Group) -> None:
        self.__session.add(group)
        self.__session.commit()

    def delete_group(self, group_id: int) -> None:
        self.__session.query(Group).filter(Group.id == group_id).delete()
        self.__session.commit()

    def update_group(self, group: Group) -> None:
        self.__session.query(Group).filter(Group.id == group.id).update(group)
        self.__session.commit()

    def get_group_by_id(self, group_id: int) -> Group:
        group = self.__session.query(Group).filter(Group.id == group_id).first()
        self.__session.commit()
        return group
