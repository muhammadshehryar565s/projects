# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# import attr


# class CustomRegistrationForm(UserCreationForm):
#     username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import PasswordChangeForm
from .models import Customer

from django.contrib.auth.forms import PasswordResetForm



class Loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class':'form-control' }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control' }))

    class Meta:
        model=User
        fields=['username','email','password1','password2']


class mypasswordreset(PasswordChangeForm):
    pass        



class CustomRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class passwordchange(PasswordChangeForm):
    old_password1=forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus':'True','class':'form-control'}))
    new_password1=forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autofocus':'True','class':'form-control'}))
    new_password2=forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autofocus':'True','class':'form-control'}))


class emailpassword(PasswordResetForm):
    email=forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))




class CustomerProfielForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields = '__all__'

        widgets={
            
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'})}