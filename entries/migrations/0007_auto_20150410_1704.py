# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0006_auto_20150410_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
