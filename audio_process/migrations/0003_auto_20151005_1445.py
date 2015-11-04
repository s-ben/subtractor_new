# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio_process', '0002_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='line_pos',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wait_time',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
    ]
