# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='age_limit',
            field=models.PositiveSmallIntegerField(),
        ),
    ]