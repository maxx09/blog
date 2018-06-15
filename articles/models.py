from django.db import models
from django.conf import settings


class TimeStamp(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStamp):

    category_name = models.CharField(max_length=10)

    def __str__(self):
        return self.category_name

class Post(TimeStamp):

    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    category = models.ForeignKey(Category)

    class Meta:
        ordering = ['-id']


class Comment(TimeStamp):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    message = models.TextField()

