# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('event_type', models.CharField(choices=[('pay', 'pay'), ('start', 'start'), ('stop', 'stop'), ('renew', 'renew')], max_length=8)),
                ('event_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=10)),
                ('user_description', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('user_description', models.CharField(verbose_name='Description', help_text='form help text', max_length=200, blank=True)),
                ('planprovider_text', models.CharField(verbose_name='Service Provider', max_length=200)),
                ('notes', models.TextField(verbose_name='Notes', blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('next_renewal_date', models.DateField(null=True, blank=True)),
                ('expiration_date', models.DateField(null=True, blank=True)),
                ('last_payment_date', models.DateField(null=True, blank=True)),
                ('next_payment_date', models.DateField(null=True, blank=True)),
                ('has_recurring_payment', models.BooleanField(verbose_name='Has Recurring Payments?', default=False)),
                ('recurring_payment_amount', models.DecimalField(verbose_name='Recurring Payment Amount', null=True, decimal_places=2, blank=True, max_digits=10)),
                ('recurring_payment_months', models.PositiveSmallIntegerField(verbose_name='Recurring Payment Occurs every X Months', null=True, blank=True, default=1)),
                ('planprovider_key', models.ForeignKey(verbose_name='*service provider _ key', null=True, to='planman.PlanProvider', blank=True, on_delete=django.db.models.deletion.SET_NULL)),
                ('user', models.ForeignKey(verbose_name='*useraccount', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('lastsync', models.DateTimeField(verbose_name='Last time user loaded transactions', null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='planevent',
            name='userplan',
            field=models.ForeignKey(to='planman.UserPlan'),
        ),
    ]
