from django import forms
from .models import User, Product, Review, Address
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



        

class AddressForm(forms.ModelForm): 

    class Meta:
        model = Address
        fields = ['street', 'area','city', 'state', 'country', 'pin']
        widgets = {
            'street' : forms.TextInput(attrs={'class':'form-control', 'required': 'required'}),
            'area' : forms.TextInput(attrs={'class':'form-control', 'required': 'required'}),
            'city' : forms.TextInput(attrs={'class':'form-control', 'required': 'required'}),
            'state' : forms.TextInput(attrs={'class':'form-control', 'required': 'required'}),
            'country' : forms.TextInput(attrs={'class':'form-control', 'required': 'required'}),
            'pin' : forms.TextInput(attrs={'class':'form-control', 'required': 'required'}),
        }