from .models import Dungeon
from rest_framework import serializers

class DungeonSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    skill = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    class Meta :
        model = Dungeon
        fields = ('description', 'skill', 'name', 'duration', 'start_date', 'end_date', 'loc', 'size', 'impression')

    def get_description(self, obj):
        desc_list = obj.desc_cabinet.all()

        return [desc_cabinet.description.content for desc_cabinet in desc_list]
        
    def get_skill(self, obj):
        skill_list = obj.skill_cabinet.all()
        return [{'category' : skill_cabinet.skill.category, 'name' : skill_cabinet.skill.name} for skill_cabinet in skill_list]

    def get_duration(self, obj):
        return obj.calc_duration()