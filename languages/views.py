from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .forms import NewSurveyForm, QuestionForm, RadioChoiceForm, TexBoxForm, CheckBoxForm
from .models import Survey, Question


def english(request):
    return render(request, 'english.html')


def french(request):
    return render(request, 'french.html')


def bislama(request, get_id):
    id = get_id
    return render(request, 'bislama.html', locals())


def create_new_survey(request):
    """Creating a new survey"""
    if request.method == 'POST':
        form = NewSurveyForm(request.POST)
        if form.is_valid():
            survey_id = form.save()
            return HttpResponseRedirect(reverse(add_question, args=(survey_id.id,)))

    else:
        form = NewSurveyForm()
    return render(request, 'create_new_survey.html', {'form': form})


def add_question(request, survey_id):
    """adding the question to the survey"""
    if request.method == 'POST':
        surverid = Survey.objects.get(id=survey_id)
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.instance.survey = surverid
            question_id = form.save()
            return HttpResponseRedirect(reverse(add_choice, args=(question_id.id,)))
    else:
        form = QuestionForm()
        get_surveyid = Survey.objects.get(id=survey_id)
        survey_title = get_surveyid.title

        return render(request, 'question.html',
                      {'form': form, 'survey_title': survey_title})


def add_choice(request, question_id):
    """adding the choices"""
    if request.method == 'POST':
        questionid = Question.objects.get(pk=question_id)
        form = RadioChoiceForm(request.POST)
        if form.is_valid():
            form.instance.question = questionid
            question_id = form.save()
        return HttpResponseRedirect(reverse(add_choice, args=(question_id.question_id,)))
    else:
        form = RadioChoiceForm()
        question_id = Question.objects.get(pk=question_id)
        question_name = question_id.enter_question

        return render(request, 'add_choices.html',
                      {'form': form, 'question_name': question_name, 'question_id': question_id})


def add_textbox_choice(request, question_id):
    """adding the textbox choices"""
    if request.method == 'POST':
        questionid = Question.objects.get(pk=question_id)
        form = TexBoxForm(request.POST)
        if form.is_valid():
            form.instance.question = questionid
            question_id = form.save()
        return HttpResponseRedirect(reverse(add_choice, args=(question_id.question_id,)))
    else:
        form = TexBoxForm()
        question_id = Question.objects.get(pk=question_id)
        question_name = question_id.enter_question

        return render(request, 'add_textbox_choices.html',
                      {'form': form, 'question_name': question_name, 'question_id': question_id})


def add_checkbox_choice(request, question_id):
    """adding the textbox choices"""
    if request.method == 'POST':
        questionid = Question.objects.get(pk=question_id)
        form = CheckBoxForm(request.POST)
        if form.is_valid():
            form.instance.question = questionid
            question_id = form.save()
        return HttpResponseRedirect(reverse(add_choice, args=(question_id.question_id,)))
    else:
        form = CheckBoxForm()
        question_id = Question.objects.get(pk=question_id)
        question_name = question_id.enter_question

        return render(request, 'add_checkbox_choices.html',
                      {'form': form, 'question_name': question_name, 'question_id': question_id})


def archived_survey(request):
    survey = Survey.objects.filter(archive='archived')
    return render(request, 'survey.html', {'survey': survey})
