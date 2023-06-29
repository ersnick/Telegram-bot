from .repositories.db.connections import DBConnection, get_postgres_connection
from .repositories.role_repository import RoleRepository, RoleRepositoryImpl
from .repositories.statement_repository import StatementRepository, StatementRepositoryImpl
from .repositories.student_repository import StudentRepository, StudentRepositoryImpl
from .repositories.user_repository import UserRepository, UserRepositoryImpl
from .service.role_service import RoleService, RoleServiceImpl
from .service.statement_service import StatementService, StatementServiceImpl
from .service.student_service import StudentService, StudentServiceImpl
from .service.user_service import UserService, UserServiceImpl


class ComponentsContainer:
    __connection: DBConnection = get_postgres_connection()

    __role_repository: RoleRepository = RoleRepositoryImpl(session=__connection.session())
    __role_service: RoleService = RoleServiceImpl(repository=__role_repository)

    __statement_repository: StatementRepository = StatementRepositoryImpl(session=__connection.session())
    __statement_service: StatementService = StatementServiceImpl(repository=__statement_repository)

    __student_repository: StudentRepository = StudentRepositoryImpl(session=__connection.session())
    __student_service: StudentService = StudentServiceImpl(repository=__student_repository)

    __user_repository: UserRepository = UserRepositoryImpl(session=__connection.session())
    __user_service: UserService = UserServiceImpl(repository=__user_repository,
                                                  statement_service=__statement_service,
                                                  student_service=__student_service,
                                                  role_service=__role_service)

    @property
    def get_db_connections(self) -> DBConnection:
        return self.__connection

    @property
    def user_service(self) -> UserService:
        return self.__user_service

    @property
    def statement_service(self) -> StatementService:
        return self.__statement_service

    @property
    def role_service(self) -> RoleService:
        return self.__role_service

    @property
    def student_service(self) -> StudentService:
        return self.__student_service
