from rest_framework import serializers
from .models import Post
from info.serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ("id", "content", "title", "tags", "attach", "created", "updated")
