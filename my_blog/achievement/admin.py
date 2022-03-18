from django.contrib import admin
from .models import Achievement, AchieveDescription, AchieveSkill, AchieveFile
# Register your models here.

class AchDescInline(admin.TabularInline):
    model = AchieveDescription

class AchSkillInline(admin.TabularInline):
    model = AchieveSkill

class AchFileInline(admin.TabularInline):
    model = AchieveFile

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'position',)
    inlines =(AchDescInline, AchSkillInline, AchFileInline)
