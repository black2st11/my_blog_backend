import pytest

from django.urls import reverse


@pytest.mark.django_db(transaction=True)
class TestPost:
    def test_get_posts(self, create_post, client):
        url = reverse("post-list")
        response = client.get(url)
        assert response.status_code == 200
        assert response.data

    def test_get_post(self, create_post, client):
        url = reverse("post-detail", kwargs={"pk": create_post["id"]})
        response = client.get(url)
        assert response.status_code == 200
        assert response.data["id"] == create_post["id"]
        assert len(response.data["tags"]) == 3
