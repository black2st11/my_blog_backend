import pytest

from hunter.serializer import HunterSerializer
from info.models import Description, Skill
from common.serializers import compact_create
from achievement.serializers import AchievementSerializer


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


@pytest.fixture
def create_achievement_with_hunter(create_hunter):
    achievement_obj_in = {
        "owner": create_hunter["id"],
        "name": "신기한 업적명",
        "start_date": "2023-01-01",
        "end_date": "2023-12-12",
        "position": "신기한 직책",
        "main_work": "신기한 주요업무",
    }

    description_obj_in = [Description(**{"content": f"설명 {i}"}) for i in range(3)]

    skill_obj_in = [
        Skill(**{"category": "B", "name": skill})
        for skill in ["Django", "Flask", "Node"]
    ]
    achievement_serializer = compact_create(AchievementSerializer, achievement_obj_in)

    Description.objects.bulk_create(description_obj_in)
    Skill.objects.bulk_create(skill_obj_in)

    achievement_serializer.instance.descriptions.add(*description_obj_in)
    achievement_serializer.instance.skills.add(*skill_obj_in)

    return {
        "id": achievement_serializer.instance.id,
        "owner": achievement_serializer.instance.owner,
    }
