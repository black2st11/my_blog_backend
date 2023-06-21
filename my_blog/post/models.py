from pyexpat import model
from unicodedata import category
from django.db import models
from rest_framework.views import APIView
from common.models import BaseModel
from info.models import Tag

# Create your models here.


class Post(BaseModel):
    title = models.CharField(max_length=100)
    file = models.CharField(max_length=255, default="")

    class Meta:
        db_table = "post"

    def __str__(self):
        return self.title


class PostTag(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="tag_cabinet")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = "post_tag"
