from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
# Create your views here.

from .forms import RegisterForm


def user_login(request):

    return render(request, 'login.html')


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
