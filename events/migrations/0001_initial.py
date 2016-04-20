# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 00:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('game_system', models.CharField(max_length=128)),
                ('online_rules', models.BooleanField()),
                ('rules_url', models.URLField(blank=True)),
                ('date', models.DateTimeField()),
                ('checkin', models.TimeField()),
                ('game_on', models.TimeField()),
                ('game_off', models.TimeField()),
                ('location_address1', models.CharField(blank=True, max_length=64)),
                ('location_city', models.CharField(max_length=64)),
                ('location_state', models.CharField(max_length=2)),
                ('contact_name', models.CharField(max_length=128)),
                ('contact_email', models.EmailField(max_length=254)),
                ('pregens', models.BooleanField()),
                ('age_restriction', models.BooleanField()),
                ('age_limit', models.PositiveSmallIntegerField(max_length=2)),
                ('cost', models.PositiveSmallIntegerField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]