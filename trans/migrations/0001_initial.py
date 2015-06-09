# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaidAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('_id', models.CharField(verbose_name='Plaids _id Field', max_length=50)),
                ('_item', models.CharField(max_length=50)),
                ('_user', models.CharField(max_length=50)),
                ('name', models.CharField(verbose_name='Account Name', max_length=50)),
                ('type', models.CharField(verbose_name='Account Type', max_length=10)),
                ('institution_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PlaidTransaction',
            fields=[
                ('json_raw', models.TextField(blank=True)),
                ('_account', models.CharField(max_length=50)),
                ('_id', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField()),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('state', models.SmallIntegerField(choices=[(0, 'new'), (1, 'flagged'), (2, 'converted'), (3, 'ignored')])),
                ('account', models.ForeignKey(to='trans.PlaidAccount')),
            ],
        ),
        migrations.CreateModel(
            name='PlaidUserToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('access_token', models.CharField(verbose_name='token used to access account from plaid', max_length=200)),
                ('last_sync', models.DateTimeField(null=True, blank=True)),
                ('status', models.CharField(choices=[('ok', 'Ok'), ('connecting', 'In Process'), ('failed', 'Needs Attention'), ('new', 'New')], max_length=10)),
                ('status_text', models.CharField(max_length=128, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='plaidtransaction',
            name='usertoken',
            field=models.ForeignKey(to='trans.PlaidUserToken'),
        ),
        migrations.AddField(
            model_name='plaidaccount',
            name='usertoken',
            field=models.ForeignKey(to='trans.PlaidUserToken'),
        ),
    ]
