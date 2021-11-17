from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *





class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']








class refundForm(forms.ModelForm):
    class Meta:
        model = refund
        fields = ('client_email', 'name', 'bank_name', 'account_number', 'value', )
