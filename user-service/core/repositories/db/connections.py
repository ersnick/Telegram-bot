from sqlalchemy import create_engine, MetaData, Column, Table, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.engine import Engine
from dotenv import dotenv_values

config = dotenv_values()


def get_db_connection():
    engine = get_engine()
    create_db(engine)


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
    metadata = MetaData()
    users = Table('users', metadata,
                  Column('id', INTEGER(), primary_key=True),
                  Column('username', VARCHAR(35))
                  )

    group = Table('student_group', metadata,
                  Column('id', INTEGER(), autoincrement=True, primary_key=True),
                  Column('title', VARCHAR(10), nullable=False)
                  )

    student = Table('student', metadata,
                    Column('id', INTEGER(), autoincrement=True, primary_key=True),
                    Column('user_id', INTEGER(), ForeignKey('users.id')),
                    Column('name', VARCHAR(35), nullable=False),
                    Column('surname', VARCHAR(35), nullable=False),
                    Column('patronymic', VARCHAR(35), nullable=False),
                    Column('group_id', INTEGER(), ForeignKey('group.id'))
                    )

    role = Table('role', metadata,
                 Column('id', INTEGER(), autoincrement=True, primary_key=True),
                 Column('name', VARCHAR(20), nullable=False)
                 )

    user_role = Table('user_role', metadata,
                      Column('role_id', INTEGER(), ForeignKey('role.id')),
                      Column('user_id', INTEGER(), ForeignKey('user.id'))
                      )

    metadata.create_all(engine)
