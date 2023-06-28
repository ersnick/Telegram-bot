from core.models.user import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def save_user(self, user: User):
        with self.__session.begin():
            self.__session.add(user)
            self.__session.commit()
