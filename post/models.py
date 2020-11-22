from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='game_img', default='default value')
    gameLink = models.CharField(max_length=500, default='add link')
    tags = TaggableManager(blank=True)
    favourite = models.ManyToManyField(User, related_name='favourite_post', null=True, blank=True)

    def __str__(self):
        return self.title


