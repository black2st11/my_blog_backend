import pytest

from post.serializers import PostSerializer
from info.models import Tag
from common.serializers import compact_create


@pytest.mark.django_db(transaction=True)
class TestPost:
    def test_create_post(self):
        post_obj_in = {"title": "테스트 글"}
        tag_obj_in = [Tag(**{"name": f"tag {i}"}) for i in range(3)]

        serializer = compact_create(PostSerializer, post_obj_in)
        Tag.objects.bulk_create(tag_obj_in)
        serializer.instance.tags.add(*tag_obj_in)

        assert serializer.instance
        assert len(serializer.data["tags"]) == 3
