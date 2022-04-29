from django import forms
from . models import tool

class toolform(forms.ModelForm):
    class Meta:
        model=tool
        fields=['name','desc','year','img']