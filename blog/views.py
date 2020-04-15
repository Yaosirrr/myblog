from django.shortcuts import get_object_or_404,render
from .models import Blog,BlogType
from django.contrib.contenttypes.models import ContentType
from read_statistics.utils import read_statistics_once_read
from comment.models import Comment
from datetime import datetime

# Create your views here.
def blog_list(request):
    context={}
    context['blogs'] = Blog.objects.all()
    context['blog_types'] = BlogType.objects.all()
    return render(request,'blog/blog_list.html',context)

def blog_detail(request,blog_pk):
    blog = get_object_or_404(Blog,pk=blog_pk)
    key = read_statistics_once_read(request,blog)
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type,object_id=blog.pk)
    context={}
    context['blog'] = get_object_or_404(Blog,id = blog_pk)
    context['previous_blog'] = Blog.objects.filter(created_time__gt=context['blog'].created_time).last() #or [-1]
    context['next_blog'] = Blog.objects.filter(created_time__lt=context['blog'].created_time).first() #or [0]
    context['user'] = request.user
    context['comments'] = comments
    response = render(request,'blog/blog_detail.html',context) #响应
    response.set_cookie(key,'true') #max_age=60, expires=datetime
    return response

def blogs_with_type(request,blog_type_pk):
    context={}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type']=blog_type
    context['blog_types'] = BlogType.objects.all()
    return render(request,'blog/blogs_with_type.html',context)

def blogs_with_date(request,year,month):
    pass
















