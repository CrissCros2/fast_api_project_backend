from fastapi import APIRouter
from uuid import uuid4

from starlette import status

from api_models import Person


persons = APIRouter()


@persons.get("/")
def get_persons() -> list[Person]:
    """
    Get all persons
    """
    return [Person(id=uuid4(), name=str(uuid4()))]


@persons.post("/", status_code=status.HTTP_201_CREATED)
def create_person(person: Person) -> Person:
    """
    Create a new person
    """
    return person
