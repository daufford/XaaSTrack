# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planman', '0006_auto_20150605_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planevent',
            name='event_type',
            field=models.CharField(choices=[('pay', 'pay'), ('start', 'start'), ('stop', 'stop'), ('renew', 'renew')], max_length=8),
        ),
    ]
