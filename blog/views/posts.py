from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse

from blog.models import Post
from blog.forms import *
from blog.views.renderers import *
from django.contrib.auth.decorators import login_required

from ..utils import *

def post_list(request):
    post_list = search(request, "search", [Post], ['post_title', 'post_body'])
    if post_list is None:
        post_list = Post.objects.all()

    post_list = list(filter(lambda p: p.published, post_list))
    post_list.sort(key=lambda p: p.pub_date, reverse=True)

    return index(request, post_list)

def tag_search(request, tag):
    # TO-DO
    post_list = search(request, "search", [Post], ['post_title', 'post_body'])
    if post_list is None:
        post_list = Post.objects.all()

    post_list = list(filter(lambda p: p.published, post_list))
    post_list.sort(key=lambda p: p.pub_date, reverse=True)

    return index(request, post_list)


def post_view(request, post_id):
    if request.GET:
        return post_list(request)

    post = get_object_or_404(Post, pk=post_id)
    if not post.published:
        return HttpResponseRedirect(reverse('blog:index'))

    comment_list = post.comments
    
    context = {
        'template_path': "./blog/posts/_post-view.html",
        'post': post,
        'comment_list': comment_list,
        'form': CommentForm(request.POST)
    }
    return index_renderer(request, context)

@login_required       
def new_post(request):
    context = {
        'template_path': "./blog/posts/_new-post-form.html",
        'form': PostForm(),
        'posts': True
    }

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:dashboard_posts'))
    return dashboard_renderer(request, context)

@login_required          
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'template_path': "./blog/posts/_edit-post-form.html",
        'post_id': post_id,
        'form': PostForm(),
        'posts': True
    }

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:dashboard_posts'))
        else:
            context['form'] = form
    else:
        context['form'] = PostForm(instance=post)

    return dashboard_renderer(request, context)

@login_required        
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('blog:dashboard_posts'))

@login_required
def publish_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.publish()
    return HttpResponseRedirect(reverse('blog:dashboard_posts'))