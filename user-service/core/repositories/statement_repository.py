from abc import ABC, abstractmethod
from core.models.statement import Statement
from sqlalchemy.orm import Session


class StatementRepository(ABC):
    @abstractmethod
    def save_statement(self, statement: Statement) -> None:
        pass

    @abstractmethod
    def get_all_statement(self) -> list[Statement]:
        pass

    @abstractmethod
    def get_not_checked_statement(self) -> list[Statement]:
        pass

    @abstractmethod
    def get_statement_by_user_id(self, user_id: int) -> Statement:
        pass


class StatementRepositoryImpl(StatementRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def save_statement(self, statement: Statement) -> None:
        with self.__session.begin():
            self.__session.add(statement)
            self.__session.commit()

    def get_all_statement(self) -> list[Statement]:
        with self.__session.begin():
            statements = self.__session.query(Statement).all()
            self.__session.commit()
        return statements

    def get_not_checked_statement(self) -> list[Statement]:
        with self.__session.begin():
            statements = self.__session.query(Statement).filter(Statement.is_checked == False).all()
            self.__session.commit()
        return statements

    def get_statement_by_user_id(self, user_id: int) -> Statement:
        with self.__session.begin():
            statement = self.__session.query(Statement).filter(Statement.user_id == user_id).one()
            self.__session.commit()
        return statement
