from django.db import models
from info.models import Skill, Description, File
from career.models import Career
from common.models import BaseModel


# Create your models here.
class Achievement(BaseModel):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    position = models.CharField(max_length=50)
    corp = models.ForeignKey(
        Career, on_delete=models.CASCADE, related_name="achievements", null=True
    )
    main_work = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "achievement"

    def __str__(self):
        return self.name


class AchieveDescription(BaseModel):
    achievement = models.ForeignKey(
        Achievement, on_delete=models.DO_NOTHING, related_name="desc_cabinet"
    )
    description = models.ForeignKey(Description, on_delete=models.CASCADE)

    class Meta:
        db_table = "achievement_desc"


class AchieveSkill(BaseModel):
    achievement = models.ForeignKey(
        Achievement, on_delete=models.DO_NOTHING, related_name="skill_cabinet"
    )
    skill = models.ForeignKey(Skill, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "achievement_skill"


class AchieveFile(BaseModel):
    achievement = models.ForeignKey(
        Achievement, on_delete=models.DO_NOTHING, related_name="file_cabinet"
    )
    file = models.ForeignKey(File, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "achievement_file"
