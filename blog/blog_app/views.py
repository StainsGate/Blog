#coding: utf-8
from django.shortcuts import render
from blog_app.models import Blog,Comment
from django.http import  HttpResponseRedirect
from django.contrib.auth import get_user
from blog_app.form import BlogForm,CommentForm
import re

# Create your views here.

def index(request):
    lastest_blogs = Blog.objects.order_by('-date')[:3]
    context_dict = {'blog_list':lastest_blogs}
    return render(request,'blogs/index.html',context_dict)


def posted(request,blog_id):
    context_dict = {}
    if request.method == 'POST':
        try:
            blog = Blog.objects.get(id=blog_id)
            context_dict['blog'] = blog

            # new_comment = CommentForm(data=request.POST)
            # if new_comment.is_valid():
            #     comment = new_comment.save(commit=False)
            #     comment.owner_blog = blog
            #     comment.save()
            # else:
            #     print new_comment.errors

            # publisher = request.POST.get('publisher')
            content = request.POST.get('content')
            new_comment = Comment()
            if new_comment:
                name = get_user(request).get_username()
                if name:
                     new_comment.publisher = name
                else:
                    new_comment.publisher = "游客"
                new_comment.content = content
                new_comment.owner_blog = blog
                new_comment.save()
            else:
                print new_comment.errors

            comments = Comment.objects.filter(owner_blog_id=blog_id)
            context_dict['comments'] = comments

            return render(request,'blogs/posted.html',context_dict)


        except Comment.DoesNotExist:
            pass

    else:
        try:
            blog = Blog.objects.get(id=blog_id)
            context_dict['blog'] = blog

            comments = Comment.objects.filter(owner_blog_id=blog_id)
            context_dict['comments'] = comments

        except Comment.DoesNotExist:
            pass

        finally:
            return render(request,'blogs/posted.html',context_dict)

def edit_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            user = get_user(request)
            blog = form.save(commit=False)
            blog.author = user
            img_url =re.search(r'django.*.jpg',blog.content)
            if img_url:
                img_src = img_url.group(0)
                blog.show_img = img_src
                blog.save()
            else:
                blog.save()
            return HttpResponseRedirect('/blog/index/')
        else:
            return HttpResponseRedirect('/blog/home/')
    else:
        form = BlogForm()
        return render(request,'blogs/edit.html',{'form':form})

def edit_comlete(request):
    return render(request,'blogs/posted.html')

def home(request):
    return render(request,'blogs/home.html')