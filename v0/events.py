from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
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
async def get_event(event_id: UUID, db: Session = Depends(get_db)):
    """
    Get individual event by event_id
    """
    db_event = EventCRUD.read_by_id(db, event_id)
    if db_event:
        return db_event
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Person not found"},
    )


@events.put("/{event_id}", status_code=status.HTTP_200_OK)
async def update_event(event_id: UUID, event: Event):
    """
    Update individual event by event_id
    """
    return NotImplementedError


@events.delete("/{event_id}", status_code=status.HTTP_200_OK)
async def delete_event(event_id: UUID, db: Session = Depends(get_db)):
    """
    Delete individual event by event_id
    """
    db_event = EventCRUD.delete_by_id(db, event_id)
    if db_event:
        return db_event
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Person not found"},
    )


@events.patch("/{event_id}/cancel", status_code=status.HTTP_200_OK)
async def flip_cancel_event(event_id: UUID) -> None:
    """
    Cancel or un-cancel an event
    """
    return
