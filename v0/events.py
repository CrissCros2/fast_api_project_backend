from fastapi import APIRouter
from api_models import Event


events = APIRouter()


@events.get("/")
def get_all_events() -> list[Event]:
    pass
