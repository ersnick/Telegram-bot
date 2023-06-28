from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def getBase():
    return Base
