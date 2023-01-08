
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = models.CharField(max_length=150)
    is_verified = models.BooleanField(default=False)
    is_baned = models.BooleanField(default=False)
    otp = models.CharField(max_length=6,null=True,blank=True)


    # USERNAME_FIELD = 'username'

class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    nickname = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,choices=(('male','male'),('female','female')))
    address = models.TextField()


class TestFieldsForJwt(models.Model):
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title