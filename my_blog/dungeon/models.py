from django.db import models
from info.models import Skill, Description
# Create your models here.

class Dungeon(models.Model):
    class Difficulties(models.IntegerChoices):
        EASY = 1
        SOSO = 2
        NORMAL = 3
        HARD = 4
        HELL = 5

    name = models.CharField(max_length=100, default='정의되지 않은 던전')
    start_date = models.DateField()
    end_date = models.DateField()
    difficulty = models.IntegerField(choices=Difficulties.choices)
    size = models.CharField(max_length=20)
    loc = models.CharField(max_length=50)
    impression = models.TextField()

    class Meta:
        db_table = u'dungeon'

    def __str__(self):
        return self.name

    def calc_duration(self):
        days = (self.end_date - self.start_date).days

        if days < 28 :
            return '1개월 미만'
        else :
            return f'{days//28}개월'

class DungeonDescription(models.Model):
    dungeon = models.ForeignKey(Dungeon, on_delete=models.CASCADE, related_name='desc_cabinet')
    description = models.ForeignKey(Description, on_delete=models.CASCADE)

    class Meta:
        db_table = u'dungeon_desc'

class DungeonSkill(models.Model):
    dungeon = models.ForeignKey(Dungeon, on_delete=models.DO_NOTHING, related_name='skill_cabinet')
    skill = models.ForeignKey(Skill, on_delete=models.DO_NOTHING)

    class Meta :
        db_table = u'dungeon_skill'