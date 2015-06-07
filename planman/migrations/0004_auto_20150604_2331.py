# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('planman', '0003_auto_20150604_2119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planpayments',
            old_name='planevent',
            new_name='event',
        ),
        migrations.AddField(
            model_name='planevent',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2015, 6, 5, 4, 31, 28, 740999, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planevent',
            name='event_type',
            field=models.CharField(max_length=8, choices=[(0, 'start'), (1, 'stop'), (2, 'renew'), (3, 'pay')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planpayments',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='planevent',
            name='user_description',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='planpayments',
            name='user_description',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='userplan',
            name='recurring_payment_months',
            field=models.PositiveSmallIntegerField(verbose_name='Recurring Payment Occurs every X Months', blank=True, default=1, null=True),
        ),
    ]
