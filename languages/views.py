from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from .forms import NewSurveyForm, QuestionForm, RadioChoiceForm
from .models import Survey, Question


def english(request):
    return render(request, 'english.html')


def french(request):
    return render(request, 'french.html')


def bislama(request, get_id):
    id = get_id
    return render(request, 'bislama.html', locals())


# def create_new_survey(request):
#     return render(request, 'create_new_survey.html')


def create_new_survey(request):
    if request.method == 'POST':
        form = NewSurveyForm(request.POST)
        if form.is_valid():
            new_contact = form.save()
            return HttpResponseRedirect(reverse(add_question, args=(new_contact.id,)))

    else:
        form = NewSurveyForm()
    return render(request, 'create_new_survey.html', {'form': form})


def add_question(request, survey_id):
    if request.method == 'POST':
        surverid = Survey.objects.get(id=survey_id)
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.instance.survey = surverid
            question_id = form.save()
            return HttpResponseRedirect(reverse(add_choice, args=(question_id.id,)))
    else:
        form = QuestionForm()
        return render(request, 'question.html', {'form': form}, )


def add_choice(request, question_id):
    if request.method == 'POST':
        questionid = Question.objects.get(id=question_id)
        form = RadioChoiceForm(request.POST)
        if form.is_valid():
            form.instance.question = questionid
            question_id = form.save()
        return HttpResponseRedirect(reverse(add_choice, args=(question_id.id,)))
    else:
        form = RadioChoiceForm()
        return render(request, 'add_choices.html', {'form': form}, )
