from django.contrib import admin
from .models import Skill, Tag, Description, File
# Register your models here.

admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Description)
admin.site.register(File)