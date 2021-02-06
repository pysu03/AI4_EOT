from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from .forms import UserCreationForm


def index(request):
    return render(request, 'index.html')


# 회원 가입
# @login_required()
def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users')
    return render(request, 'signup.html', {'form': form})
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
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)

        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/users')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'login.html')


# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/users')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'login.html')