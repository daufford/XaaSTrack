# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planman', '0002_auto_20150611_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='userplan',
            name='last_payment_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
