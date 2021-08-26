from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta: #THIS NEEDS TO BE EXACT "META"
        model=User #This is the value in the db that will be changed
        fields=["username","email","password1","password2"]
        


