from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    username = forms.CharField(label="Register Number" ,required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['candidates']