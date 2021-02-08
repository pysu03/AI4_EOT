from django import forms
from .models import Board


class BaseBulletinBoard(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'