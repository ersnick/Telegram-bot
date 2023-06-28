from dataclasses import dataclass

from user import User
from group import Group


@dataclass
class Student(User):
    name: str
    surname: str
    patronymic: str
    group: Group
