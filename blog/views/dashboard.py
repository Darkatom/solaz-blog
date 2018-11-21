
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse

from blog.models import Post, Comment, BlogSettings
from blog.views.renderers import dashboard_renderer
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_posts(request):
    context = {
        'template_path': "./blog/posts/_editor-post-list.html",
        'post_list': Post.objects.all()
    }
    return dashboard_renderer(request, context)
    
@login_required
def dashboard_comments(request):
    context = {
        'template_path': "./blog/comments/_editor-comment-list.html",
        'comment_list': Comment.objects.all()
    }
    return dashboard_renderer(request, context)
    
@login_required
def dashboard_static(request):
    context = {
        'template_path': "./blog/statics/_editor-static-list.html",
    }
    return dashboard_renderer(request, context)

@login_required
def dashboard_page(request):
    context = {
        'template_path': "",
    }
    return dashboard_renderer(request, context)