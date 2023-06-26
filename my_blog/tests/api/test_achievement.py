import pytest
from django.urls import reverse


@pytest.mark.django_db(transaction=True)
class TestAchievement:
    def test_get_achievements(self, create_achievement_with_hunter, client):
        url = reverse("achievement-list")
        response = client.get(url)

        assert response.status_code == 200
        assert response.data

    def test_get_achievement(self, create_achievement_with_hunter, client):
        url = reverse(
            "achievement-detail", kwargs={"pk": create_achievement_with_hunter["id"]}
        )
        response = client.get(url)
        assert response.status_code == 200
        assert response.data["id"] == create_achievement_with_hunter["id"]
        assert len(response.data["skills"]["B"]) == 3
        assert len(response.data["descriptions"]) == 3
