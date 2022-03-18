from .models import Career
from rest_framework import serializers

class CareerSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    skill = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    achievement = serializers.SerializerMethodField()

    class Meta :
        model = Career
        fields = ('name', 'description', 'skill','start_date', 'end_date', 'duration', 'position', 'work', 'achievement')

    def get_description(self, obj):
        desc_list = obj.desc_cabinet.all()
        return [desc.description.content for desc in desc_list]

    def get_skill(self, obj):
        skill_list = obj.skill_cabinet.all()
        return [{'category' : skill_cabinet.skill.category, 'name' : skill_cabinet.skill.name} for skill_cabinet in skill_list]

    def get_duration(self, obj):
        return obj.calc_duration()

    def get_achievement(self, obj):
        achievement = obj.achievements.all()[0]
        return {"id" : achievement.id, "name" : achievement.name}