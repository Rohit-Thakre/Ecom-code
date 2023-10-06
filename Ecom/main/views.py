from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from .models import Cart, User, Order, Review, Address, Category, Product, Cart_item

from .forms import RegisterForm
from .forms import LoginForm


def user_login(request):

    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        email_check = User.objects.filter(email=email)
        if email_check:
            instance = authenticate(email=email, password=password)
            if instance:
                login(request, instance)
                return redirect('product')
            else:
                return render(request, 'login.html', {'val': True,  'msg': "Password Incorrect !"})

        else:
            return render(request, 'login.html', {'val': True,  'msg': "No account with this email"})

    return render(request, 'login.html', {'val': False})


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


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'temp.html', context)


def user(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'temp.html', context)
