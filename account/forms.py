from django import forms
from django.contrib.auth.forms import UserCreationForm 
from account.models import RegisterModel
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = RegisterModel
        fields = ("phone",)