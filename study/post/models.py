from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    # writer는 django User model에 포함된 값만 저장될 수 있게 제약함.
    
    def __str__(self):
        return self.title
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    # Post에 있는 내용물을 불러올 영역(?)
    
    image_file = models.ImageField(null=True, upload_to="images/", blank=True)
    # 앞으로 업로드 될 사진을 담을 영역 (?)