# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0010_entry_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(default=datetime.datetime(2015, 7, 28, 15, 32, 11, 67559, tzinfo=utc), upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='article',
            field=models.TextField(default='nothing'),
        ),
    ]
