from django import forms
from django.contrib.auth.models import User #1

class UserForm(forms.ModelForm):
    class Meta: #2
        model = User
        fields = ['username', 'email', 'password']