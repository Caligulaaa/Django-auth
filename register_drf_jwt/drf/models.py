
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    nickname = models.CharField(max_length=20)
    gender = models.CharField(max_length=6,choices=(('male','male'),('female','female')))
    address = models.TextField()
