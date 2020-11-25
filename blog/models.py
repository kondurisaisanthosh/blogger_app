from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from users.models import Profile


class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    # time and date at which it is created but can change dates
    date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    # last modified date
    # date =models.DateTimeField(auto_now=true)
    # time and date at which it is created
    # date=models.DateTimeField(auto_now_add=true)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})