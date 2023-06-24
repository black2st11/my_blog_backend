from rest_framework.serializers import ModelSerializer, BaseSerializer
from collections import defaultdict

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


class SkillMixin(BaseSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        skill_set = defaultdict(list)
        for skill in ret.get("skills", []):
            skill_set[skill["category"]].append({"name": skill["name"]})
        ret["skills"] = skill_set
        return ret
