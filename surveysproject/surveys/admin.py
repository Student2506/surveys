from django.contrib import admin

from .models import Survey, Question, Answer, Customer, SurveyInstance


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    empty_value_display = "-пусто-"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    empty_value_display = "-пусто-"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    empty_value_display = "-пусто-"


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    empty_value_display = "-пусто-"


@admin.register(SurveyInstance)
class SUAdmin(admin.ModelAdmin):
    empty_value_display = "-пусто-"
