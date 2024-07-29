from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .models import PostImage
from .forms import PostForm
# Create your views here.

# request는 현재 상황을 의미한다.

def list(request):
    posts = Post.objects.all() # db에 있는 모든 것을 불러옴, 변수에.
    return render(request,'main.html', {'posts':posts})
    # posts란 변수에 모든 걸 담아서 main.html에 불러옴.

@login_required
def write(request):
    if request.method=='POST': #폼에 무언가 작성했을 때
        form=PostForm(request.POST)
        # form이라는 변수에 PostForm에 담긴 글들(정보들) 담겠다는 의미.
        
        images = request.FILES.getlist('image')
        # write.html에서 유저가 업로드한 사진 파일들을 list 형식으로 바꿔준다.
        
        if form.is_valid(): # 빈 게시물이 아닌지를 확인하기 위함.
            post = form.save(commit=False)
            post.writer = request.user
            # writer를 정의해두고 아무것도 담아주지 않으니 뭘 띄워야 할지도 모르는
            # 오류가 뜸. writer에 django db에 있는 user 정보를 담아줘야 한다.
            post.save()
            # 지금 post엔 작성자가 적은 제목, 내용, 작성일, 작성자가 담겨 있다. (db에 저장)
            
            for i in images:
                PostImage.objects.create(post=post, image_file=i) 
            return redirect('post:list')
    else:
        form=PostForm()
        return render(request,'write.html', {'form':form})
    #GET으로 새 글 양식을 준다.
    
def show(request, post_id):
    post = get_object_or_404(Post, pk =post_id)
    image_file=PostImage.objects.filter(post=post)
    return render(request, 'detail.html',{'post':post, 'image_file':image_file})

def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # form.save : 입력된 데이터를 db에 바로 저장함.
            # form.save(commit=False) : 입력된 데이터를 바로 db에 저장하지 않고, 메모리에만 저장한다0.
            
            post.save()
            return redirect('/show/<int:post_id>') 
        # 글의 수정사항을 모두 입력하고 제출을 눌렀을 경우!!!! 수정하고 -> detail.html 로 돌아가기   
    
    else: # GET일 때 수정 html로 이동해 수정 후 제출한 다음, 위 POST일 경우의 루트를 탄다.
        form = PostForm() # 기존의 forms.py에서 형식을 가져온다.
    return render(request, post/edit.html, {'form':form})