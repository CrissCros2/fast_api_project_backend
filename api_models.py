from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class Person(BaseModel):
    id: UUID
    name: str

    class Config:
        from_attributes = True


class Event(BaseModel):
    id: UUID
    title: str
    description: str = ""
    time: datetime
    attendees: list[Person]
    cancelled: bool = False

    class Config:
        from_attributes = True
