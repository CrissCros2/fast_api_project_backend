from fastapi import APIRouter
from starlette import status
from uuid import uuid4
from datetime import datetime

from api_models import Event


events = APIRouter()


@events.get("/")
async def get_all_events() -> list[Event]:
    """
    Access the database and get the list of all events
    """
    # For now returns a single event
    return [Event(id=uuid4(), title="blah", description="blah", time=datetime.now(), attendees=[])]


@events.post("/", status_code=status.HTTP_201_CREATED)
async def create_event(event: Event) -> Event:
    """
    Create event in database
    """
    return event
