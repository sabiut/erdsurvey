from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from languages.models import Survey

from languages.forms import NewSurveyForm


def signin(request):
    return render(request, 'loginpage.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def dashboard(request):
    return render(request, 'dashboard.html')


def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        if user.groups.filter(name="member").exists():
            return HttpResponseRedirect('/dashboard')
        else:
            messages.info(request, 'Username or Password Incorrect')
    return HttpResponseRedirect('/signin')


def admin_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        if user.groups.filter(name="administrator").exists():
            return HttpResponseRedirect('/admin_dashboard')
        else:
            messages.info(request, 'Username or Password Incorrect')
    return HttpResponseRedirect('/admin_page')
    # return render(request, 'login.html')


def admin_page(request):
    return render(request, 'admin_login.html')


def admin_dashboard(request):
    survey = Survey.objects.filter(archive='')
    return render(request, 'admin_dashboard.html', {'survey': survey})


def admin_logout(request):
    logout(request)
    return redirect('/')


def archive_survey(request, archive_id):
    """Archive the survey"""
    get_id = Survey.objects.get(id=archive_id)
    get_id.archive = "archived"
    get_id.save()
    return redirect('/admin_dashboard')


def edit_survey(request, get_survey_id):
    if request.method == 'POST':
        surveyid = Survey.objects.get(id=get_survey_id)
        form = NewSurveyForm(request.POST, instance=surveyid)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin_dashboard')

    else:
        surveyid = Survey.objects.get(id=get_survey_id)
        form = NewSurveyForm(instance=surveyid)
        return render(request, 'edit_survey.html', {'form': form})


def delete_survey(request, get_survey_id):
    """delete survey record"""
    try:
        survey_record = Survey.objects.get(id=get_survey_id)
        survey_record.delete()
        return HttpResponseRedirect('/admin_dashboard')
    except(survey_record.DoestNotExist):
        messages.warning(request, 'Selected record was not found on the system.')
        #return render(request, 'record_not_exist.html')
