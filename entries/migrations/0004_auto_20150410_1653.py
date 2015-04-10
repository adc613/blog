# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20150410_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='article',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='author',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='last_updated',
        ),
    ]
