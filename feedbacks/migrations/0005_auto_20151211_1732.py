# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0004_auto_20151211_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
