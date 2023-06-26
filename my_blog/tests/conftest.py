import pytest
from rest_framework.serializers import Serializer


from hunter.serializer import HunterSerializer
from common.serializers import compact_create
from achievement.serializers import AchievementSerializer
from career.serializers import CareerSerializer
from dungeon.models import Dungeon
from dungeon.serializers import DungeonSerializer
from post.models import Post
from post.serializers import PostSerializer
from info.models import Tag
from qna.models import Question
from tests.service.utils import create_descriptions_and_skills


def generate_serializer_with_owner(serializer_obj: Serializer, obj_in: dict):
    serializer = compact_create(serializer_obj, obj_in)
    create_descriptions_and_skills(serializer)

    return {
        "id": serializer.instance.id,
        "owner": serializer.instance.owner,
    }


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

    return generate_serializer_with_owner(AchievementSerializer, achievement_obj_in)


@pytest.fixture
def create_career_with_owner(create_hunter):
    career_obj_in = {
        "owner": create_hunter["id"],
        "name": "매그너스 길드",
        "position": "선임",
        "work": "풀스택",
        "start_date": "2023-12-01",
        "end_date": "2023-12-30",
    }

    return generate_serializer_with_owner(CareerSerializer, career_obj_in)


@pytest.fixture
def create_dungeon_with_owner(create_hunter):
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

    return generate_serializer_with_owner(DungeonSerializer, dungeon_obj_in)


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def create_post():
    post = Post.objects.create(title="테스트 포스트 타이틀")
    tags = [Tag(name=f"{i} tag") for i in range(3)]
    Tag.objects.bulk_create(tags)
    post.tags.add(*tags)
    serializer = PostSerializer(post)
    return {"id": serializer.instance.id}


@pytest.fixture
@pytest.mark.django_db(transaction=True)
def creaet_question():
    questions = [Question(**{"content": f"{i}번째 질문"}) for i in range(10)]
    Question.objects.bulk_create(questions)
    return {"data": questions}
