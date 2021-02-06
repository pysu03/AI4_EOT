from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth

def weather(request):
    return render(request, 'weather.html')
