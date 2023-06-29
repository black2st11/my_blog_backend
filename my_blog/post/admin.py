from django.contrib import admin

from .models import Post, PostTag

# Register your models here.


class PostTagInline(admin.TabularInline):
    model = PostTag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "updated")
    inlines = (PostTagInline,)
