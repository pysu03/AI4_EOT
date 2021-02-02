from django.shortcuts import render, redirect
from django.http      import JsonResponse
from django.utils import timezone

# Create your views here.
from users.models import userRegister


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
        id = request.POST['id']
        pwd = request.POST['pwd']
        name = request.POST['name']
        birthday = request.POST['birthday']
        email = request.POST['email']
        city = request.POST['city']
        dong = request.POST['dong']
        mobile = request.POST['mobile']
        register = userRegister(user_id=id, user_pwd=pwd, user_name=name,
                                birthday=birthday, email=email,
                                city=city, dong=dong, mobile=mobile)
        register.save()
    return render(request, 'login.html')
