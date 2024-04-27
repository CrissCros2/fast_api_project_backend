from fastapi import APIRouter
from starlette import status

from api_models import Event


events = APIRouter()


@events.get("/")
async def get_all_events() -> list[Event]:
    """
    Access the database and get the list of all events
    """
    # For now stubbed out
    return []


@events.post("/", status_code=status.HTTP_201_CREATED)
async def create_event(event: Event):
    """
    Create event in database
    """
    return
