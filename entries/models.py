from django.db import models
from datetime import datetime

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=255)
    article = models.TextField(default="nothing")
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey('accounts.User', null=True)

    def __unicode__(self):
        return u'%s' % (self.title)

