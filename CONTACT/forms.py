from django import forms
from . import models as contact_models
from django.contrib.auth import models as auth_models
class Contact_Form(forms.Form):
    name = forms.CharField(max_length=500,label='Name  ',widget=forms.TextInput({'class':'form-control'}))
    mobile_no = forms.CharField(max_length=500,label='Mobile Number  ',widget=forms.TextInput({'class':'form-control'}))
    email = forms.EmailField(max_length=500,label='Email ID  ',widget=forms.TextInput({'class':'form-control'}))
    message = forms.CharField(max_length=500,label='Message  ',widget=forms.Textarea({'class':'form-control'}))

