# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('source', models.CharField(max_length=300)),
                ('summary', models.TextField()),
                ('score', models.PositiveIntegerField()),
                ('link', models.CharField(max_length=300)),
                ('time_written', models.TimeField()),
                ('will_apply', models.BooleanField(default=False)),
                ('applied', models.BooleanField(default=False)),
            ],
        ),
    ]
