from django import forms
from .models import user,Userc
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class feedback(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name','email','rating','feedback']

class contact(forms.ModelForm):
    class Meta:
        model = Userc
        fields = ['name','email','contactno','massage']