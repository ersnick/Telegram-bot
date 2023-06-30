from pydantic import BaseModel


class Group(BaseModel):
    id: int
    title: str
