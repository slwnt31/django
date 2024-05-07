
from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.

def list(request):
    posts = Post.objects.all()
    return render(request,'main.html', {'posts':posts})

def write(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list')
    else:
        form=PostForm()
        return render(request,'write.html', {'form':form})
    
def show(request, post_id):
    post = get_object_or_404(Post, pk =post_id)
    return render(request, 'detail.html',{'post':post})
