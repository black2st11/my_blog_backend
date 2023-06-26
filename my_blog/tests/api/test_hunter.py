import pytest

from django.urls import reverse
from tests.service import create_hunter


@pytest.mark.django_db(transaction=True)
class TestClient:
    def test_get_hunters(self, create_hunter, client):
        url = reverse("hunter-list")
        request = client.get(url)
        assert request.status_code == 200
        assert len(request.data) == 1
        assert request.data[0]["id"] == create_hunter["id"]

    def test_get_hunter(self, create_hunter, client):
        url = reverse("hunter-detail", kwargs={"pk": create_hunter["id"]})
        request = client.get(url)
        assert request.status_code == 200
        assert request.data["id"] == create_hunter["id"]
        assert len(request.data["skills"]) == 0
