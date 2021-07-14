from django.contrib import admin

from .models import Survey, Question, Answer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    empty_value_display = "-пусто-"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    empty_value_display = "-пусто-"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    empty_value_display = "-пусто-"
