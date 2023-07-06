from rest_framework import serializers
from django_quill.quill import QuillParseError

from .models import Post
from info.serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    content = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", "content", "title", "tags", "attach", "created", "updated")

    def get_content(self, instance):
        try:
            return str(instance.content.html)
        except QuillParseError:
            return "해당 게시글은 Quill을 이용해 작성된 게시물이 아닙니다."
