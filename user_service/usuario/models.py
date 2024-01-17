from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=True)
    id_user = models.IntegerField(null=True)
    # bio = models.TextField(blank=True)
    profileimage = models.ImageField(
        upload_to='profile_images', default='do-utilizador.png')
    # location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    
class Follower(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user