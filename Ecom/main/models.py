from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(unique=True)

    number = models.CharField(max_length=15, null=True)
    verified = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True)
    merchant = models.BooleanField(default=False)
    avatar = models.ImageField(
        null=True, default="avatar.svg", upload_to='user/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
