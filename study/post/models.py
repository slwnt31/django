from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Image(models.Model):
    post=models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    image=models.ImageField(blank=True, upload_to="images/")