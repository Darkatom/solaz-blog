
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse

from blog.models import Post, Comment, BlogSettings
from blog.views.renderers import dashboard_renderer
from django.contrib.auth.decorators import login_required

from ..utils import *

@login_required
def dashboard_posts(request):
    post_list = search(request, "search", [Post], ['post_title', 'post_body'])
    if post_list is None:
        post_list = Post.objects.all()

    post_list = list(filter(lambda p: p.published, post_list))
    post_list.sort(key=lambda p: p.pub_date, reverse=True)

    context = {
        'template_path': "./blog/posts/_editor-post-list.html",
        'post_list': post_list,
        'posts': True
    }
    return dashboard_renderer(request, context)
    
@login_required
def dashboard_posts_with_post(request, post_id):
    post_list = search(request, "search", [Post], ['post_title', 'post_body'])
    if post_list is None:
        post_list = Post.objects.all()

    post_list = list(filter(lambda p: p.published, post_list))
    post_list.sort(key=lambda p: p.pub_date, reverse=True)

    selected_post = get_object_or_404(Post, pk=post_id)

    context = {
        'template_path': "./blog/posts/_editor-post-list.html",
        'post_list': post_list,
        'post': selected_post,
        'posts': True
    }
    return dashboard_renderer(request, context)
    
@login_required
def dashboard_comments(request):
    comment_list = search(request, "search", [Post], ['author', 'text', 'post__post_title', 'post__post_body'])
    if comment_list is None:
        comment_list = Post.objects.all()

    comment_list = list(filter(lambda p: p.published, comment_list))
    comment_list.sort(key=lambda p: p.pub_date, reverse=True)

    context = {
        'template_path': "./blog/comments/_editor-comment-list.html",
        'commcomment_listent_list': Comment.objects.all(),
        'comments': True
    }
    return dashboard_renderer(request, context)
    
@login_required
def dashboard_static(request):
    context = {
        'template_path': "./blog/statics/_editor-static-list.html",
        'statics': True
    }
    return dashboard_renderer(request, context)

@login_required
def dashboard_page(request):
    context = {
        'template_path': "",
    }
    return dashboard_renderer(request, context)