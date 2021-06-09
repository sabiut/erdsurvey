from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Survey(models.Model):
    title = models.CharField(max_length=200)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    archive = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    enter_question = models.CharField(max_length=900)

    def __str__(self):
        return self.enter_question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)


class TextChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)


class CheckChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_check = models.CharField(max_length=100, null=True)


class SurveyAnswer(models.Model):
    orig_survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class QuestionAnswer(models.Model):
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)
    # text_answer = models.ForeignKey(TextChoice, on_delete=models.CASCADE)
    # check_answer = models.ForeignKey(CheckChoice, on_delete=models.CASCADE)
    survey_answer = models.ForeignKey(SurveyAnswer, on_delete=models.CASCADE)
