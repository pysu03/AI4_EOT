from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from config import settings
from .forms import UserCreationForm, LoginForm
from .models import User

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text


def index(request):
    return render(request, 'users/index.html')

# 회원가입
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
                return redirect('/')

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
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            return render(request, 'users/signin.html', {'form': form})
    else:
        return render(request, 'users/signin.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')