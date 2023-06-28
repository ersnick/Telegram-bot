from core.models.base import getBase
from core.models.group import Group
from core.models.role import Role
from core.models.student import Student
from core.models.user import User
from core.models.statement import Statement
from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

config = dotenv_values()


def get_db_connection() -> Session:
    engine = get_engine()
    create_db(engine)
    return Session(bind=engine)


def get_engine() -> Engine:
    try:
        db_url = f'postgresql+psycopg2://{config["DB_USER_NAME"]}:{config["DB_USER_PASSWORD"]}@{config["DB_HOST"]}/{config["DB_NAME"]}'
        engine = create_engine(db_url, echo=True)
        engine.connect()

        return engine
    except:
        print('Failed to connect to the database')
        raise ConnectionError


def create_db(engine: Engine):
    group = Group()
    user = User()
    role = Role()
    student = Student()
    statement = Statement()
    base = getBase()
    base.metadata.create_all(engine)
