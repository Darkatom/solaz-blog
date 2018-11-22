from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse

from blog.models import Post, Comment
from blog.forms import *
from blog.views.renderers import index_renderer, dashboard_renderer
from django.contrib.auth.decorators import login_required

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