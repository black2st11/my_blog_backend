from django.db import models
from info.models import Skill, Description, Attach
from common.models import BaseModel

# Create your models here.


class Dungeon(BaseModel):
    class Difficulties(models.IntegerChoices):
        EASY = 1
        SOSO = 2
        NORMAL = 3
        HARD = 4
        HELL = 5

    owner = models.ForeignKey(
        "hunter.Hunter",
        on_delete=models.CASCADE,
        related_name="dungeons",
        verbose_name="모험가",
    )
    name = models.CharField("던전명", max_length=100, default="정의되지 않은 던전")
    start_date = models.DateField("진입날짜")
    end_date = models.DateField("클리어날짜")
    difficulty = models.IntegerField("난이도", choices=Difficulties.choices)
    size = models.CharField("인원", max_length=20)
    address = models.CharField("위치", max_length=50)
    impression = models.TextField("후기")
    descriptions = models.ManyToManyField(
        Description, related_name="dungeons", through="dungeon.DungeonDescription"
    )
    skills = models.ManyToManyField(
        Skill, related_name="dungeons", through="dungeon.DungeonSkill"
    )
    attachs = models.ManyToManyField(
        Attach, related_name="dungeons", through="dungeon.DungeonAttach"
    )

    class Meta:
        db_table = "dungeon"
        verbose_name = "던전"
        verbose_name_plural = "던전"

    def __str__(self):
        return self.name

    def calc_duration(self):
        days = (self.end_date - self.start_date).days

        if days < 28:
            return "1개월 미만"
        else:
            return f"{days//28}개월"


class DungeonDescription(BaseModel):
    dungeon = models.ForeignKey(Dungeon, on_delete=models.CASCADE)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)


class DungeonSkill(BaseModel):
    dungeon = models.ForeignKey(Dungeon, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class DungeonAttach(BaseModel):
    dungeon = models.ForeignKey(Dungeon, on_delete=models.CASCADE)
    attach = models.ForeignKey(Attach, on_delete=models.CASCADE)
