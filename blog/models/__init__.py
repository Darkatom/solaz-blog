# Import here all your models
from .post_model import Post
from .comment_model import Comment
from .tag_model import Tag
from .blog_model import BlogSettings

__all__ = [ 'Post', 'Comment', 'Tag', 'BlogSettings']
