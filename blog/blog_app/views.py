from django.shortcuts import render
from blog_app.models import Blog,Comment


# Create your views here.

def index(request):
    lastest_blogs = Blog.objects.order_by('-date')[:3]
    context_dict = {'blog_list':lastest_blogs}
    return render(request,'blogs/index.html',context_dict)


def posted(request,blog_id):
    context_dict = {}

    try:
        blog = Blog.objects.get(id=blog_id)
        context_dict['blog'] = blog

        comments = Comment.objects.get(owner_blog_id=blog_id)
        context_dict['comments'] = comments

    except Comment.DoesNotExist:
        pass

    finally:
        return render(request,'blogs/posted.html',context_dict)




def home(request):
    return render(request,'blogs/home.html')