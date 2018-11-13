from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    post_list = Post.objects.order_by('-pub_date')
    context = {
        'template_path': "./blog/posts/_post-index.html",
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context)

def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_list = post.comments
    print(comment_list)
    context = {
        'template_path': "./blog/posts/_post-view.html",
        'post': post,
        'comment_list': comment_list
    }
    return render(request, 'blog/index.html', context)