from django.db import models
from .post_model import Post

class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    text = models.TextField(max_length=5000)

    def __str__(self):
        return self.pub_date.strftime('(%Y-%m-%d, %H:%M)') + " " + self.text

    def __unicode__(self):
        return u'{t}'.format(t=self.text)

    # -- Control
    
    def new(self, author, post, pub_date, text):
        self.author = author
        self.post = post
        self.pub_date = pub_date
        self.text = text
        self.save()  
