from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse

from blog.models import Post
from blog.forms import *
from blog.views.renderers import index_renderer, dashboard_renderer
from django.contrib.auth.decorators import login_required

def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
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
        'form': PostForm()
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
        'form': PostForm()
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