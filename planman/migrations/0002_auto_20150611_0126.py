# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planman', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userplan',
            name='last_payment_date',
        ),
        migrations.AlterField(
            model_name='userplan',
            name='user_description',
            field=models.CharField(help_text='Additional description (optional)', max_length=200, blank=True, verbose_name='Description'),
        ),
    ]
