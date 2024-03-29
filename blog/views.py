from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all()
    # blogs = Blog.objects.order_by('-date')[:1]
    return render(request,'blog/all_blogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request,'blog/detail.html',{'id':blog_id,'blog':blog})
