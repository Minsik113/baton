#import json

from django.shortcuts import render, redirect
#from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])

def home(request):
    return render(request, 'home/home.html', {})

def user_register(request):
    if request.method == "POST":
        if request.POST.get("password1",False) == request.POST.get("password2",False):
            user = User.objects.create_user(
                username=request.POST.get("username",False),password=request.POST.get("password1",False),email=request.POST.get("email",False))
            auth.login(request,user)
            return redirect('home')
        return render(request, 'user_register.html')

    return render(request, 'home/user_register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'user_login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'home/user_login.html')

def user_logout(request):
    auth_logout(request)
    return redirect('home')

def service_notice(request):
    return render(request, 'home/service_notice.html')

def service_center(request):
    return render(request, 'home/service_center.html')

def user_mypage(request):
    return render(request, 'home/user_mypage.html')

def product_add(request): #상품추가
    return render(request, 'home/product_add.html')

def chat_room(request): #메시지
    return render(request, 'home/chat_room.html')

def product_like(request): #관심상품
    return render(request, 'home/product_like.html')