from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse

from blog.models import Post
from blog.forms import CommentForm
from blog.views.renderers import index_renderer

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
    