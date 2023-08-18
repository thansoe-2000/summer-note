from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
# Create your models here.


class Category(models.Model):
     name = models.CharField(max_length=250)
     description = models.TextField(null=True, blank=True)
     status = models.IntegerField(default=1)
     date_added = models.DateTimeField(default=timezone.now)
     date_updated = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.name

class Post(models.Model):
     category = models.ForeignKey(Category, on_delete=models.CASCADE)
     title = models.CharField(max_length=100, null=True, blank=True)
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     blog_post = models.TextField(blank=True, null=True)
     image = models.ImageField(null=True, blank=True, upload_to='images')
     status = models.IntegerField(default=0)
     date_added = models.DateTimeField(default=timezone.now)
     date_updated = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.title + " - " + self.category.name