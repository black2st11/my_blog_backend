from django.db import models

# Create your models here.

SKILL_CATEGORY_CHOICES =[()]

class Skill(models.Model):
    class CategoryOfSkill(models.TextChoices):
        BACKEND = 'B', ('BackEnd')
        FRONTEND = 'F' , ("FrontEnd")
        DEVOPS = "D", ('DevOps')
        INFRA = 'I', ('Infra')
        COMMUNICATION = 'C' , ("Communication")
        LANGUAGE = 'L' , ("Language")
        UNKNOWN = 'U', ("Unknown")

    category = models.CharField(max_length=1, choices=CategoryOfSkill.choices, default=CategoryOfSkill.UNKNOWN)
    name = models.CharField(max_length=20, default='Unknown Skill')

    def __str__(self):
        return self.name

    class Meta :
        db_table = u'skill'

class Description(models.Model):
    content = models.TextField()
    
    class Meta :
        db_table = u'description'

    def __str__(self):
        return self.content[:15] + '...'

class Tag(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = u'tag'
    
    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255)