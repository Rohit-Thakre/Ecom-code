from django.urls import path
from . import views

# for media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path('remove_address/<int:key>/', views.remove_address, name='remove_address'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('add_product/', views.add_product, name='add_product'),
    path('review/<int:key>/', views.review, name='review'),
    path('merchant_details/', views.be_merchant, name='merchant_details'),
    path('cart/', views.cart, name='cart'),

    path('add_to_cart/<int:key>/', views.add_to_cart, name='add_to_cart'),

    path('remove_from_cart/<int:key>/',
         views.remove_from_cart, name='remove_from_cart'),
    path('product-view/<int:key>/', views.product, name='product'),
    path('product-like/<int:key>/', views.like_product, name='product-like'),
    path('product-dislike/<int:key>/', views.dislike_product, name='product-dislike'),

    path('category/<str:type>/', views.category_list, name='category'),


    path('new_category/', views.new_category_list, name='new_category'),

    path('payment/<int:key>/', views.payment, name='payment'),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
