
from django.shortcuts import render,redirect, get_object_or_404
from .models import Post, Image, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.db.models import Q
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
    comments = post.comment_set.all()  
    commentForm = CommentForm() 
    context = {
        'post': post,
        'images': images,
        'comments': comments,
        'commentForm': commentForm, 
    }
    return render(request, 'detail.html', context)

    # commentForm=CommentForm()
    # comment=get_object_or_404(Comment, pk=post_id)
    # return render(request, 'detail.html',
    # {'post':post, 'images':images, 'commentForm':commentForm})

# def update(request, pk):
#     post=Post.objects.get(id=pk)
#     if request.method=="POST":
#         post.title=request.POST['title']
#         post.content=request.POST['content']
#         post.writer=request.POST['writer']
        
#         post.save()
#         return redirect('post')
#     else:
#         postForm=PostForm
#         return render(request, updated.html)

@login_required(login_url='/accounts/home/login')
def deleteget(request, post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return redirect('post:list')

    # if request.user==post.writer:
    #     if request.method=='POST':
    #         post.delete()
    #         return redirect('/')
    #     return render(request, 'delete.html', {'post':post})
    
    #     return redirect('post:show')
    # else:
    #     post.delete()
    #     return redirect('post:list')

def updateget(request, post_id):
    post=Post.objects.get(id=post_id)
    if request.method=='POST':
        postForm=PostForm(request.POST, request.FILES, instance=post)
        if postForm.is_valid():
            post=postForm.save(commit=False)
            post.modify_date=timezone.now()
            post.save()
            return redirect('/show/'+str(post_id), {'post':post})
    else:
        postForm=PostForm(instance=post)
        return render(request, 'updated.html', {'post':post})                
            
        # if request.method=='POST':
        #     postForm=PostForm(request.POST, request.FILES, instance=post)
        #     if postForm.is_valid(): #수정글 다 작성해서 저장할때
        #         post=postForm.save(commit=False)
        #         post.save()
        #         # return redirect(''+str(bid))
        #         return render(request, 'post:show', post_id )
        # else:
        #     postForm=PostForm(instance=post)
        # return render('post:') #수정버튼 눌렀을 때

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        post=Post.objects.get(pk=pk)
        commentForm=CommentForm(request.POST)
        if commentForm.is_valid():
            comment=commentForm.save(commit=False)
            comment.post=post
            comment.writer=request.user
            comment.save()
        return redirect('post:show', pk)
    return redirect('accounts/home/login')
    
@require_POST
def comments_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.writer:
            comment.delete()
    return redirect('post:show', pk)

    # if request.users.is_authenticated:
    #     comment=get_object_or_404(Comment, pk=comment_pk)
    #     if request.user==comment.writer:
    #         comment.delete()
    # return redirect('post:show', post_pk)

@require_POST
def likes(request, post_pk):
    if request.user.is_authenticated:
        post=get_object_or_404(Post, pk=post_pk)
        if post.like_users.filter(pk=request.user.pk).exists():
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
        return redirect('post:show', post_pk)
    return redirect('accounts/home/login')

# def search(request):
#         if request.method == 'POST':
#                 searched = request.POST['searched']
#                 # 검색창에 입력된 내용을 searched에 받음
#                 post1 = Post.objects.filter(name__contains=searched)
#                 # 그리고 그 변수가 데이터베이스에 사용자가 검색한 내용이 포함된 object에 있는지 찾아서
#                 # 찾은 내용을 post1에 담아 searched.html 페이지에 딕셔너리 형태로 반환해줌.
#                 context = {
#                     'searched':searched,
#                     'post1':post1
#                 }
#                 ret'searched':searchedurn render(request, 'searched.html', context)
#         else: # POST 방식이 아닐 경우, 빈 딕셔너리를 searched.html에 반환해줌.
#                 return render(request, 'searched.html', {})
#             #  request.POST[''] 안에 있는 searched는 검색창을 구현했던 nav 부분에서 
#             #  form 태그의 input 태그에 있는 name=searched의 searched를 의미합니다.


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(Q(title=searched) | Q(content=searched))
        
    context = {
        'searched':searched,
        'posts':posts
    }    
    
    return render(request, 'search.html', context)