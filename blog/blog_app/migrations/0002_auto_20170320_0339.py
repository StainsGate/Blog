# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-03-20 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='show_img',
            field=models.CharField(default='blog_images/default.jpg', max_length=128),
        ),
        migrations.AlterField(
            model_name='comment',
            name='publisher',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Logo',
            field=models.ImageField(blank=True, default='images/logo.png', upload_to='Logos'),
        ),
    ]
