from abc import ABC, abstractmethod
from fastapi import status


class TestRoutes(ABC):
    """
    Base class for route testing so all methods get tested
    """
    not_allowed_responses = {status.HTTP_405_METHOD_NOT_ALLOWED,
                             status.HTTP_404_NOT_FOUND,
                             status.HTTP_406_NOT_ACCEPTABLE,
                             status.HTTP_401_UNAUTHORIZED,
                             status.HTTP_403_FORBIDDEN,
                             }

    @property
    @abstractmethod
    def route(self):
        raise NotImplementedError

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


class TestRoot(TestRoutes):
    """
    Test the "" route redirects to docs
    """

    route = ""

    def test_get(self, client):
        response = client.get(self.route)
        assert response.status_code is status.HTTP_301_MOVED_PERMANENTLY
        assert "/docs" in response.url

