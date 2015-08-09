from django.db import models
from datetime import datetime

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=255)
    article = models.TextField(default="nothing")
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey('accounts.User', null=True)
    image = models.ImageField()

    def __str__(self):
        return u'%s' % (self.title)

    def get_date(self):
        year = self.creation_date.year
        month = self.creation_date.month
        day = self.creation_date.day

        month_converter_dic = [
                'error',
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'December'
                ]

        date = month_converter_dic[month] + ', ' + str(day) + ' ' + str(year)

        return date
