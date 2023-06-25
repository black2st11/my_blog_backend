import pytest

from .utils import create_descriptions_and_skills
from .test_hunter import create_hunter
from common.serializers import compact_create
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
