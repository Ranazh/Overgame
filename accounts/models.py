from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from post.models import Post


class UserProfile(User):
    profile_pic = models.ImageField(upload_to='profile_img')
    profile_phone = models.CharField(max_length=12)

    def __str__(self):
        return self.username




