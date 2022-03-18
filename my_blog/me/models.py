from datetime import datetime
from django.db import models
from info.models import Skill, Description
from django.utils.timezone import now
# Create your models here.

class Me(models.Model):
    name = models.CharField(default='', max_length=30)
    phone = models.CharField(default='00000000000', max_length=12 )
    birth = models.DateField(default=now)
    email = models.EmailField()
    edu = models.CharField(default='' ,max_length=100)
    loc = models.CharField(default='', max_length=100)

    class Meta:
        db_table = u'me'

    def __str__(self):
        return self.name

class MySkill(models.Model):
    me = models.ForeignKey(Me, on_delete=models.DO_NOTHING, related_name='my_skill')
    skill = models.ForeignKey(Skill, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = u'my_skill'
    
class Archiving(models.Model):
    category = models.CharField(max_length=20)

    class Meta :
        db_table = u'archiving'

    def __str__(self):
        return self.category


class MyDesc(models.Model):
    me = models.ForeignKey(Me,on_delete=models.DO_NOTHING, related_name='desc_cabinet', related_query_name='desc_cabinets')
    description = models.ForeignKey(Description, on_delete=models.DO_NOTHING, related_name='descs')

    class Meta :
        db_table = u'my_desc'


class ArchDesc(models.Model):
    archiving = models.ForeignKey(Archiving, on_delete=models.DO_NOTHING, related_name='desc_cabinet')
    description = models.ForeignKey(Description, on_delete=models.DO_NOTHING)

    class Meta :
        db_table = u'arch_desc'