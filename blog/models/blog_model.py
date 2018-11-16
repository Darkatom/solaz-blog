from django.db import models

class BlogSettings (models.Model):
    title = models.CharField(max_length=300)
    about_us = models.TextField(max_length=20000)
    about_this_blog = models.TextField(max_length=20000)
    contact_data = models.TextField(max_length=20000)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'{t}'.format(t=self.title)

    # -- Control
    
    def new(self, title, about_us, about_this_blog, contact_data):
        self.title = title
        self.about_us = about_us
        self.about_this_blog = about_this_blog
        self.contact_data = contact_data
        self.save()

    def save(self, *args, **kwargs):
        if BlogSettings.objects.exists() and not self.pk:
            return
        return super(BlogSettings, self).save(*args, **kwargs)