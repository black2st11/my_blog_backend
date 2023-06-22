from django.contrib import admin
from .models import Hunter, MySkill, Archiving, ArchDesc

# Register your models here.


class MySkillInline(admin.TabularInline):
    model = MySkill


@admin.register(Hunter)
class HunterAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth", "address", "email"]
    inlines = [MySkillInline]
