from django.db import models

class Post (models.Model):
    pub_date = models.DateTimeField('date published')
    last_edit_date = models.DateTimeField('date last edited')
    post_title = models.CharField(max_length=200)

    post_summary = models.TextField(max_length=1000)
    post_body = models.TextField(max_length=25000)

    def __str__(self):
        publication = self.pub_date.strftime('(%Y-%m-%d, %H:%M)')
        edit = self.last_edit_date.strftime('[%Y-%m-%d, %H:%M]')

        if publication == edit:
            return publication + " " + self.post_title
        
        return publication + " " + edit + " " + self.post_title

    def __unicode__(self):
        return u'{t}/{b}'.format(t=self.post_title, b=self.post_body)

    # -- Control
    
    def new(self, pub_date, text):
        self.pub_date = pub_date
        self.post_body = text
        self.post_summary = text[:997] + "..."
        self.save()  

    def edit(self, edit_date, text):
        self.last_edit_date = edit_date
        self.post_body = text
        self.post_summary = text[:997] + "..."
        self.save()

