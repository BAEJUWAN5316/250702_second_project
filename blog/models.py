from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    MUSIC_CHOICES = [
        ("track1", "music1"),
        ("track2", "music2"),
        ("track3", "music3"),
    ]

    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="blog/images/")
    music = models.CharField(max_length=20, choices=MUSIC_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id"]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id"]

