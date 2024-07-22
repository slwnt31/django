from django.db import models

# Create your models here.

# 글 작성 모델
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    
    def __str__(self):
        return self.postname
    # 안에 뭐가 쓰인지 모르는 post object 대신에 게시글의 제목인 postname으로 바꿈.
    
    