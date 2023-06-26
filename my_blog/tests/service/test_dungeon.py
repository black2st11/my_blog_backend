import pytest
from rest_framework.serializers import ValidationError

from .utils import create_descriptions_and_skills
from .test_hunter import create_hunter
from common.serializers import compact_create, START_DATE_EXCEED_END_DATE
from dungeon.models import Dungeon
from dungeon.serializers import DungeonSerializer


@pytest.mark.django_db(transaction=True)
class TestDungeon:
    # TODO: end_date가 start_date 보다 뒤에 있으면 안되는 검증 로직이 필요
    def test_create_dungeon(self, create_hunter):
        dungeon_obj_in = {
            "owner": create_hunter["id"],
            "name": "테스트 던전",
            "start_date": "2020-01-01",
            "end_date": "2020-12-12",
            "difficulty": Dungeon.Difficulties.HELL,
            "size": "5~10",
            "address": "순천",
            "impression": "매우 어렵구나",
        }
        serializer = compact_create(DungeonSerializer, dungeon_obj_in)

        create_descriptions_and_skills(serializer)

        assert serializer.instance
        assert len(serializer.data["skills"])
        assert len(serializer.data["descriptions"])

    def test_create_dungeond_exceed_end_date(self, create_hunter):
        dungeon_obj_in = {
            "owner": create_hunter["id"],
            "name": "테스트 던전",
            "start_date": "2020-01-01",
            "end_date": "2019-12-12",
            "difficulty": Dungeon.Difficulties.HELL,
            "size": "5~10",
            "address": "순천",
            "impression": "매우 어렵구나",
        }

        serializer = DungeonSerializer(data=dungeon_obj_in)

        with pytest.raises(ValidationError) as error:
            serializer.is_valid(raise_exception=True)
            serializer.save()

        assert error.value.detail["end_date"][0] == START_DATE_EXCEED_END_DATE
