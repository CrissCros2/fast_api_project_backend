import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from uuid import uuid4, UUID

from db import get_db
from v0.main import app

from sqlalchemy import create_engine, Engine
from sqlalchemy.pool import StaticPool

from db import sessionmaker, Base
from db_models import PersonTable


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(scope="function")
def db_engine():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture(scope="function")
def db_session(db_engine: Engine):
    session = sessionmaker(bind=db_engine)
    test_session = session()
    yield test_session
    test_session.rollback()
    test_session.close()


@pytest.fixture(scope="function", autouse=True)
def add_person(db_session: Session):
    db_person1 = PersonTable(
        id=UUID("e1a0bcb9-6827-41bf-9888-fbed5dc9e9bb"), name="Person1"
    )
    db_person2 = PersonTable(
        id=UUID("cb6d5a97-d871-4bac-8fe8-a117ea3fd9de"), name="Person2"
    )
    db_session.add(db_person1)
    db_session.add(db_person2)
    db_session.commit()

    def get_session():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = get_session
