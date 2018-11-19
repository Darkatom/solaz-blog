from django.shortcuts import render

from blog.models import BlogSettings, Post
from blog.views.renderers import static_page_renderer

def about(request):
    blog = BlogSettings.objects.get(pk=1)
    return static_page_renderer(request, {'page_text': blog.about})

def contact(request):
    blog = BlogSettings.objects.get(pk=1)
    return static_page_renderer(request, {'page_text': blog.contact})
