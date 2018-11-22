from django.contrib.auth.decorators import login_required
from django.shortcuts import (HttpResponseRedirect, get_object_or_404, render,
                              reverse)

from blog.forms import *
from blog.models import Comment, Post
from blog.views.renderers import dashboard_renderer, index_renderer


def new_comment(request, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(post_id)
            return HttpResponseRedirect(reverse('blog:post_view', kwargs={'post_id': post_id}))

    context = {
        'template_path': "./blog/posts/_post-view.html",
        'form': CommentForm()
    }
    return index_renderer(request, context)
     
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    context = {
        'template_path': "./blog/posts/_post-view.html",
    }
    return HttpResponseRedirect(reverse('blog:dashboard_comments'))

@login_required
def dashboard_post_delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    context = {
        'template_path': "./blog/posts/_post-view.html",
    }
    return HttpResponseRedirect(reverse('blog:dashboard_posts_with_post', kwargs={'post_id': post_id}))
