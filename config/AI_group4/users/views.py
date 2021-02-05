from django.shortcuts import render, redirect
from django.http      import JsonResponse
from django.utils import timezone
from .models import *

# Create your views here.
from users.models import *


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def recommendForm(request):
    return render(request, 'recommendForm.html')

def registerForm(request):
    return render(request, 'registerForm.html')

def register(request):
    if request.method == 'POST':
        id = request.POST['user_id']
        pwd = request.POST['user_pwd']
        name = request.POST['user_name']
        birthday = request.POST['birthday']
        email = request.POST['email']
        city = request.POST['city']
        mobile = request.POST['mobile']
        register = memRegister(user_id=id, user_pwd=pwd, user_name=name, user_birthday=birthday, user_email=email, user_city=city, user_mobile=mobile)
        register.save()
    return render(request, 'login.html')

def loginProc(request):
    if request.method == 'GET':
        return redirect('index')
    elif request.method == 'POST':
        id  = request.POST['id']
        pwd = request.POST['pwd']
        user = memRegister.objects.get(user_id=id, user_pwd=pwd)
        print(user)
        context = {}
        if user is not None:
            request.session['user_name'] = user.user_name
            request.session['user_id'] = user.user_id
            context['name'] = request.session['user_name']
            context['id'] = request.session['user_id']
            return render(request, 'index.html')
        else:
            return redirect('index')


