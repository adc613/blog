from django.db import models

# Create your models here.
class Entry(models.Model):
    article = models.TextField()
