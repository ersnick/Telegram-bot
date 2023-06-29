from abc import ABC, abstractmethod

from core.models.statement import Statement

from ..repositories.statement_repository import StatementRepository


class StatementService(ABC):
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

    @abstractmethod
    def check_statement(self, statement_id: int) -> None:
        pass


class StatementServiceImpl(StatementService):
    def __init__(self, repository: StatementRepository) -> None:
        self.__repository = repository

    def save_statement(self, statement: Statement) -> None:
        self.__repository.save_statement(statement=statement)

    def get_all_statement(self) -> list[Statement]:
        return self.__repository.get_all_statement()

    def get_not_checked_statement(self) -> list[Statement]:
        return self.__repository.get_not_checked_statement()

    def get_statement_by_user_id(self, user_id: int) -> Statement:
        return self.__repository.get_statement_by_user_id(user_id=user_id)

    def check_statement(self, statement_id: int) -> None:
        self.__repository.check_statement(statement_id=statement_id)
