from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    surname: str
    patronymic: str
    group: str
