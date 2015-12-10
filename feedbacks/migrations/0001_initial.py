# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('from_email', models.EmailField(max_length=75)),
                ('create_date', models.DateField(default=datetime.datetime(2015, 12, 10, 17, 15, 23, 363137))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
