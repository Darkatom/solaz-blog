from django import forms

from .models import *

import hashlib
import datetime

class CommentForm(forms.Form):
    author = forms.CharField(required=True, label='Your name', max_length=20)
    text = forms.CharField(required=True, label='Your comment', max_length=5000, widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ("post", "author", "publication date", "text")

    def save(self, post, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        comment.post = post
        comment.author = self.cleaned_data["author"]
        comment.pub_date = datetime.datetime.now
        comment.text = self.cleaned_data["text"]

        if commit:
            comment.save()
        return comment