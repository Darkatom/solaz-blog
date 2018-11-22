from django.shortcuts import render

from blog.models import BlogSettings, Post
from ..utils import *

def index_renderer(request, context):
    blog_data = BlogSettings.objects.get(pk=1)
    context['blog_title'] = blog_data.title
    return render(request,'blog/index.html', context)

def static_page_renderer(request, context):
    blog_data = BlogSettings.objects.get(pk=1)
    context['blog_title'] = blog_data.title
    return render(request, 'blog/static-page.html', context)
    
def dashboard_renderer(request, context):
    return render(request, 'blog/editor-dashboard.html', context)
  
def index(request):
    post_list = search(request, "search", [Post], ['post_title', 'post_body'])
    if post_list is None:
        post_list = Post.objects.all()

    post_list = list(filter(lambda p: p.published, post_list))
    post_list.sort(key=lambda p: p.pub_date, reverse=True)

    context = {
        'template_path': "./blog/posts/_post-index.html",
        'post_list': post_list
    }
    return index_renderer(request, context)
