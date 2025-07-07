from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    trait = models.CharField(max_length=25, blank=True, null=True)

