# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_auto_20150410_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='article',
            field=models.TextField(default=b'nothing'),
        ),
    ]
