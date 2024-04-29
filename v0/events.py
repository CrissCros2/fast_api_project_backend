from datetime import datetime
from uuid import uuid4, UUID

from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session

from api_models import Event, Person
from crud import EventCRUD
from db import get_db

events = APIRouter()


@events.get("/")
async def get_all_events(db: Session = Depends(get_db)) -> list[Event]:
    """
    Access the database and get the list of all events
    """
    return EventCRUD.get_all_events(db)


@events.post("/create_no_persons", status_code=status.HTTP_201_CREATED)
async def create_event_without_persons(
    event: Event, db: Session = Depends(get_db)
) -> Event:
    """
    Create event in database
    """
    return EventCRUD.create_without_persons(
        db, event.id, event.title, event.description, event.time
    )


@events.post("/create_with_persons", status_code=status.HTTP_201_CREATED)
async def create_event_with_persons(
    event: Event, persons: list[Person], db: Session = Depends(get_db)
) -> Event:
    """
    Create event in database
    """
    return EventCRUD.create_with_persons(
        db, event.title, event.description, event.time, persons
    )


@events.get("/{event_id}")
async def get_event(event_id: UUID) -> Event:
    """
    Get individual event by event_id
    """
    return Event(
        id=uuid4(), title="blah", description="blah", time=datetime.now(), attendees=[]
    )


@events.put("/{event_id}", status_code=status.HTTP_200_OK)
async def update_event(event_id: UUID, event: Event) -> Event:
    """
    Update individual event by event_id
    """
    return event


@events.delete("/{event_id}", status_code=status.HTTP_200_OK)
async def delete_event(event_id: UUID) -> None:
    """
    Delete individual event by event_id
    """
    return


@events.patch("/{event_id}/cancel", status_code=status.HTTP_200_OK)
async def flip_cancel_event(event_id: UUID) -> None:
    """
    Cancel or un-cancel an event
    """
    return
