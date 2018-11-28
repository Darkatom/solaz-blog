from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from .tag_model import Tag

class Post (models.Model):
    pub_date = models.DateTimeField('date published')
    last_edit_date = models.DateTimeField('date last edited', null=True)
    published = models.BooleanField(default=False)
    
    post_title = models.CharField(max_length=200)
    post_summary = RichTextUploadingField(max_length=1000) #models.TextField(max_length=1000)
    post_body = RichTextUploadingField(max_length=25000) #models.TextField(max_length=25000)
    
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        publication = self.pub_date.strftime('(%Y-%m-%d, %H:%M)')
        edit = self.last_edit_date.strftime('[%Y-%m-%d, %H:%M]')

        info = publication + " "
        if publication != edit:
            info += edit + " "
        
        if not self.published:
            info += "(Borrador) "

        info += self.post_title
        return info

    def __unicode__(self):
        return u'{t}/{b}'.format(t=self.post_title, b=self.post_body)

    def publish(self):
        self.published = True
        self.save()

    def get_tags(self):
        s = ""
        for tag in self.tags.all():
            s += " " + tag.word
        return s

    def get_tags_html(self):
        s = ""
        for tag in self.tags.all():
            s += '<p class="tag">' + tag.word + '</p>'
        return s