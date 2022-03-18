from rest_framework import serializers
from .models import Achievement

class AchievementSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    skill = serializers.SerializerMethodField()
    file = serializers.SerializerMethodField()
    
    class Meta :
        model = Achievement
        fields = ('name', 'description', 'skill', 'file', 'start_date', 'end_date', 'position', 'main_work')

    def get_description(self, obj):
        desc_list = obj.desc_cabinet.all()
        return [desc.description.content for desc in desc_list]

    def get_skill(self, obj):
        skill_list = obj.skill_cabinet.all()
        return [{'category' : skill_cabinet.skill.category, 'name' : skill_cabinet.skill.name} for skill_cabinet in skill_list]

    def get_file(self, obj):
        file_list = obj.file_cabinet.all()
        return [{'name' : file_cabinet.file.name, "address" : file_cabinet.file.name} for file_cabinet in file_list]