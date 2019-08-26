from django.db import models
from django.utils import timezone
from ACCOUNTS.models import User
from django.urls import reverse


class BlogPost(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='blog_images',blank=True,null=True)

    def __str_(self):
        return self.title