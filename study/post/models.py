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
