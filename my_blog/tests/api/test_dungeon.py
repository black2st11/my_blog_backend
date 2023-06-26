import pytest

from django.urls import reverse


@pytest.mark.django_db(transaction=True)
class TestDungeon:
    def test_get_dungeons(self, create_dungeon_with_owner, client):
        url = reverse("dungeon-list")
        response = client.get(url)

        assert response.status_code == 200
        assert response.data

    def test_get_dungeon(self, create_dungeon_with_owner, client):
        url = reverse("dungeon-detail", kwargs={"pk": create_dungeon_with_owner["id"]})
        response = client.get(url)

        assert response.status_code == 200
        assert response.data["id"] == create_dungeon_with_owner["id"]
        assert len(response.data["skills"]["B"]) == 3
