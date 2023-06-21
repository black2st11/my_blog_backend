from common.models import BaseModel
from django.db import models

# Create your models here.


class Me(BaseModel):
    name = models.CharField(default="", max_length=30)
    phone = models.CharField(default="00000000000", max_length=12)
    birth = models.DateField()
    email = models.EmailField()
    edu = models.CharField(default="", max_length=100)
    address = models.CharField(default="", max_length=100)

    class Meta:
        db_table = "me"

    def __str__(self):
        return self.name


class MySkill(BaseModel):
    me = models.ForeignKey(Me, on_delete=models.DO_NOTHING, related_name="my_skill")
    skill = models.ForeignKey("info.Skill", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "my_skill"


class Archiving(BaseModel):
    category = models.CharField(max_length=20)

    class Meta:
        db_table = "archiving"

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
        "info.Description", on_delete=models.DO_NOTHING, related_name="descs"
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
    me = models.ForeignKey(Me, on_delete=models.DO_NOTHING, related_name="educations")
    name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    point = models.DecimalField()
    full_point = models.DecimalField()
    started = models.DateField()
    ended = models.DateField(null=True, blank=True)
