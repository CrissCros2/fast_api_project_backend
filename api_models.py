from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Person(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str


class Event(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    title: str
    description: str = ""
    time: datetime
    attendees: list[Person] = []
    cancelled: bool = False
