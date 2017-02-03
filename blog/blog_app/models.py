from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Userprofile(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(default=10)
    imgs = models.ImageField(upload_to='images',blank=True)

    def __unicode__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=128,unique=True)
    content = models.TextField()
    author = models.ForeignKey(User)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    imgaes = models.ImageField(upload_to='blog_images',blank=True)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=200,unique=True)
    date = models.DateTimeField(auto_now=True)
    owner_blog = models.ForeignKey(Blog)
    publisher = models.CharField(max_length=200,unique=True)



