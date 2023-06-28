from ..repositories.user_repository import UserRepository
from ..models.user import User


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.__repository = repository

    def get_all_users(self) -> list[User]:
        pass

    def register(self, user: User) -> None:
        pass

    def accept_student(self, user_id: int) -> None:
        pass

    def create_manager(self, user_id: int) -> None:
        pass

    def delete_manager(self, user_id: int) -> None:
        pass
