from rest_framework import serializers

from .models import Achievement, AchieveDescription, AchieveSkill
from info.serializers import DescriptionSerializer, SkillSerializer


class AchievementDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchieveDescription
        fields = ["achievement", "description"]


class AchievementSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = AchieveSkill
        fields = ["skill"]


class AchievementSerializer(serializers.ModelSerializer):
    desc_cabinet = AchievementDescriptionSerializer(many=True)
    skill_cabinet = AchievementSkillSerializer(many=True)
    file = serializers.SerializerMethodField()

    class Meta:
        model = Achievement
        fields = (
            "name",
            "desc_cabinet",
            "skill_cabinet",
            "file",
            "start_date",
            "end_date",
            "position",
            "main_work",
        )

    def get_skill(self, obj):
        skill_list = obj.skill_cabinet.all()
        return [
            {"category": skill_cabinet.skill.category, "name": skill_cabinet.skill.name}
            for skill_cabinet in skill_list
        ]

    def get_file(self, obj):
        file_list = obj.file_cabinet.all()
        return [
            {"name": file_cabinet.file.name, "address": file_cabinet.file.name}
            for file_cabinet in file_list
        ]
