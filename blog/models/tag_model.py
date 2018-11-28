from django.db import models

class Tag(models.Model):
    word        = models.CharField(max_length=35)
    created_at  = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.word

    def __unicode__(self):
        return u'{w}'.format(w=self.word)
