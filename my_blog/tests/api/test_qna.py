import pytest

from django.urls import reverse


@pytest.mark.django_db(transaction=True)
class TestQna:
    def test_create_question(self, client):
        obj_in = {"content": "첫번째 질문"}
        url = reverse("question-list")
        response = client.post(url, data=obj_in)

        assert response.status_code == 201
        assert response.data
        assert response.data["content"] == obj_in["content"]
        assert response.data["id"]
        assert response.data["ip"]

    def test_get_questions(self, creaet_question, client):
        url = reverse("question-list")
        response = client.get(url)
        assert response.status_code == 200
        assert response.data
        assert len(response.data) == 10

    def test_get_question(self, creaet_question, client):
        first_question_id = creaet_question["data"][0].id
        url = reverse("question-detail", kwargs={"pk": first_question_id})
        response = client.get(url)
        assert response.status_code == 200
        assert response.data
        assert response.data["id"] == first_question_id
