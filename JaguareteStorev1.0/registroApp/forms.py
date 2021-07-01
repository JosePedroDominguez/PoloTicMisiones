from django import forms
from django.db.models import fields 
from registroApp.models import User
class FomularioUser(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'
        