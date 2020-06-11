from django import forms
from .models import *
from django.contrib.auth.models import User

class question_form(forms.ModelForm):
    class Meta:
        model=questions_model
        fields=['author','question']
class answer_form(forms.ModelForm):
    class Meta:
        model=answers_model
        fields=['question','answer']
class signup_form(forms.ModelForm):
    class Meta:
        model=User
        #fields='__all__'
        fields=['username','password']
class profile_form(forms.ModelForm):
    class Meta:
        model=profile
        fields='__all__'
