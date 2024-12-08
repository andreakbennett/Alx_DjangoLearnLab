from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)  # Blog post title
    content = models.TextField()  # Blog post content
    published_date = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Many-to-one relation with User

    def __str__(self):
        return self.title

