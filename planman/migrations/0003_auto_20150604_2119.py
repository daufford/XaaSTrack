# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planman', '0002_auto_20150604_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplan',
            name='user_description',
            field=models.CharField(verbose_name='Description', max_length=200, blank=True),
        ),
    ]
