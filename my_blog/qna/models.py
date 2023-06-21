from django.db import models

from common.models import BaseModel

# Create your models here.


class Question(BaseModel):
    ip = models.CharField("세계", max_length=50, null=True)
    content = models.TextField("내용")

    class Meta:
        verbose_name = "질문"
        verbose_name_plural = "질문"


class Answer(BaseModel):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers", verbose_name="질문"
    )
    content = models.TextField("내용")

    class Meta:
        verbose_name = "답변"
        verbose_name_plural = "답변"
