import os

os.environ.setdefault('DJANGO_SETTING_MODULE','blog.setting')

import django
django.setup()


from blog_app.models import  Blog, Comment

