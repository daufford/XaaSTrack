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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('user_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PlanPayments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('user_description', models.CharField(max_length=200)),
                ('planevent', models.ForeignKey(to='planman.PlanEvent')),
            ],
        ),
        migrations.CreateModel(
            name='PlanProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('user_description', models.CharField(verbose_name='Description', max_length=200)),
                ('planprovider_text', models.CharField(verbose_name='Service Provider', max_length=200)),
                ('notes', models.TextField(verbose_name='Notes', blank=True)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('next_renewal_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('last_payment_date', models.DateField(blank=True, null=True)),
                ('next_payment_date', models.DateField(blank=True, null=True)),
                ('has_recurring_payment', models.BooleanField(verbose_name='Has Recurring Payments?', default=False)),
                ('recurring_payment_amount', models.DecimalField(verbose_name='Recurring Payment Amount', decimal_places=2, blank=True, null=True, max_digits=10)),
                ('recurring_payment_months', models.PositiveSmallIntegerField(verbose_name='Recurring Payment Occurs every X Months', blank=True, null=True)),
                ('planprovider_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='planman.PlanProvider', verbose_name='*service provider _ key')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='*useraccount')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('lastsync', models.DateTimeField(verbose_name='Last time user loaded transactions', blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='planevent',
            name='userplan',
            field=models.ForeignKey(to='planman.UserPlan'),
        ),
    ]
