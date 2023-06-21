from django.db import models

from common.models import BaseModel

# Create your models here.


class Question(BaseModel):
    ip = models.CharField(max_length=50, null=True)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)


class Answer(BaseModel):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    content = models.TextField()
