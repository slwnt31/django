
from django.shortcuts import render,redirect, get_object_or_404
from .models import Post, Image
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def list(request):
    posts = Post.objects.all()
    return render(request,'main.html', {'posts':posts})

def write(request): #새 글 폼 띄워줌, 게시글 저장
    #post랑 get의 차이: post는 비밀화되어있는 정보들 get은 주소창에 그대로 정보가 뜬다.
    #get은 비어있는 느낌, post는 꽉 차있는 느낌
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer=request.user
            post.save()
            
            for img in request.FILES.getlist('image',None):
                Image.objects.create(post=post, image=img)
                
            return redirect('post:list')
    else:
        form=PostForm() #request는 현재 상황인데 없으니까 아예 새 포스트를 불러옴
        return render(request,'write.html', {'form':form})
    
def show(request, post_id):
    post = get_object_or_404(Post, pk =post_id)
    images=Image.objects.filter(post=post)
    return render(request, 'detail.html',
    {'post':post, 'images':images})

@login_required
def deleteget(request, bid):
    post=Post.objects.get(id=bid)
    if request.user!=post.writer:
        return redirect('')
    else:
        post.delete()
        return redirect('')
    # return redirect()

def updateget(request, post_id):
    post=Post.objects.get(pk=post_id)
    if request.method=='POST':
        postForm=PostForm(request.POST, instance=post)
        if postForm.is_valid(): #수정글 다 작성해서 저장할때
            post=postForm.save(commit=False)
            post.save()
            # return redirect(''+str(bid))
            return render(request, 'post:show', post_id )
    else:
        postForm=PostForm(instance=post)
    return render('post:') #수정버튼 눌렀을 때
