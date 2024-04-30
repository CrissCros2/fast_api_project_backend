from uuid import UUID, uuid4
from datetime import datetime

from sqlalchemy.orm import Session

from db_models import PersonTable, EventTable, EventPersonAssociation
from api_models import Person


class PersonCRUD:
    """
    Person CRUD operations
    """

    @classmethod
    def create(cls, db: Session, person_name: str):
        db_person = PersonTable(id=uuid4(), name=person_name)
        db.add(db_person)
        db.commit()
        db.refresh(db_person)
        return db_person

    @classmethod
    def read_by_id(cls, db: Session, row_id: UUID):
        # noinspection PyTypeChecker
        return db.query(PersonTable).filter(PersonTable.id == row_id).first()

    @classmethod
    def get_all_persons(cls, db: Session):
        return db.query(PersonTable).all()

    @classmethod
    def delete_by_id(cls, db: Session, row_id: UUID):
        # noinspection PyTypeChecker
        db_person = db.query(PersonTable).filter(PersonTable.id == row_id).first()
        if db_person:
            # noinspection PyTypeChecker
            db.query(PersonTable).filter(PersonTable.id == row_id).delete()
            return db_person
        return None


class EventCRUD:
    """
    Event CRUD operations
    """

    @classmethod
    def create_without_persons(
        cls, db: Session, event_id: UUID, title: str, desc: str, time: datetime
    ):
        db_event = EventTable(id=event_id, title=title, description=desc, time=time)
        db.add(db_event)
        db.commit()
        return db_event

    @classmethod
    def create_with_persons(
        cls, db: Session, title: str, desc: str, time: datetime, persons: list[Person]
    ):
        db_event = EventTable(id=uuid4(), title=title, description=desc, time=time)
        for person in persons:
            # noinspection PyTypeChecker
            new_person = (
                db.query(PersonTable).filter(PersonTable.id == person.id).first()
            )
            new_association = EventPersonAssociation(
                event_id=db_event.id, person_id=new_person.id
            )
            db.add(new_association)

        db.add(db_event)
        db.commit()
        return db_event

    @classmethod
    def read_by_id(cls, db: Session, row_id: UUID):
        # noinspection PyTypeChecker
        return db.query(EventTable).filter(EventTable.id == row_id).first()

    @classmethod
    def get_all_events(cls, db: Session):
        return db.query(EventTable).all()

    @classmethod
    def delete_by_id(cls, db: Session, row_id: UUID):
        # noinspection PyTypeChecker
        db_event = db.query(EventTable).filter(EventTable.id == row_id).first()
        if db_event:
            # noinspection PyTypeChecker
            db.query(EventTable).filter(EventTable.id == row_id).delete()
            return db_event
        return None
