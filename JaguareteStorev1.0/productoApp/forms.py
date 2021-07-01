from django import forms
from django.db.models import fields 
from productoApp.models import Items
class FomularioItem(forms.ModelForm):
    class Meta:
        model = Items
        fields ='__all__'
        