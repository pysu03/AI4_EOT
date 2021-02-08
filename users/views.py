from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from .forms import UserCreationForm, LoginForm


def index(request):
    return render(request, 'users/index.html')


# 회원 가입
# @login_required()
def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users')
    return render(request, 'users/signup.html', {'form': form})
    # # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    # if request.method == 'POST':
    #     # password와 confirm에 입력된 값이 같다면
    #     if request.POST['password'] == request.POST['confirm']:
    #         # user 객체를 새로 생성
    #         user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    #         # 로그인 한다
    #         auth.login(request, user)
    #         return redirect('/users')
    # # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    # return render(request, 'signup.html')


# 로그인
def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/users')
        else:
            return HttpResponse('Login failed. Try again')
    else:
        return render(request, 'users/signin.html', {'form': form})

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/users')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'users/signin.html')