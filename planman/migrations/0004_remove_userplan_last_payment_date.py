# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planman', '0003_userplan_last_payment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userplan',
            name='last_payment_date',
        ),
    ]
