from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    """Form definition for ."""

    class Meta:
        """Meta definition for form."""
        model = User
        fields = ('full_name', 'email', 'number', 'age', 'merchant', 'avatar')
