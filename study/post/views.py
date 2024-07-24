from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.

def list(request):
    posts = Post.objects.all()
    return render(request,'main.html', {'posts':posts})

def write(request):
    if request.method=='POST': #폼에다가 뭘 작성했을 때
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            # writer를 정의해두고 아무것도 담아주지 않으니 뭘 띄워야 할지도 모르는
            # 오류가 뜸. writer에 django db에 있는 user 정보를 담아줘야 한다.
            post.save()
            return redirect('post:list')
    else:
        form=PostForm()
        return render(request,'write.html', {'form':form})
    
def show(request, post_id):
    post = get_object_or_404(Post, pk =post_id)
    return render(request, 'detail.html',{'post':post})
