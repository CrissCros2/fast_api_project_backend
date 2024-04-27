from fastapi import APIRouter
from api_models import Event


events = APIRouter()


@events.get("/")
def get_all_events() -> list[Event]:
    """
    Access the database and get the list of all events
    """
    # For now stubbed out
    return []
