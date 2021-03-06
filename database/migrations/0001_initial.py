# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 05:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('chat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_number', models.IntegerField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Chat')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger', models.CharField(max_length=100)),
                ('response', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lyrics', models.CharField(max_length=10000)),
                ('lines', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='counter',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Song'),
        ),
        migrations.AddField(
            model_name='chat',
            name='lyric_tracker',
            field=models.ManyToManyField(through='database.Counter', to='database.Song'),
        ),
    ]
