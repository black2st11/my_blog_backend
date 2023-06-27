from django.contrib import admin
from .models import Hunter, MySkill, Archiving, ArchDesc, Description

# Register your models here.


class MySkillInline(admin.TabularInline):
    model = MySkill


class MyArchivinInline(admin.TabularInline):
    model = Archiving


class DescriptionInline(admin.TabularInline):
    model = ArchDesc


@admin.register(Archiving)
class ArchDescAdmin(admin.ModelAdmin):
    list_display = ["id", "owner"]
    inlines = [DescriptionInline]


@admin.register(Hunter)
class HunterAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth", "address", "email"]
    inlines = [MySkillInline, MyArchivinInline]
