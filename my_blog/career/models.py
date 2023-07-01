from django.db import models
import datetime

from info.models import Description, Skill, Attach
from common.models import BaseModel


# Create your models here.
class Career(BaseModel):
    owner = models.ForeignKey(
        "hunter.Hunter",
        on_delete=models.CASCADE,
        related_name="careers",
        verbose_name="모험가",
    )
    name = models.CharField("길드명", max_length=50)
    position = models.CharField("직책", max_length=50)
    work = models.CharField("맡은 일", max_length=50)
    start_date = models.DateField("시작날짜")
    end_date = models.DateField("종료날짜", null=True, blank=True)
    descriptions = models.ManyToManyField(
        Description, related_name="careers", through="career.CareerDescription"
    )
    skills = models.ManyToManyField(
        Skill, related_name="careers", through="career.CareerSkill"
    )
    attachs = models.ManyToManyField(
        Attach, related_name="careers", through="career.CareerAttach"
    )

    class Meta:
        ordering = ["-id"]
        db_table = "career"
        verbose_name = "길드"
        verbose_name_plural = "길드"

    def __str__(self):
        return self.name

    def calc_duration(self):
        end_date = self.end_date
        if not end_date:
            end_date = datetime.date.today()
        days = (end_date - self.start_date).days

        if days < 28:
            return 0
        else:
            return days // 28


class CareerDescription(BaseModel):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)


class CareerSkill(BaseModel):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class CareerAttach(BaseModel):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    attach = models.ForeignKey(Attach, on_delete=models.CASCADE)
