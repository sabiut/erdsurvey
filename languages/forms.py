from django import forms

# setup date picker start
from .models import Survey, Question, Choice, TextChoice, CheckChoice


class DateInput(forms.DateInput):
    input_type = 'date'


class NewSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('title',)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('enter_question',)


class RadioChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice',)


class TexBoxForm(forms.ModelForm):
    class Meta:
        model = TextChoice
        fields = ('choice_text',)


class CheckBoxForm(forms.ModelForm):
    class Meta:
        model = CheckChoice
        fields = ('choice_check',)
