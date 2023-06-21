from django.contrib import admin
from .models import Question, Answer

# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("content", "created", "updated")
    inlines = (AnswerInline,)
