import psycopg2
from dotenv import dotenv_values

config = dotenv_values()


def get_db_connections():
    try:
        conn = psycopg2.connect(dbname=config['DB_NAME'],
                                user=config['DB_HOST'],
                                password=config['DB_USER_NAME'],
                                host=config['DB_USER_PASSWORD'])
        yield conn
    except:
        print('Failed to connect to the database')
