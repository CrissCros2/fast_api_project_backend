import pytest
from fastapi.testclient import TestClient
from v0.main import app
from db import sessionmaker, get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from uuid import uuid4


@pytest.fixture(scope="session")
def client():
    app.dependency_overrides[get_db] = init_database
    return TestClient(app)


def init_database():
    from db_models import EventTable, PersonTable
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = testing_session_local()
    Base.metadata.create_all(bind=engine)
    db.add(PersonTable(id=uuid4(), name="Chris"))
    db.commit()
    try:
        yield db
    finally:
        db.close()
