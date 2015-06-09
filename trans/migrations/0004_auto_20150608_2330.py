# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0003_auto_20150608_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='plaidaccount',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, default=1, verbose_name='ID', serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plaidaccount',
            name='_id',
            field=models.CharField(max_length=50),
        ),
    ]
