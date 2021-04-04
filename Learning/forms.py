from django import forms
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']


class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['name','Email','age']
