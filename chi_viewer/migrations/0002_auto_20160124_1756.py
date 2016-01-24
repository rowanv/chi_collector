# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chi_viewer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posting',
            name='time_written',
        ),
        migrations.AddField(
            model_name='posting',
            name='date_written',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 24, 17, 56, 22, 718831, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
