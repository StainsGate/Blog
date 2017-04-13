from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Userprofile(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(default=10)
    Logo = models.ImageField(upload_to='Logos',blank=True,default='images/logo.png')

    def __unicode__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=128,unique=True)
    content = models.TextField()
    author = models.ForeignKey(User)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    show_img = models.CharField(max_length=128,default='blog_images/default.jpg')
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(unique=True)
    date = models.DateTimeField(auto_now=True)
    owner_blog = models.ForeignKey(Blog)
    publisher = models.CharField(max_length=200)



