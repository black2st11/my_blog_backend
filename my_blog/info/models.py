from django.db import models
from common.models import BaseModel

# Create your models here.

SKILL_CATEGORY_CHOICES = [()]


class Skill(BaseModel):
    class CategoryOfSkill(models.TextChoices):
        BACKEND = "B", ("BackEnd")
        FRONTEND = "F", ("FrontEnd")
        DEVOPS = "D", ("DevOps")
        INFRA = "I", ("Infra")
        COMMUNICATION = "C", ("Communication")
        LANGUAGE = "L", ("Language")
        UNKNOWN = "U", ("Unknown")

    category = models.CharField(
        max_length=1,
        choices=CategoryOfSkill.choices,
        default=CategoryOfSkill.UNKNOWN,
        verbose_name="스킬 계통",
    )
    name = models.CharField("스킬 이름", max_length=20, default="Unknown Skill")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "skill"
        verbose_name = "스킬"
        verbose_name_plural = "스킬"


class Description(BaseModel):
    content = models.TextField("설명")

    class Meta:
        db_table = "description"
        verbose_name = "상세내용"
        verbose_name_plural = "상세내용"

    def __str__(self):
        return self.content[:15] + "..."


class Tag(BaseModel):
    name = models.CharField("태그이름", max_length=30)

    class Meta:
        db_table = "tag"
        verbose_name = "태그"
        verbose_name_plural = "태그"

    def __str__(self):
        return self.name


class File(BaseModel):
    name = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255)
