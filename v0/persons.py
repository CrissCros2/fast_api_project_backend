from fastapi import APIRouter
from uuid import uuid4

from api_models import Person


persons = APIRouter()


@persons.get("/")
def get_persons() -> list[Person]:
    """
    Get all persons
    """
    return [Person(id=uuid4(), name=str(uuid4()))]
