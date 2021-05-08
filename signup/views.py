from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from languages.models import Survey


def signin(request):
    return render(request, 'loginpage.html')


def logout_view(request):
    logout(request)
    return redirect('signin')


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
