from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')

    def __str__(self):
        return self.title
