# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0004_auto_20150608_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='plaidtransaction',
            name='meta',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='plaidtransaction',
            name='meta_score',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
