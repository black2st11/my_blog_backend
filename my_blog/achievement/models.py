from django.db import models
from info.models import Skill, Description, File
from career.models import Career
from common.models import BaseModel


# Create your models here.
class Achievement(BaseModel):
    owner = models.ForeignKey(
        "me.Me",
        on_delete=models.CASCADE,
        related_name="achievements",
        verbose_name="모험가",
    )
    name = models.CharField("업적 명", max_length=100)
    start_date = models.DateField("시작날짜")
    end_date = models.DateField("종료날짜")
    position = models.CharField("직책", max_length=50)
    corp = models.ForeignKey(
        Career,
        on_delete=models.CASCADE,
        related_name="achievements",
        null=True,
        verbose_name="회사",
    )
    main_work = models.CharField("주요 업무", max_length=100, null=True)

    class Meta:
        verbose_name_plural = "업적"
        verbose_name = "업적"
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
