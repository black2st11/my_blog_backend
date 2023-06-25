import pytest
from achievement.serializers import AchievementSerializer
from achievement.models import Achievement
from info.models import Description, Skill
from .test_hunter import create_hunter, Hunter
from common.serializers import compact_create


@pytest.mark.django_db(transaction=True)
class TestAchievement:
    # TODO: end_date가 start_date 보다 뒤에 있으면 안되는 검증 로직이 필요
    def test_create_achievement(self, create_hunter):
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
        achievement_serializer = compact_create(
            AchievementSerializer, achievement_obj_in
        )

        Description.objects.bulk_create(description_obj_in)
        Skill.objects.bulk_create(skill_obj_in)

        achievement_serializer.instance.descriptions.add(*description_obj_in)
        achievement_serializer.instance.skills.add(*skill_obj_in)

        assert achievement_serializer.instance
        assert len(achievement_serializer.instance.descriptions.all()) == 3
        assert len(achievement_serializer.instance.skills.all()) == 3
