from django.urls import path,include
from . import views

# for media
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', views.home, name='home'),
   path('accounts/', include('allauth.urls')),

    path('login/', views.login_method, name='login_method'),
    path('logout/', views.logout_method, name='logout_method'),
    path('register/', views.register_method, name='register_method'),

    path('otp_check/', views.check_otp, name='check_otp_method'),
    
    path('password_change/', views.password_change_method, name='password_change'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)