from turtle import title
from django.db import models
from django.forms import CharField

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()

    def __str__(self):
        return self.title