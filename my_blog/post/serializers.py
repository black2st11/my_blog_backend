from rest_framework import serializers
from .models import Post
from info.serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ("id", "title", "tag", "file", "created_at", "updated_at")
