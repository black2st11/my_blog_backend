from django.contrib import admin
from .models import Dungeon, DungeonDescription, DungeonSkill
# Register your models here.

class DungeonDescInline(admin.TabularInline):
    model = DungeonDescription

class DungeonSkillInline(admin.TabularInline):
    model = DungeonSkill

@admin.register(Dungeon)
class DungeonAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'difficulty', 'size', 'loc', 'impression', )
    inlines = (DungeonDescInline, DungeonSkillInline, )
