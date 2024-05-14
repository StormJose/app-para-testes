# users/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    location = forms.CharField(required=False)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'location', 'birth_date']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'birth_date']
