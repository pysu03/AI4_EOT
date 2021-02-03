from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginForm(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        user_pwd = request.POST["user_pwd"]
        user = authenticate(user_id=user_id, user_pwd=user_pwd)
        if user is not None :
            print("인증성공")
            login(request, user)
        else :
            print("인증실패")

    return render(request, 'login.html')

def accountForm(request):
    if request.method == "POST":
        print(request.POST)
        user_id = request.POST["user_id"]
        user_pwd = request.POST["user_pwd"]
        user_name = request.POST["user_name"]
        user_birthday = request.POST["user_birthday"]
        user_mobile = request.POST["user_mobile"]
        user_email = request.POST["user_email"]
        user_address = request.POST["user_address"]

        user = User.objects.create_user(user_id, user_email, user_pwd)
        user.last_name = user_name
        user.last_birthday = user_birthday
        user.last_mobile = user_mobile
        user.last_address = user_address
        user.save()
        return redirect('loginForm')

    return render(request, 'accountForm.html')


