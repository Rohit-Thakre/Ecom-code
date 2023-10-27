from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.User)
class AdminUser(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'number',
                    'verified', 'age', 'merchant', 'avatar']


@admin.register(models.Address)
class AdminAddress(admin.ModelAdmin):
    list_display = ['user', 'city', 'state', 'country',
                    'pin', 'selected', 'created', 'updated']


@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['type', 'by', 'created', 'updated']


@admin.register(models.Banner)
class AdminCategory(admin.ModelAdmin):
    list_display = ['img', 'by', 'created',]


@admin.register(models.Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'max_price', 'last_price',
                    'current_price', 'image', 'merchant']


@admin.register(models.Cart_item)
class AdminCart_ites(admin.ModelAdmin):
    list_display = ['product', 'count', 'created', 'updated', 'user']


# @admin.register(models.Payment_method)
# class AdminPayment_method(admin.ModelAdmin):
#     list_display = ['method']


# @admin.register(models.Status)
# class AdminStatus(admin.ModelAdmin):
#     list_display = ['status']


@admin.register(models.Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['payment_method', 'user', 'status', 'product']


@admin.register(models.Review)
class AdminReview(admin.ModelAdmin):
    list_display = ['product', 'img',
                    'rating', 'user', 'created', 'updated']
