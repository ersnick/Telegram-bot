from .repositories.db.connections import DBConnection, get_postgres_connection
from .repositories.statement_repository import StatementRepository, StatementRepositoryImpl
from .repositories.student_repository import StudentRepository, StudentRepositoryImpl
from .repositories.user_repository import UserRepository, UserRepositoryImpl
from .service.statement_service import StatementService, StatementServiceImpl
from .service.student_service import StudentService, StudentServiceImpl
from .service.user_service import UserService, UserServiceImpl
from .service.role_service import RoleService, RoleServiceImpl
from .repositories.role_repository import RoleRepository, RoleRepositoryImpl

connection: DBConnection = get_postgres_connection()

role_repository: RoleRepository = RoleRepositoryImpl(session=connection.session())
role_service: RoleService = RoleServiceImpl(repository=role_repository)

statement_repository: StatementRepository = StatementRepositoryImpl(session=connection.session())
statement_service: StatementService = StatementServiceImpl(repository=statement_repository)

student_repository: StudentRepository = StudentRepositoryImpl(session=connection.session())
student_service: StudentService = StudentServiceImpl(repository=student_repository)

user_repository: UserRepository = UserRepositoryImpl(session=connection.session())
user_service: UserService = UserServiceImpl(repository=user_repository,
                                            statement_service=statement_service,
                                            student_service=student_service,
                                            role_service=role_service)


def get_db_connections() -> DBConnection:
    return connection


def get_user_service() -> UserService:
    return user_service


def get_user_repository() -> UserRepository:
    return user_repository


def get_statement_repository() -> StatementRepository:
    return statement_repository
