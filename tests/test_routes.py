from abc import ABC
from datetime import datetime
from uuid import uuid4, UUID

from fastapi import status

from api_models import Person, Event


class RoutesTest(ABC):
    """
    Base class for route testing so all methods get tested
    """

    not_allowed_responses = {
        status.HTTP_405_METHOD_NOT_ALLOWED,
        status.HTTP_404_NOT_FOUND,
        status.HTTP_406_NOT_ACCEPTABLE,
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_403_FORBIDDEN,
        status.HTTP_422_UNPROCESSABLE_ENTITY,
    }

    route: str = NotImplemented

    def test_get(self, client):
        response = client.get(self.route)
        assert response.status_code in self.not_allowed_responses

    def test_post(self, client):
        response = client.post(self.route)
        assert response.status_code in self.not_allowed_responses

    def test_put(self, client):
        response = client.put(self.route)
        assert response.status_code in self.not_allowed_responses

    def test_delete(self, client):
        response = client.delete(self.route)
        assert response.status_code in self.not_allowed_responses

    def test_patch(self, client):
        response = client.patch(self.route)
        assert response.status_code in self.not_allowed_responses


class TestRoot(RoutesTest):
    """
    Test the "/" route redirects to docs
    """

    route = "/"

    def test_get(self, client):
        response = client.get(self.route)
        assert response.status_code is status.HTTP_200_OK
        assert "/docs" in str(response.url)


class TestPersonsRoot(RoutesTest):
    """
    Test the "/persons/" rout
    """

    route = "/persons/"

    def test_get(self, client):
        response = client.get(self.route)
        assert response.status_code is status.HTTP_200_OK
        assert response.json()

    def test_post(self, client):
        data = {"name": "blah"}
        response = client.post(f"{self.route}?person_name=chris", json=data)
        assert response.json()
        assert response.status_code is status.HTTP_201_CREATED


class TestEventsRoot(RoutesTest):
    """
    Test the "/events/" route
    """

    route = "/events/"

    def test_get(self, client):
        response = client.get(self.route)
        assert response.json()
        assert response.status_code is status.HTTP_200_OK


class TestCreateEventWithoutPersons(RoutesTest):
    route = "/events/create_no_persons"

    def test_post(self, client):
        data = {
            "id": uuid4().hex,
            "title": "blah",
            "description": "blah",
            "time": str(datetime.now()),
        }
        response = client.post(self.route, json=data)
        assert response.status_code is status.HTTP_201_CREATED
        event = Event(**response.json())
        assert event.id == UUID(data["id"])
        assert event.title == data["title"]
        assert event.description == data["description"]
        assert str(event.time) == data["time"]
        assert event.attendees == []


class TestEventsByID(RoutesTest):
    """
    Test the "/events/{event_id} route
    """

    route = f"/events/{uuid4()}"

    def test_get(self, client):
        response = client.get(self.route)
        assert response.status_code is status.HTTP_200_OK
        assert response.json()

    def test_put(self, client):
        data = {
            "id": uuid4().hex,
            "title": "blah",
            "description": "blah",
            "time": str(datetime.now()),
            "attendees": [],
        }
        response = client.put(self.route, json=data)
        assert response.status_code is status.HTTP_200_OK

    def test_delete(self, client):
        response = client.delete(self.route)
        assert response.status_code is status.HTTP_200_OK


class TestCancelEvent(RoutesTest):
    """
    Test "/events/{event_id}/cancel" route
    """

    route = f"/events/{uuid4()}/cancel"

    def test_patch(self, client):
        response = client.patch(self.route)
        assert response.status_code is status.HTTP_200_OK


class TestPersonByIDExists(RoutesTest):

    route = "/persons/e1a0bcb9-6827-41bf-9888-fbed5dc9e9bb"

    def test_get(self, client):
        response = client.get(self.route)
        assert response.status_code is status.HTTP_200_OK
        person = Person(**response.json())
        assert person.name == "Person1"
        assert person.id == UUID("e1a0bcb9-6827-41bf-9888-fbed5dc9e9bb")

    def test_delete(self, client):
        response = client.delete(self.route)
        assert response.status_code is status.HTTP_200_OK
        person = Person(**response.json())
        assert person.name == "Person1"
        assert person.id == UUID("e1a0bcb9-6827-41bf-9888-fbed5dc9e9bb")


class TestPersonByIDNotExists(RoutesTest):
    route = f"/persons/{uuid4()}"

    def test_get(self, client):
        response = client.get(self.route)
        assert response.status_code is status.HTTP_404_NOT_FOUND

    def test_delete(self, client):
        response = client.delete(self.route)
        assert response.status_code is status.HTTP_404_NOT_FOUND
