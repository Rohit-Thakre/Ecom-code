from django import forms
from .models import User, Product, Review
from django.contrib.auth.forms import UserCreationForm

class ReviewForm(forms.ModelForm):

    img = forms.ImageField()
    img.label = ""
    img.widget.attrs.update({'class':'form-control'})

    class Meta: 
        model = Review
        fields = ['img']


class ProductForm(forms.ModelForm):

    image = forms.ImageField()
    image.label = ""
    image.widget.attrs.update({'class':'form-control'})

    class Meta: 
        model = Product
        fields = ['image']



class UserForm(forms.ModelForm):

    avatar = forms.ImageField()
    avatar.widget.attrs.update({'class':'form-control'})

    class Meta: 
        model = User
        fields = ['avatar']

        # fields = ['full_name', 'number', 'age', 'avatar']
        

        # widgets = {
        #     'full_name' : forms.TextInput(attrs={'class':'form-control', 'required': 'required'}),
        #     'number' : forms.TextInput(attrs={'class':'form-control', 'required': 'required'}),
        #     'age' : forms.TextInput(attrs={'class':'form-control', 'required': 'required'}),
        # }



        