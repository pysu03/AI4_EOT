from django.shortcuts import render, redirect
from django.http      import JsonResponse
from django.utils import timezone
from .models import *

# Create your views here.
from users.models import *


def index(request):
    print('request index - ')
    return render(request, 'index.html')

def login(request):
    print('request login - ')
    return render(request, 'login.html')

def registerForm(request):
    print('registerForm - ')
    return render(request, 'registerForm.html')

def register(request):
    print('register - ')
    if request.method == 'POST':
        id = request.POST['user_id']
        pwd = request.POST['user_pwd']
        name = request.POST['user_name']
        birthday = request.POST['birthday']
        email = request.POST['email']
        city = request.POST['city']
        gu = request.POST['gu']
        dong = request.POST['dong']
        mobile = request.POST['mobile']
        register = memRegister(user_id=id, user_pwd=pwd, user_name=name, user_birthday=birthday, user_email=email, user_city=city, user_gu=gu, user_dong=dong, user_mobile=mobile)
        register.save()
    return render(request, 'login.html')



def loginProc(request):
    print('request - loginProc')
    if request.method == 'GET':
        return redirect('index')
    elif request.method == 'POST':
        id  = request.POST['id']
        pwd = request.POST['pwd']
        # DB와 연동시키는 것
        # select * from userregister where user_id = id and user_pwd = pwd
        # orm class - table
        user = memRegister.objects.get(user_id=id, user_pwd=pwd)
        print('user result - ', user)
        context = {}
        if user is not None:
            request.session['user_name'] = user.user_name
            request.session['user_id'] = user.user_id    # session create
            context['name'] = request.session['user_name']
            context['id'] = request.session['user_id']  # session write(심는 작업)
            return render(request, 'index.html')
        else:
            return redirect('index')
