from sqlalchemy.orm import Session
from abc import ABC
from uuid import UUID, uuid4
from db_models import PersonTable, EventTable


class CRUD(ABC):
    """
    Base class for all CRUD operations a different class is created for each table at runtime
    """

    @classmethod
    def create(cls, db: Session, row_to_add):
        raise NotImplementedError

    @classmethod
    def read_by_id(cls, db: Session, row_id: UUID):
        raise NotImplementedError

    @classmethod
    def update(cls, db: Session, row_id: UUID, column_to_update, new_value):
        pass
        # raise NotImplementedError

    @classmethod
    def delete_by_id(cls, db: Session, row_id: UUID):
        raise NotImplementedError


class PersonCRUD(CRUD):
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
        return db.query(PersonTable).filter(PersonTable.id == row_id).delete()
