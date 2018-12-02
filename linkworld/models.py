from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    text = models.TextField()
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=200, null=True)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    post = models.ForeignKey(
        to="Post", on_delete=models.CASCADE, null=True, related_name="comments")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Vote(models.Model):
    post = models.ForeignKey(
        to="Post", on_delete=models.CASCADE, null=True, related_name="votes")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="votes")
