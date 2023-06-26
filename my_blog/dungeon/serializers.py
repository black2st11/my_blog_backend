from rest_framework import serializers

from .models import Dungeon
from info.serializers import DescriptionSerializer, SkillSerializer, SkillMixin
from common.serializers import EndDateValidationMixin


class DungeonSerializer(
    EndDateValidationMixin, SkillMixin, serializers.ModelSerializer
):
    descriptions = DescriptionSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, required=False)
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Dungeon
        fields = (
            "id",
            "owner",
            "descriptions",
            "skills",
            "name",
            "difficulty",
            "duration",
            "start_date",
            "end_date",
            "address",
            "size",
            "impression",
        )

    def get_duration(self, obj):
        return obj.calc_duration()
