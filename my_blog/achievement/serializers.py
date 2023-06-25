from rest_framework import serializers

from .models import Achievement
from info.serializers import SkillSerializer, DescriptionSerializer, SkillMixin


class AchievementSerializer(SkillMixin, serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, required=False)

    class Meta:
        model = Achievement
        fields = [
            "owner",
            "name",
            "descriptions",
            "skills",
            "start_date",
            "end_date",
            "position",
            "main_work",
        ]
