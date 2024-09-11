from pydantic import BaseModel


class Location(BaseModel):
    id: int
    name: str
    state: str
