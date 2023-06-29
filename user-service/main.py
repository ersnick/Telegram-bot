import logging
from logging import INFO

from dotenv import load_dotenv

from core.deps import ComponentsContainer
from core.service.user_service import UserService
from core.models.statement import Statement


def main():
    ioc = ComponentsContainer()
    user_service: UserService = ioc.user_service
    # statement = Statement(id=1,
    #                       user_id=1007,
    #                       name='test name',
    #                       surname='test surname',
    #                       patronymic='test patronymic',
    #                       group_id=99999)
    # user_service.accept_student(statement)

    user = user_service.get_user_by_username('un')
    print(f'{user.id} {user.username}')


def __config_logger():
    file_log = logging.FileHandler('user-service.log')
    console_log = logging.StreamHandler()
    FORMAT = '[%(levelname)s] %(asctime)s : %(message)s | %(filename)s'
    logging.basicConfig(level=INFO,
                        format=FORMAT,
                        handlers=(file_log, console_log),
                        datefmt='%d-%m-%y - %H:%M:%S')


if __name__ == '__main__':
    __config_logger()
    load_dotenv('../.env')
    main()
