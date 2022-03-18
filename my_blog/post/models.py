from pyexpat import model
from unicodedata import category
from django.db import models
from rest_framework.views import APIView
from info.models import Tag
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    file = models.CharField(max_length=255, default='')

    class Meta:
        db_table = u'post'

    def __str__(self):
        return self.title


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tag_cabinet')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta :
        db_table = u'post_tag'

    