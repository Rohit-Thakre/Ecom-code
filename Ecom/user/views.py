from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
# from .models import User
from main.models import User



# Create your views here.
def home(request):
    return render(request, 'user/base.html')


def login_method(request):

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
                return render(request, 'user/login.html', {'val': True,  'msg': "Password Incorrect !"})

        else:
            return render(request, 'user/login.html', {'val': True,  'msg': "No account with this email"})

    return render(request, 'user/login.html', {'val': False})


def logout_method(request):
    logout(request)
    return redirect('home')


def register_method(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        try:
            usr_obj = User.objects.get(email = email)

            if usr_obj: 
                print('email taken')
                return render(request, 'user/register.html', {'val': True, 'msg': 'Email Taken !'})
        

        except:
            user_obj = User.objects.create(full_name=full_name, email=email, username = full_name+'+'+email)
            user_obj.set_password(pass1)
            user_obj.save()
            login(request, user_obj)
            return redirect('home')


    return render(request, 'user/register.html')


import random
user_obj = None
otp_gen = random.randrange(100000,999999)
def check_otp(request):

    if request.method == 'POST':
        
        email = request.POST.get('email')
        otp = request.POST.get('otp')

        print('generated otp : ', otp_gen)
            

        global user_obj
        user_obj = User.objects.filter(email = email)


        if  not user_obj: 
            return render(request, 'user/check_otp.html', {'val':True, 'msg':'Email does not exists!'})

        elif not otp: 
            send_mail_after_registration(email, otp_gen)
            print('email send step tak aa rha hai')
            return render(request,'user/check_otp.html', {'otp' : True, 'email': email})
    

        elif otp_gen == int(otp) : 
            print('password change page redirect----------')
            return redirect('password_change')
        
        else: 
            print('otp_input \t otp_gen')
            print(otp, otp_gen)
            return render(request, 'user/check_otp.html',{'val':True, 'msg':'Incorrect OTP!', 'otp': True, 'email':email} )

      
    return render(request,'user/check_otp.html')



def password_change_method(request):

    if request.method == 'POST':

        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            user_obj.set_password(pass1)
            user_obj.save()

            login(request,user_obj)

            return redirect('home')
        

    return render(request, 'user/password_reset.html')




from django.conf import settings
from django.core.mail import send_mail
def send_mail_after_registration(email , token):
    subject = 'OTP for Password reset.'
    message = f'Hi,\nHere is your OTP : \n{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )



