from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional


class Person(BaseModel):
    id: UUID
    name: str


class Event(BaseModel):
    id: UUID
    title: str
    description: str = ""
    time: datetime
    attendees: list[Person]
    cancelled: bool = False


class EventOptional(Event):
    __annotations__ = {k: Optional[v] for k, v in Event.__annotations__.items()}
