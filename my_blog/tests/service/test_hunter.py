import pytest
from hunter.serializer import HunterSerializer
from hunter.models import Hunter


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

    def test_get_hunter(self, create_hunter):
        hunter = Hunter.objects.get(id=create_hunter["id"])
        assert hunter
