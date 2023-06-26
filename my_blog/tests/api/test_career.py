import pytest

from django.urls import reverse


@pytest.mark.django_db(transaction=True)
class TestCareer:
    def test_get_careers(self, create_career_with_owner, client):
        url = reverse("career-list")
        response = client.get(url)
        assert response.status_code == 200
        assert response.data

    def test_get_career(self, create_career_with_owner, client):
        url = reverse("career-detail", kwargs={"pk": create_career_with_owner["id"]})
        response = client.get(url)
        assert response.status_code == 200
        assert response.data["id"] == create_career_with_owner["id"]
        assert len(response.data["skills"]["B"]) == 3
        assert len(response.data["descriptions"]) == 3
