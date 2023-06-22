import pytest
from hunter.serializer import HunterSerializer
from hunter.models import Hunter
from info.models import Skill


@pytest.mark.django_db(transaction=True)
@pytest.fixture
def create_hunter():
    obj_in = {
        "name": "문정훈",
        "phone": "01086147257",
        "birth": "1995-05-16",
        "email": "black2st11@gmail.com",
        "edu": "학사",
        "address": "전남 순천시 도장길 50",
    }
    serializer = HunterSerializer(data=obj_in)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


@pytest.mark.django_db(transaction=True)
class TestHunter:
    def test_create_hunter(self):
        obj_in = {
            "name": "문정훈",
            "phone": "01086147257",
            "birth": "1995-05-16",
            "email": "black2st11@gmail.com",
            "edu": "학사",
            "address": "전남 순천시 도장길 50",
        }
        serializer = HunterSerializer(data=obj_in)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        assert serializer.instance
        for k, v in obj_in.items():
            assert serializer.data[k] == v
        assert len(serializer.data["skills"]) == 0

    def test_add_skill(self, create_hunter):
        hunter = Hunter.objects.get(id=create_hunter["id"])
        serializer = HunterSerializer(hunter)
        skill_obj = {"category": Skill.CategoryOfSkill.BACKEND, "name": "Django"}
        serializer.add_skill(skill_obj=skill_obj)
        assert serializer.instance.skills
        assert serializer.data
        print(serializer.data["skills"][0]["category"])
