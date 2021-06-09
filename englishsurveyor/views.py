from django.shortcuts import render

# Create your views here.

from languages.models import Choice, Survey, SurveyAnswer, QuestionAnswer, TextChoice,CheckChoice


def survey_view(request, object_id=None):
    try:
        survey = Survey.objects.get(id=object_id)
        questions = survey.question_set.all()
        ctx = {'survey': survey, 'questions': questions}
    except:
        return render(request, 'surveynotfound-error.html', {'sv_id': object_id})
    return render(request, 'survey_take.html', ctx)


def survey_fill(request):
    ans = SurveyAnswer()
    orig_survey = Survey.objects.get(id=request.POST['survey_id'])
    ans.orig_survey = orig_survey
    ans.save()
    questions = orig_survey.question_set.all()
    for question in questions:
        qc = request.POST['question' + str(question.id)]
        qa = QuestionAnswer()
        qa.answer = Choice.objects.get(id=int(qc))
        # qa.answer = TextChoice.objects.get(id=int(qc))
        # qa.answer = CheckChoice.objects.get(id=int(qc))
        qa.survey_answer = ans
        qa.save()
    ans.save()
    return render(request, 'survey-complete.html', {})
