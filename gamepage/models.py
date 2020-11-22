from django.db import models
from accounts.models import UserProfile


# Create your models here.

class GamePage(models.Model):
    gameTitle = models.CharField(max_length=255)
    text = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.gameTitle
