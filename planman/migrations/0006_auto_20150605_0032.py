# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planman', '0005_planevent_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planpayments',
            name='event',
        ),
        migrations.AlterField(
            model_name='planevent',
            name='event_type',
            field=models.CharField(choices=[(0, 'pay'), (1, 'start'), (2, 'stop'), (3, 'renew')], max_length=8),
        ),
        migrations.DeleteModel(
            name='PlanPayments',
        ),
    ]
