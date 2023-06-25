from .models import Career
from rest_framework import serializers
from info.serializers import DescriptionSerializer, SkillSerializer


class CareerSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, required=False)
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Career
        fields = (
            "owner",
            "name",
            "descriptions",
            "skills",
            "start_date",
            "end_date",
            "duration",
            "position",
            "work",
        )

    def get_duration(self, obj):
        return obj.calc_duration()
