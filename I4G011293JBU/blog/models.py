import imp
from time import timezone
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + " | " + str(self.author)