import pytest
from django.urls import reverse


@pytest.mark.django_db(transaction=True)
class TestClient:
    def test_get_hunters(self, create_hunter, client):
        url = reverse("hunter-list")
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["id"] == create_hunter["id"]

    def test_get_hunter(self, create_hunter, client):
        url = reverse("hunter-detail", kwargs={"pk": create_hunter["id"]})
        response = client.get(url)
        assert response.status_code == 200
        assert response.data["id"] == create_hunter["id"]
        assert len(response.data["skills"]) == 0
