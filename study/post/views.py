
from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def list(request):
    posts = Post.objects.all()
    return render(request,'main.html', {'posts':posts})

def write(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer=request.user
            post.save()
            return redirect('post:list')
    else:
        form=PostForm()
        return render(request,'write.html', {'form':form})
    
def show(request, post_id):
    post = get_object_or_404(Post, pk =post_id)
    return render(request, 'detail.html',{'post':post})

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