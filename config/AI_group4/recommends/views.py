from django.shortcuts import render, redirect
from django.http      import JsonResponse
from django.utils import timezone
from .models import *


def index(request):
    print('request index - ')
    return render(request, 'index.html')

def recommendForm(request):
    return render(request, 'recommendForm.html')
