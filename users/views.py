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
from .tokens import account_activation_token

<<<<<<< HEAD
=======

def index(request):
    return render(request, 'users/index.html')

# 회원가입
>>>>>>> remotes/origin/feature/login/ykk
def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
<<<<<<< HEAD

            email = form.cleaned_data.get("email") 
            password = form.cleaned_data.get("password1") 
            user = authenticate(username=email, password=password) 
            if user is not None: 
                login(request, user) 
                return redirect_after_login(request)
    return render(request, 'users/signup.html', {'form': form})
=======
            # user =
            # current_site = get_current_site(request)
            # message = render_to_string('accounts/activateEmail.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # mail_title = "계정 활성화 확인 이메일"
            # mail_to = request.POST["email"]
            # email = EmailMessage(mail_title, message, to=[mail_to])
            # email.send()
            return redirect('/users/signin')
    print (form.errors)
    return render(request, 'users/signup.html', {'form': form})

# 이메일 인증
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoseNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        # return redirect_after_login(request)
        else:
            return redirect('/users')
    else:
        return render(request, 'users/index.html', {'error' : '계정 활성화 오류'})
>>>>>>> remotes/origin/feature/login/ykk

def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
<<<<<<< HEAD
            return redirect_after_login(request)
=======
            # return redirect('/users')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            # return redirect_after_login(request)
            else:
                return redirect('/users')
>>>>>>> remotes/origin/feature/login/ykk
        else:
            return HttpResponse('Login failed. Try again')
    else:
        return render(request, 'users/signin.html', {'form': form})

<<<<<<< HEAD
def logout(request):
    auth.logout(request)    
    return redirect('/')
=======
# 로그아웃
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/users')
    return render(request, 'users/signin.html')
>>>>>>> remotes/origin/feature/login/ykk

# def redirect_after_login(request):
#     nxt = request.GET.get("next", None)
#     if nxt is None:
#         return redirect(settings.LOGIN_REDIRECT_URL)
#     elif not is_safe_url(
#             url=nxt,
#             allowed_hosts={request.get_host()},
#             require_https=request.is_secure()):
#         return redirect(settings.LOGIN_REDIRECT_URL)
#     else:
#         return redirect(nxt)