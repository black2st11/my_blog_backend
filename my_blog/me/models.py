from common.models import BaseModel
from django.db import models

# Create your models here.


class Me(BaseModel):
    name = models.CharField("이름", default="", max_length=30)
    phone = models.CharField("연락처", default="00000000000", max_length=12)
    birth = models.DateField("생년월일")
    email = models.EmailField("이메일")
    edu = models.CharField("학력", default="", max_length=100)
    address = models.CharField("주소", default="", max_length=100)

    class Meta:
        db_table = "me"
        verbose_name = "모험가"
        verbose_name_plural = "모험가"

    def __str__(self):
        return self.name


class MySkill(BaseModel):
    me = models.ForeignKey(Me, on_delete=models.DO_NOTHING, related_name="my_skill")
    skill = models.ForeignKey("info.Skill", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "my_skill"


class Archiving(BaseModel):
    owner = models.ForeignKey(
        Me, on_delete=models.CASCADE, related_name="archivings", verbose_name="모험가"
    )
    category = models.CharField("주제명", max_length=20)

    class Meta:
        db_table = "archiving"
        verbose_name = "주제"
        verbose_name_plural = "주제"

    def __str__(self):
        return self.category


class MyDesc(BaseModel):
    me = models.ForeignKey(
        Me,
        on_delete=models.DO_NOTHING,
        related_name="desc_cabinet",
        related_query_name="desc_cabinets",
    )
    description = models.ForeignKey(
        "info.description", on_delete=models.DO_NOTHING, related_name="descs"
    )

    class Meta:
        db_table = "my_desc"


class ArchDesc(BaseModel):
    archiving = models.ForeignKey(
        Archiving, on_delete=models.DO_NOTHING, related_name="desc_cabinet"
    )
    description = models.ForeignKey("info.Description", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "arch_desc"


class Education(BaseModel):
    me = models.ForeignKey(
        Me, on_delete=models.DO_NOTHING, related_name="educations", verbose_name="모험가"
    )
    name = models.CharField("훈련장명", max_length=50)
    major = models.CharField("전공", max_length=50)
    point = models.DecimalField("학점", max_digits=3, decimal_places=2)
    full_point = models.DecimalField("전체학점", max_digits=3, decimal_places=2)
    started = models.DateField("시작날짜")
    ended = models.DateField("종료날짜", null=True, blank=True)

    class Meta:
        verbose_name = "훈련장"
        verbose_name_plural = "훈련장"
