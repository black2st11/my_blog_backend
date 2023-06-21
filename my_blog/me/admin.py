from django.contrib import admin
from .models import Me, MySkill, Archiving, ArchDesc, MyDesc

# Register your models here.


class MyDescInline(admin.TabularInline):
    model = MyDesc


class MySkillInline(admin.TabularInline):
    model = MySkill


class ArchDescInline(admin.TabularInline):
    model = ArchDesc


@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth", "address", "email"]
    inlines = [MyDescInline, MySkillInline]


@admin.register(Archiving)
class ArchivingAdmin(admin.ModelAdmin):
    list_display = ("category",)
    inlines = [ArchDescInline]
