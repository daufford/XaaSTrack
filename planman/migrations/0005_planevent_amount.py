# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planman', '0004_auto_20150604_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='planevent',
            name='amount',
            field=models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2),
        ),
    ]
