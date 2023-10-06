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
                return redirect('home')
            else:
                return render(request, 'login.html', {'val': True,  'msg': "Password Incorrect !"})

        else:
            return render(request, 'login.html', {'val': True,  'msg': "No account with this email"})

    return render(request, 'login.html', {'val': False})


def user_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', '')
        pass1 = request.POST.get('pass1', '')
        pass2 = request.POST.get('pass2', '')

        if full_name != '' and email != '' and pass1 != pass2:
            return render(request, 'register.html', {'val': True, 'msg': 'Fill all fields !'})

        if pass1 != pass2:
            return render(request, 'register.html', {'val': True, 'msg': 'passwords are different !'})

        else:
            user_obj = User(full_name=full_name, email=email)
            user_obj.set_password(pass1)
            user_obj.save()
            login(request, user_obj)
            return redirect('home')

    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'temp.html', context)


def user(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'temp.html', context)
