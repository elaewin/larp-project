# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20160424_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='age_limit',
            field=models.PositiveSmallIntegerField(default='18'),
        ),
        migrations.AddField(
            model_name='event',
            name='age_restriction',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='event',
            name='contact_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='event',
            name='cost',
            field=models.PositiveSmallIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='event',
            name='location_address1',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='event',
            name='location_address2',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='event',
            name='location_city',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='event',
            name='location_state',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='event',
            name='pregens',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='rules_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='online_rules',
            field=models.BooleanField(default=False),
        ),
    ]
