from django import forms
from models import*

class Normal_Form(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()
    place=forms.CharField()

class Model_form(forms.Modelform):
    class meta:
        model=project_user
        fields='__all__'