from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,unique=True, on_delete = models.CASCADE)
    bio=models.CharField(max_length=1000)
    name=models.CharField(max_length=30)
    created=models.DateTimeField(default=timezone.now)
    dp=models.ImageField(upload_to='propics',default='default.jpg')
    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
    


