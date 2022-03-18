from django.contrib import admin
from .models import Career, CareerDescription, CareerSkill
# Register your models here.

class CareerDescInline(admin.TabularInline):
    model = CareerDescription

class CareerSkillInline(admin.TabularInline):
    model = CareerSkill


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('name' ,'work', 'position', 'start_date', 'end_date', )
    inlines = (CareerDescInline, CareerSkillInline)
