from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette import status

from api_models import Person
from crud import PersonCRUD
from db import get_db

persons = APIRouter()


@persons.get("/", response_model=list[Person])
async def get_persons(db: Session = Depends(get_db)):
    """
    Get all persons
    """
    return PersonCRUD.get_all_persons(db)


@persons.post("/", status_code=status.HTTP_201_CREATED, response_model=Person)
async def create_person(person_name: str, db: Session = Depends(get_db)):
    """
    Create a new person
    """
    return PersonCRUD.create(db, person_name)


@persons.get("/{person_id}")
async def get_person(person_id: UUID, db: Session = Depends(get_db)):
    """
    Get a person
    """
    db_person = PersonCRUD.read_by_id(db, person_id)
    if db_person:
        return db_person
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Person not found"},
    )


@persons.delete("/{person_id}")
async def delete_person(person_id: UUID, db: Session = Depends(get_db)):
    """
    Delete a person
    """
    db_person = PersonCRUD.delete_by_id(db, person_id)
    if db_person:
        return db_person
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Person not found"},
    )
