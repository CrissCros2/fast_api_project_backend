from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class Person(BaseModel):
    id: UUID
    name: str


class Task(BaseModel):
    id: UUID
    title: str
    description: str
    time: datetime
    attendees: list[Person]
