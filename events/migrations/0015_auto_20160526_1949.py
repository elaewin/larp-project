# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 19:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0014_auto_20160526_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Playing'), (2, 'Not Playing')])),
            ],
            options={
                'verbose_name_plural': 'Participation',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('participating_in', models.ManyToManyField(related_name='playing_in', through='events.Participation', to='events.Player')),
            ],
        ),
        migrations.RemoveField(
            model_name='participant',
            name='game',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='players',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='events',
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='participation',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='participation',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Player'),
        ),
        migrations.AddField(
            model_name='event',
            name='players',
            field=models.ManyToManyField(through='events.Participation', to='events.Player'),
        ),
    ]