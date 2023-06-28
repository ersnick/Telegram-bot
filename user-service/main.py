import logging
from logging import INFO

from dotenv import load_dotenv

from core.repositories.db.connections import get_db_connection
from core.repositories.user_repository import UserRepository
from core.service.user_service import UserService


def main():
    session = get_db_connection()
    repo = UserRepository(session=session)
    service = UserService(repository=repo)


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
