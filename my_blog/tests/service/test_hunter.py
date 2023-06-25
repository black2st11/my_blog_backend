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
        skill_obj = {"category": Skill.CategoryOfSkill.FRONTEND, "name": "React"}
        serializer.add_skill(skill_obj=skill_obj)
        assert len(serializer.instance.skills.all()) == 2
        assert serializer.data.get("skills")["B"]
        assert serializer.data.get("skills")["F"]

    def test_add_archiving(self, create_hunter):
        hunter = Hunter.objects.get(id=create_hunter["id"])
        serializer = HunterSerializer(hunter)

        archiving_obj = {
            "category": "백엔드",
            "owner_id": hunter.id,
            "description": {"content": "매우 뛰어난 백엔드 실력"},
        }

        archiving_obj_1 = {
            "category": "프론트엔드",
            "owner_id": hunter.id,
            "description": {"content": "매우 뛰어난 프론트엔드 실력"},
        }

        serializer.add_archiving(archiving_obj=archiving_obj)
        serializer.add_archiving(archiving_obj=archiving_obj_1)

        assert len(serializer.instance.archivings.all()) == 2
        assert serializer.data.get("archivings")["백엔드"]
        assert serializer.data.get("archivings")["프론트엔드"]

    def test_add_skills(self, create_hunter):
        hunter = Hunter.objects.get(id=create_hunter["id"])
        serializer = HunterSerializer(hunter)
        skill_objs = [
            {"category": Skill.CategoryOfSkill.BACKEND, "name": "Django"},
            {"category": Skill.CategoryOfSkill.FRONTEND, "name": "React"},
        ]
        serializer.add_skills(skill_objs)
        assert len(serializer.data.get("skills")["B"]) == 1
        assert len(serializer.data.get("skills")["F"]) == 1
        assert serializer.data.get("skills")["B"][0]["name"] == "Django"
