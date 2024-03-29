from rest_framework import serializers

from .models import Achievement
from info.serializers import (
    SkillSerializer,
    DescriptionSerializer,
    AttachSerializer,
    SkillMixin,
)
from common.serializers import EndDateValidationMixin


class AchievementSerializer(
    EndDateValidationMixin, SkillMixin, serializers.ModelSerializer
):
    descriptions = DescriptionSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, required=False)
    attachs = AttachSerializer(many=True, required=False)

    class Meta:
        model = Achievement
        fields = [
            "id",
            "owner",
            "name",
            "start_date",
            "end_date",
            "position",
            "main_work",
            "descriptions",
            "skills",
            "attachs",
        ]
