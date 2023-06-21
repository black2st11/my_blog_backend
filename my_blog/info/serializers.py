from rest_framework.serializers import ModelSerializer
from .models import Tag, Description, Skill


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class DescriptionSerializer(ModelSerializer):
    class Meta:
        model = Description
        fields = ["content"]


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = ["category", "name"]
