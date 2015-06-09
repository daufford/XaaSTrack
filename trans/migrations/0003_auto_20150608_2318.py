# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0002_auto_20150608_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plaidaccount',
            name='id',
        ),
        migrations.AlterField(
            model_name='plaidaccount',
            name='_id',
            field=models.CharField(serialize=False, max_length=50, primary_key=True, verbose_name='Plaids _id Field'),
        ),
    ]
