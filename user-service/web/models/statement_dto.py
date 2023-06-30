from pydantic import BaseModel


class Statement(BaseModel):
    id: int
    name: str
    surname: str
    patronymic: str
    group: str
    is_checked: bool
