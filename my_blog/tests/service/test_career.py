import pytest
from rest_framework.serializers import ValidationError

from career.serializers import CareerSerializer
from info.models import Description, Skill
from .test_hunter import create_hunter, Hunter
from common.serializers import compact_create, START_DATE_EXCEED_END_DATE


@pytest.mark.django_db(transaction=True)
class TestCareer:
    # TODO: end_date가 start_date 보다 뒤에 있으면 안되는 검증 로직이 필요
    def test_create_career(self, create_hunter):
        career_obj_in = {
            "owner": create_hunter["id"],
            "name": "매그너스 길드",
            "position": "선임",
            "work": "풀스택",
            "start_date": "2023-12-01",
            "end_date": "2023-12-30",
        }

        description_obj_in = [Description(**{"content": f"설명 {i}"}) for i in range(3)]

        skill_obj_in = [
            Skill(**{"category": "B", "name": skill})
            for skill in ["Django", "Flask", "Node"]
        ]

        career_serializer = compact_create(CareerSerializer, career_obj_in)

        Description.objects.bulk_create(description_obj_in)
        Skill.objects.bulk_create(skill_obj_in)

        career_serializer.instance.descriptions.add(*description_obj_in)
        career_serializer.instance.skills.add(*skill_obj_in)

        assert career_serializer.instance
        assert len(career_serializer.instance.descriptions.all()) == 3
        assert len(career_serializer.instance.skills.all()) == 3

    def test_create_career_exceed_end_date(self, create_hunter):
        career_obj_in = {
            "owner": create_hunter["id"],
            "name": "매그너스 길드",
            "position": "선임",
            "work": "풀스택",
            "start_date": "2023-12-01",
            "end_date": "2023-11-30",
        }

        with pytest.raises(ValidationError) as error:
            serializer = CareerSerializer(data=career_obj_in)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        assert error.value.detail["end_date"][0] == START_DATE_EXCEED_END_DATE
