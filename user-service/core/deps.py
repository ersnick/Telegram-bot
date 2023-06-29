from .repositories.db.connections import DBConnection, get_postgres_connection
from .repositories.statement_repository import StatementRepository, StatementRepositoryImpl
from .repositories.user_repository import UserRepository, UserRepositoryImpl
from .service.user_service import UserService, UserServiceImpl

connection: DBConnection = get_postgres_connection()
user_repository: UserRepository = UserRepositoryImpl(session=connection.session())
statement_repository: StatementRepository = StatementRepositoryImpl(session=connection.session())
user_service: UserService = UserServiceImpl(user_repository=user_repository, statement_repository=statement_repository)


def get_db_connections() -> DBConnection:
    return connection


def get_user_service() -> UserService:
    return user_service


def get_user_repository() -> UserRepository:
    return user_repository


def get_statement_repository() -> StatementRepository:
    return statement_repository
