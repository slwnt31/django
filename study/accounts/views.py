from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

#회원가입
def signup(request):
    #http 요청이 post 방식일 때 실행합니다.
    if request.method=='POST':
        #사용자가 입력한 비밀번호와 비밀번호 확인 값이 일치하는 지 확인합니다.
        if request.POST['password1']==request.POST['password2']:
            #새로운 유저 객체를 생성합니다.
            user=User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )
            #user 객체로 로그인합니다.
            auth.login(request, user)
            #회원가입이 성공적으로 처리되었다면, '/'(홈) 페이지로 이동합니다.
            return redirect('/')
        #회원가입이 실패한 경우, 다시 회원가입 페이지를 보여줍니다.
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password'})
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')