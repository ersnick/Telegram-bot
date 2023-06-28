from dotenv import load_dotenv
from core.repositories.db.connections import get_db_connection


def main():
    get_db_connection()


if __name__ == '__main__':
    load_dotenv('../.env')
    main()
