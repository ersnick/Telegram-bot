from abc import ABC, abstractmethod
from core.models.statement import Statement
from sqlalchemy.orm import Session


class StatementRepository(ABC):
    @abstractmethod
    def save_statement(self, statement: Statement):
        pass

    @abstractmethod
    def get_all_statement(self):
        pass

    @abstractmethod
    def get_not_checked_statement(self):
        pass

    @abstractmethod
    def get_statement_by_user_id(self, user_id: int):
        pass


class StatementRepositoryImpl(StatementRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def save_statement(self, statement: Statement):
        with self.__session.begin():
            self.__session.add(statement)
            self.__session.commit()

    def get_all_statement(self):
        pass

    def get_not_checked_statement(self):
        pass

    def get_statement_by_user_id(self, user_id: int):
        pass
