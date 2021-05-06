from django.contrib import admin

from django.contrib import admin
from django.db.models import Choices

from .models import Survey, Choice, Question

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
