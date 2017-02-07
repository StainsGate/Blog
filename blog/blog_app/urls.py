from django.conf.urls import url
from blog_app import views


urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^home/',views.home,name='home'),
    url(r'^edit_blog/',views.edit_blog,name='edit_blog'),
    url(r'^post/(?P<blog_id>.*)',views.posted,name='post'),
]