from django.contrib import admin
from blog_app.models import Blog,Comment,Userprofile
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title','author','date','views')



admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
admin.site.register(Userprofile)