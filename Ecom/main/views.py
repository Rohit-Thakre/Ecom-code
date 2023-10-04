from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
# Create your views here.

from .forms import RegisterForm
from .forms import LoginForm


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            instance = authenticate(email=request.POST.get('email', 0),
                                    password=request.POST.get('password', 0))
            if instance:
                login(request, instance)
                return HttpResponse('logged in')
            else:
                return HttpResponse('username or password incorrect')

    context = {'form': form}

    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return HttpResponse('Logged out')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            instance = form.instance
            login(request, instance)
            return HttpResponse('logged in as ' + request.POST.get('full_name'))
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'login.html', context)
