from django.shortcuts import render
# View에 Model(Post 게시글) 가져오기
from .models import Post

# Create your views here.

# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')

# blog.html 페이지를 부르는 blog 함수
def blog(request):
    # 모든 Post를 가져와 postlist에 저장한다.
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist': postlist})
# models.py에 정의한 모든 Post를 가져와 postlist라는 변수이자 객체에 저장함. -> main/blog.html을
# 호출했을 시에, 따옴표 안에 있는 postlist라는 이름으로 정보를 보내줌.

# blog의 게시글(posting)을 부르는 posting 함수 즉, 저장된 글들을 불러온다. (볼 수 있게끔)
def posting(request, pk):
    
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)을 검색
    post = Post.objects.get(pk=pk)
    
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져온다.
    return render(request, 'main/posting.html', {'post': post})

def new_post(request):
    if request.method == "POST":
        if request.POST['contents']:
            new_article = Post.objects.create(  # 객체 생성 
                postname = request.POST['postname'],
                contents = request.POST['contents']
                )
    return render(request, 'main/new_post.html')
            