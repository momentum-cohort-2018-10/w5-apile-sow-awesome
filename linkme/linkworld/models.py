from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.CharField(max_length=255)
    url = models.URLField()


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(to="Post", on_delete=models.CASCADE)


class Vote(models.Model):

    post = models.ForeignKey(to="Post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.BooleanField(default=False)
