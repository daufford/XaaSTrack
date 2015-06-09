# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plaidaccount',
            name='name',
            field=models.CharField(max_length=50, blank=True, verbose_name='Account Name', null=True),
        ),
        migrations.AlterField(
            model_name='plaidtransaction',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
