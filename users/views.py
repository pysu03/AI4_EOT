from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.utils.http import is_safe_url

from config import settings
from .forms import UserCreationForm, LoginForm

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            email = form.cleaned_data.get("email") 
            password = form.cleaned_data.get("password1") 
            user = authenticate(username=email, password=password) 
            if user is not None: 
                login(request, user) 
                return redirect_after_login(request)
    return render(request, 'users/signup.html', {'form': form})

def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect_after_login(request)
        else:
            return HttpResponse('Login failed. Try again')
    else:
        return render(request, 'users/signin.html', {'form': form})

def logout(request):
    auth.logout(request)    
    return redirect('/')

def redirect_after_login(request):
    nxt = request.GET.get("next", None)
    if nxt is None:
        return redirect(settings.LOGIN_REDIRECT_URL)
    elif not is_safe_url(
            url=nxt,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure()):
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return redirect(nxt)
