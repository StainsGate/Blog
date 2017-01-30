from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Userprofile(models.Model):
    user = models.OneToOneField(User)
    images = models.ImageField(upload_to= user.username+'_imgaes',blank=True)
    authority = models.IntegerField(default=0)


    def __unicode__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=128,unique=True)
    content = models.CharField(unique=True)
    author = models.ForeignKey(Userprofile)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=1000,unique=True)
    date = models.DateField()
    owner_blog = models.ForeignKey(Blog)
    publisher = models.CharField(unique=True)



