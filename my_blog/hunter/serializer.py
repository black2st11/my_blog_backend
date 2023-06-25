from rest_framework import serializers
from collections import defaultdict

from .models import Hunter, Archiving
from info.models import Skill, Description
from common.serializers import compact_create
from info.serializers import SkillMixin
from info.serializers import SkillSerializer, DescriptionSerializer


class ArchinvingSerializer(serializers.ModelSerializer):
    descriptions = DescriptionSerializer(many=True, required=False)

    class Meta:
        model = Archiving
        fields = ["category", "descriptions", "owner"]


class HunterSerializer(SkillMixin, serializers.ModelSerializer):
    archivings = ArchinvingSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, read_only=True)

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
        ]

    # archiving description 은 여기에서만 사용하기에 Mixin으로 하지않음(추후 늘어날 경우 변경)
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        archiving_set = defaultdict(list)
        for archiving in ret.get("archivings", []):
            archiving_set[archiving["category"]].append(
                {
                    "content": description["content"]
                    for description in archiving["descriptions"]
                }
            )
        ret["archivings"] = archiving_set
        return ret

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
