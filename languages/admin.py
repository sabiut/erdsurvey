from django.contrib import admin

from django.contrib import admin
from django.db.models import Choices

from .models import Survey, Choice, Question, TextChoice, CheckChoice, SurveyAnswer, QuestionAnswer

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(TextChoice)
admin.site.register(CheckChoice)
admin.site.register(SurveyAnswer)
admin.site.register(QuestionAnswer)
