from rest_framework import serializers
from .models import Me, Archiving


class MeSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    skill = serializers.SerializerMethodField()
    info = serializers.SerializerMethodField()

    class Meta :
        model = Me
        fields = ['description', 'name', 'phone', 'birth', 'skill','info']

    def get_description(self, obj):
        desc = obj.desc_cabinet.select_related('description', 'me').all()
        array = [me_desc.description.content for me_desc in desc]
        return array

    def get_skill(self, obj):
        skills = obj.my_skill.select_related('skill').all()
        category = {
            'B' : 1,
            'F' : 2,
            "L" : 0,
            "I" : 3,
            "D" : 4,
            "U" : 5
        }

        result = [{
            "category" : '언어',
            "value" : []
        },{
            "category" : '백엔드',
            "value" : []
        },{
            "category" : '프론트',
            "value" : []
        },
        {
            "category" : '인프라',
            "value" : []
        },
        {
            "category" : '데브옵스',
            "value" : []
        },{
            "category" : '기타',
            "value" : []
        },
        ]
        for skill in skills:
            result[category[skill.skill.category]]['value'].append(skill.skill.name)
        return result

    def get_info(self, obj):
        return [
            {"category" : '이름', "value" : obj.name}, 
            {"category" : '나이' , "value" : obj.birth }, 
            {"category" : "직업", "value" : '풀스택 개발자'}, 
            {"category" : "선호", "value" : ['백엔드', '인프라']}, 
            {"category" : '학력', "value" : obj.edu},
            {'category' : '사는 곳' , "value" : obj.loc}
        ]

class ArchinvingSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Archiving
        fields = ('category', 'description')

    def get_description(self, obj):
        desc_list = obj.desc_cabinet.all()
        return [desc_cabinet.description.content for desc_cabinet in desc_list]