from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=40)
    content=models.TextField(max_length=2000)
    image=models.ImageField(upload_to='postpics/')
    time=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
