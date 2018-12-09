from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *

import hashlib
import datetime

class PostForm(forms.ModelForm):
    post_title = forms.CharField(required=True, label='Título', max_length=200)
    post_body = forms.CharField(required=True, label='Texto', max_length=25000, widget=CKEditorUploadingWidget)
    published = forms.BooleanField(required=False, widget=forms.CheckboxInput)

    tags = forms.ModelMultipleChoiceField(required=False, queryset=Tag.objects.all())

    _newly_created: bool

    class Meta:
        model = Post
        fields = ['post_title', 'post_body', 'published', 'tags']

    def __init__(self, *args, **kwargs):
        self._newly_created = kwargs.get('instance') is None
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        title = self.cleaned_data["post_title"]
        post_body = self.cleaned_data["post_body"]

        if self._newly_created:
            post.pub_date = datetime.datetime.now()
        else:
            post.last_edit_date = datetime.datetime.now()

        post.post_title = title
        post.post_body = post_body
        post.post_summary = post_body[:997] + "..."

        if commit:
            post.save()
            post.tags.set(self.cleaned_data["tags"])
            post.save()

        return post

class CommentForm(forms.ModelForm):
    author = forms.CharField(required=True, label='Tu nombre', max_length=20)
    text = forms.CharField(required=True, label='Tu comentario', max_length=5000, widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['author', 'text']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

    def save(self, post_id, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        comment.post = Post.objects.get(pk=post_id)
        comment.author = self.cleaned_data["author"]
        comment.pub_date = datetime.datetime.now()
        comment.text = self.cleaned_data["text"]

        if commit:
            comment.save()
        return 
        
class BlogAboutForm(forms.ModelForm):
    about = forms.CharField(required=True, label='', max_length=20000, widget=CKEditorUploadingWidget)

    class Meta:
        model = BlogSettings
        fields = ['about']

    def __init__(self, *args, **kwargs):
        super(BlogAboutForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        blog = super(BlogAboutForm, self).save(commit=False)
        blog.about = self.cleaned_data["about"]

        if commit:
            blog.save()
               
        return blog


class BlogContactForm(forms.ModelForm):
    contact_data = forms.CharField(required=True, label='', max_length=20000, widget=CKEditorUploadingWidget)

    class Meta:
        model = BlogSettings
        fields = ['contact_data']

    def __init__(self, *args, **kwargs):
        super(BlogContactForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        blog = super(BlogContactForm, self).save(commit=False)
        blog.contact_data = self.cleaned_data["contact_data"]

        if commit:
            blog.save()
               
        return blog

