from . import models
from django import forms
#from .models import Visitor
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import modelformset_factory, modelform_factory, inlineformset_factory
from django.contrib.auth.models import User
#Creating a form here
class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','username', 'first_name', 'last_name', 'password']