from django.db import models

# Create your models here.
class Entry(models.Model):
    article = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField( auto_now=True)
    author = models.ForeignKey('accounts.User')
    title = models.CharField(max_length=255)
