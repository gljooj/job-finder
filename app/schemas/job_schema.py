from pydantic import BaseModel


class ServiceCategory(BaseModel):
    id: int
    name: str


class Job(BaseModel):
    id: int
    category: str
    location: str


class JobInput(BaseModel):
    category: str
    location: str


class JobOutput(BaseModel):
    id: int
    category: str
    location: str
