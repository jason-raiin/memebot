# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20170912_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]