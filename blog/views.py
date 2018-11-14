from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse

from .models import Post
from .forms import *

def index(request):
    post_list = Post.objects.order_by('-pub_date')
    context = {
        'template_path': "./blog/posts/_post-index.html",
        'post_list': post_list
    }
    return render(request,'blog/index.html', context)

def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_list = post.comments
    print(comment_list)
    context = {
        'template_path': "./blog/posts/_post-view.html",
        'post': post,
        'comment_list': comment_list,
        'form':CommentForm(request.POST)
    }
    return render(request, 'blog/index.html', context)

def new_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(post)
            
            return HttpResponseRedirect(reverse('blog:post_view', kwargs={'post_id': post.id}))

    context = {
        'template_path': "./blog/posts/_post-view.html",
        'form': CommentForm()
    }
    return render(request, 'blog/index.html', context)