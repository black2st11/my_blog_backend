from django.db import models
from info.models import Skill, Description, Attach
from career.models import Career
from common.models import BaseModel


# Create your models here.
class Achievement(BaseModel):
    owner = models.ForeignKey(
        "hunter.Hunter",
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
    descriptions = models.ManyToManyField(
        "info.Description",
        related_name="achievements",
        through="achievement.AchieveDescription",
    )
    skills = models.ManyToManyField(
        "info.Skill", related_name="achievements", through="achievement.AchieveSkill"
    )
    attachs = models.ManyToManyField(
        "info.Attach", related_name="achievements", through="achievement.AchieveAttach"
    )

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "업적"
        verbose_name = "업적"
        db_table = "achievement"

    def __str__(self):
        return self.name


class AchieveDescription(BaseModel):
    achievement = models.ForeignKey(Achievement, on_delete=models.DO_NOTHING)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)


class AchieveSkill(BaseModel):
    achievement = models.ForeignKey(Achievement, on_delete=models.DO_NOTHING)
    skill = models.ForeignKey(Skill, on_delete=models.DO_NOTHING)


class AchieveAttach(BaseModel):
    achievement = models.ForeignKey(Achievement, on_delete=models.DO_NOTHING)
    file = models.ForeignKey(Attach, on_delete=models.DO_NOTHING)
