from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post (models.Model):
    pub_date = models.DateTimeField('date published')
    last_edit_date = models.DateTimeField('date last edited', null=True)
    published = models.BooleanField(default=False)
    
    post_title = models.CharField(max_length=200)
    post_summary = RichTextUploadingField(max_length=1000) #models.TextField(max_length=1000)
    post_body = RichTextUploadingField(max_length=25000) #models.TextField(max_length=25000)
    

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

    # -- Control
    
    def new(self, pub_date, published, title, text):
        self.pub_date = pub_date
        self.published = published
        self.post_title = title
        self.post_body = text
        self.post_summary = text[:993] + "...</p>"
        self.save()  

    def edit(self, edit_date, title, text):
        self.last_edit_date = edit_date
        self.post_title = title
        self.post_body = text
        self.post_summary = text[:993] + "...</p>"
        self.save()

    def publish(self):
        self.published = True
        self.save()
