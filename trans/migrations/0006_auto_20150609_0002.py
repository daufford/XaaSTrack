# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0005_auto_20150609_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plaidtransaction',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
