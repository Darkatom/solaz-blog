from django.contrib import admin

from .models import Post, Comment, BlogSettings

admin.site.register(BlogSettings)
admin.site.register(Post)
admin.site.register(Comment)