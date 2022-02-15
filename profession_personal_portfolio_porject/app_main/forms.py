from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from .models import *


class ContactForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Contact
        fields = ('__all__')
        # widgets = 'full_name': forms.TextInput(attrs={'class': 'form-control'})
