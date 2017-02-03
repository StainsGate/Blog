from django.shortcuts import render
from django.http import HttpResponse
from blog_app.models import  Blog


# Create your views here.

def index(request):
    lastest_blogs = Blog.objects.order_by('-date')[:3]
    context_dict = {'blog_list':lastest_blogs}
    return render(request,'blogs/index.html',context_dict)


def home(request):
    return render(request,'blogs/home.html')