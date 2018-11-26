from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class BlogSettings (models.Model):
    title = models.CharField(max_length=300)
    about = RichTextUploadingField()
    contact_data = RichTextUploadingField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'{t}'.format(t=self.title)

    # -- Control
    
    def new(self, title, about, contact_data):
        self.title = title
        self.about = about
        self.contact_data = contact_data
        self.save()

    def save(self, *args, **kwargs):
        if BlogSettings.objects.exists() and not self.pk:
            return
        return super(BlogSettings, self).save(*args, **kwargs)