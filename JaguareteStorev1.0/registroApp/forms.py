from django import forms
from django.db.models import fields 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CustomUserForm(UserCreationForm):
  class Meta:
    model = User
    fields =['username',"email","password1","password2"]    