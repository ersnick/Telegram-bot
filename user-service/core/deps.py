from .repositories.db.connections import DBConnection, get_postgres_connection
from .repositories.group_repository import GroupRepository, GroupRepositoryImpl
from .repositories.manager_repository import ManagerRepository, ManagerRepositoryImpl
from .repositories.role_repository import RoleRepository, RoleRepositoryImpl
from .repositories.statement_repository import StatementRepository, StatementRepositoryImpl
from .repositories.student_repository import StudentRepository, StudentRepositoryImpl
from .repositories.user_repository import UserRepository, UserRepositoryImpl
from .service.group_service import GroupService, GroupServiceImpl
from .service.manager_service import ManagerService, ManagerServiceImpl
from .service.role_service import RoleService, RoleServiceImpl
from .service.statement_service import StatementService, StatementServiceImpl
from .service.student_service import StudentService, StudentServiceImpl
from .service.user_service import UserService, UserServiceImpl


class ComponentsContainer:
    __connection: DBConnection = get_postgres_connection()

    __group_repository: GroupRepository = GroupRepositoryImpl(session=__connection.session())
    __group_service: GroupService = GroupServiceImpl(repository=__group_repository)

    __manager_repository: ManagerRepository = ManagerRepositoryImpl(session=__connection.session())
    __manager_service: ManagerService = ManagerServiceImpl(repository=__manager_repository)

    __role_repository: RoleRepository = RoleRepositoryImpl(session=__connection.session())
    __role_service: RoleService = RoleServiceImpl(repository=__role_repository)

    __statement_repository: StatementRepository = StatementRepositoryImpl(session=__connection.session())
    __statement_service: StatementService = StatementServiceImpl(repository=__statement_repository)

    __student_repository: StudentRepository = StudentRepositoryImpl(session=__connection.session())
    __student_service: StudentService = StudentServiceImpl(repository=__student_repository,
                                                           group_service=__group_service)

    __user_repository: UserRepository = UserRepositoryImpl(session=__connection.session())
    __user_service: UserService = UserServiceImpl(repository=__user_repository,
                                                  statement_service=__statement_service,
                                                  student_service=__student_service,
                                                  role_service=__role_service,
                                                  manager_service=__manager_service)

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

    @property
    def group_service(self) -> GroupService:
        return self.__group_service
