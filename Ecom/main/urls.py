from django.urls import path
from . import views

# for media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('add_product/', views.add_product, name='add_product'),
    path('merchant_details/', views.be_merchant, name='merchant_details'),
    path('cart/', views.cart, name='cart'),

    path('add_to_cart/<int:key>/', views.add_to_cart, name='add_to_cart'),

    path('remove_from_cart/<int:key>/',
         views.remove_from_cart, name='remove_from_cart'),
    path('product-view/<int:key>/', views.product, name='product'),

    path('category/<str:type>/', views.category_list, name='category'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
