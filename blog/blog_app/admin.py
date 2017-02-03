from django.contrib import admin
from blog_app.models import Blog,Comment,Userprofile

# Register your models here.


admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Userprofile)