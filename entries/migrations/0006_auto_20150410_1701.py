# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0005_entry_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='creation_date',
            field=models.DateTimeField( auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='last_modified',
            field=models.DateTimeField( auto_now=True),
            preserve_default=False,
        ),
    ]
