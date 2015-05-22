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
            name='provider',
        ),
        migrations.AddField(
            model_name='userplan',
            name='planprovider',
            field=models.ForeignKey(default=1, verbose_name='provider of this service', to='planman.PlanProvider'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userplan',
            name='userprofile',
            field=models.ForeignKey(verbose_name='user/owner', to='planman.UserProfile'),
        ),
    ]
