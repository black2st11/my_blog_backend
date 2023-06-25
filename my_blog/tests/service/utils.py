from info.models import Description, Skill


def create_descriptions_and_skills(serializer):
    description_obj_in = [Description(**{"content": f"설명 {i}"}) for i in range(3)]

    skill_obj_in = [
        Skill(**{"category": "B", "name": skill})
        for skill in ["Django", "Flask", "Node"]
    ]

    Description.objects.bulk_create(description_obj_in)
    Skill.objects.bulk_create(skill_obj_in)

    serializer.instance.descriptions.add(*description_obj_in)
    serializer.instance.skills.add(*skill_obj_in)
