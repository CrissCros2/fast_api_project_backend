import pytest
from fastapi.testclient import TestClient
from v0.main import app


@pytest.fixture(scope="session")
def client():
    return TestClient(app)
