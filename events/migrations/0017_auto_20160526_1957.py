# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 19:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20160526_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='participating_in',
            field=models.ManyToManyField(related_name='playing_in', through='events.Relationship', to='events.Player'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='from_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_people', to='events.Player'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='to_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_people', to='events.Player'),
        ),
    ]
