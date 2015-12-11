# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0003_auto_20151211_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 11, 17, 12, 57, 151844)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.CharField(max_length=255),
        ),
    ]
