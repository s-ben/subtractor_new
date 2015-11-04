# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wait_time', models.DecimalField(max_digits=10, decimal_places=2)),
                ('line_pos', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='audio',
            name='user',
            field=models.ForeignKey(to='audio_process.User'),
        ),
    ]
