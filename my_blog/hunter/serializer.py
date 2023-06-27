from rest_framework import serializers
from collections import defaultdict

from .models import Hunter, Archiving
from info.models import Skill, Description
from common.serializers import compact_create
from info.serializers import SkillMixin
from info.serializers import SkillSerializer, DescriptionSerializer
from dungeon.serializers import DungeonSerializer
from achievement.serializers import AchievementSerializer
from career.serializers import CareerSerializer


class ArchinvingSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True, required=False)

    class Meta:
        model = Archiving
        fields = ["category", "descriptions", "owner"]


class HunterSerializer(SkillMixin, serializers.ModelSerializer):
    archivings = ArchinvingSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, read_only=True)
    dungeons = DungeonSerializer(many=True, read_only=True)
    achievements = AchievementSerializer(many=True, read_only=True)
    careers = CareerSerializer(many=True, read_only=True)

    class Meta:
        model = Hunter
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "birth",
            "edu",
            "address",
            "skills",
            "archivings",
            "dungeons",
            "achievements",
            "careers",
        ]

    def add_skill(self, skill_obj):
        skill_serializer = SkillSerializer(data=skill_obj)
        skill_serializer.is_valid()
        skill_serializer.save()
        self.instance.skills.add(skill_serializer.instance)
        self.instance.refresh_from_db()

    def add_skills(self, skill_objs: list):
        skills = [Skill(**skill_obj) for skill_obj in skill_objs]
        Skill.objects.bulk_create(skills)
        self.instance.skills.add(*skills)

    def add_archiving(self, archiving_obj):
        data = {
            "owner": self.instance.id,
            "category": archiving_obj["category"],
        }
        description_serializer = compact_create(
            DescriptionSerializer, archiving_obj["description"]
        )
        archiving_serializer = compact_create(ArchinvingSerializer, data)
        archiving_serializer.instance.descriptions.add(description_serializer.instance)

        self.instance.refresh_from_db()
