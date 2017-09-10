# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='players',
            field=models.ManyToManyField(blank=True, to='database.Player'),
        ),
    ]
