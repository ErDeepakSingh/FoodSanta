from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class Sign_Up_Form(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email = forms.EmailField()
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']