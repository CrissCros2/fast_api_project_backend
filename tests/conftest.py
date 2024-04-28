import pytest
from fastapi.testclient import TestClient
from v0.main import app
from db import sessionmaker, get_db
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.ext.declarative import declarative_base


@pytest.fixture(scope="session")
def client():
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


def override_get_db():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = testing_session_local()
    base = declarative_base()
    base.metadata.create_all(bind=engine)
    try:
        yield db
    finally:
        db.close()
