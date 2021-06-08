from django.shortcuts import render

# Create your views here.
from languages.models import Survey

from languages.models import Choice


def survey_view(request, object_id=None):
    try:
        survey = Survey.objects.get(id=object_id)
        questions = survey.question_set.all()
        ctx = {'survey': survey, 'questions': questions}
    except:
        return render(request, 'surveynotfound-error.html', {'sv_id': object_id})
    return render(request, 'survey_take.html', ctx)
