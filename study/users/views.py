from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
    # 만약 HTTP 요청이 POST 방식일 때?
    
        if request.POST['password1'] == request.POST['password2']:
        # 사용자가 입력한 비밀번호와 비밀번호 확인 값이 일치한다면?
        
            user = User.objects.create_user(
            # 새로운 유저 객체를 생성한다.
                username = request.POST['username'],
                password = request.POST['password1'],
                email = request.POST['email'])
            # 유저 이름과 비밀번호, 이메일 필드를 입력받은 유저 객체!
            
            auth.login(request, user)
            # user 객체로 로그인함.
            
            return redirect('/')
            # 회원가입이 성공적으로 처리되었다면, '/'(홈)페이지로 이동.
            
        return render(request, 'signup.html')
        # 회원가입을 실패했다면, 다시 회원가입 페이지를 보여줌.
        
    return render(request, 'signup.html')      

# 위 코드는 사용자가 입력한 폼 데이터를 검증받지 않고 DB에 바로 저장하고 있기 때문에
# 좋은 방법은 아님. 이런 방식은 권장되지 않으므로, 적절한 폼 검증과 사용자 인증 절차
# 를 추가해서 보안적인 취약성을 방지해야 한다.


def login(request):
    if request.method == 'POST':
    # POST 요청을 받았을 시 (request.method를 사용해 현재 요청이 POST인지 확인함.)    
        
        username = request.POST['username']
        password = request.POST['password']
        # request.POST를 사용해 전송된 데이터를 가져온다.
        
        user = authenticate(request, usernaer=username, password=password)
        # authenticate를 사용해 사용자의 정보가 가져온 데이터와 일치하는지 확인한다.
        
        if user is not None:
            auth.login(request, user)
            # 확인에 성공했다면 auth.login() 함수를 사용해 사용자를 로그인시킨다.
            
            return redirect('home')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect.'})
            # 확인에 실패했다면 오류 메시지와 함께 로그인 페이지를 다시 렌더링한다.
    else:
        return render(request, 'login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')


# render: 함수나 html을 불러오면서 그 함수나 html에게 데이터 또한 전송할수 있게 함.
# redirect: 함수나 html을 반환시키는 게 전부임.