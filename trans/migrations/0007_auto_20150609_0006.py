# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0006_auto_20150609_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plaidtransaction',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
