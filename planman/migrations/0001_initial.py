# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PlanPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user_description', models.CharField(max_length=200)),
                ('planevent', models.ForeignKey(to='planman.PlanEvent')),
            ],
        ),
        migrations.CreateModel(
            name='PlanProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user_description', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('next_renewal_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('provider', models.ForeignKey(to='planman.PlanProvider')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='userplan',
            name='userprofile',
            field=models.ForeignKey(to='planman.UserProfile'),
        ),
        migrations.AddField(
            model_name='planevent',
            name='userplan',
            field=models.ForeignKey(to='planman.UserPlan'),
        ),
    ]
