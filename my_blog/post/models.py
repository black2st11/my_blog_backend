from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from common.models import BaseModel
from info.models import Tag, Attach

# Create your models here.


class Post(BaseModel):
    title = models.CharField("제목", max_length=100)
    content = RichTextUploadingField("내용")
    tags = models.ManyToManyField(Tag, related_name="posts", through="post.PostTag")
    attach = models.ManyToManyField(
        Attach, related_name="posts", through="post.PostAttach"
    )

    class Meta:
        ordering = ["-id"]
        db_table = "post"
        verbose_name = "게시판"
        verbose_name_plural = "게시판"

    def __str__(self):
        return self.title


class PostTag(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class PostAttach(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    attach = models.ForeignKey(Attach, on_delete=models.CASCADE)
