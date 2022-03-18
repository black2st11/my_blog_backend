from django.db import models
from info.models import Description, Skill

# Create your models here.
class Career(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    work = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    
    class Meta :
        db_table = u'career'

    def __str__(self):
        return self.name

    def calc_duration(self):
        days = (self.end_date - self.start_date).days

        if days < 28 :
            return 0
        else :
            return days//28

class CareerDescription(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='desc_cabinet')
    description = models.ForeignKey(Description, on_delete=models.CASCADE)

    class Meta :
        db_table = u'career_desc'

class CareerSkill(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='skill_cabinet')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta :
        db_table = u'career_skill'