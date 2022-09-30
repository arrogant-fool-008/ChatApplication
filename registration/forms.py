from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    class meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
       