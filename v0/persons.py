from fastapi import APIRouter, Depends, HTTPException
from uuid import uuid4
from sqlalchemy.orm import Session

from starlette import status

from api_models import Person
from db import get_db
from crud import PersonCRUD


persons = APIRouter()


@persons.get("/", response_model=list[Person])
def get_persons(db: Session = Depends(get_db)):
    """
    Get all persons
    """
    return PersonCRUD.get_all_persons(db)


@persons.post("/", status_code=status.HTTP_201_CREATED, response_model=Person)
def create_person(person_name: str, db: Session = Depends(get_db)):
    """
    Create a new person
    """
    return PersonCRUD.create(db, person_name)
