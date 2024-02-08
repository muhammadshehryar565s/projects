from django import forms
from .models import getimage

class imageForm(forms.ModelForm):
    class Meta:
        model=getimage
        fields='__all__'
        labels={'image':''}