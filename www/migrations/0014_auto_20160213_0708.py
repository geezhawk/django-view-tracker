# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 07:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0013_auto_20160213_0545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='byline',
            options={},
        ),
        migrations.RemoveField(
            model_name='byline',
            name='view_count',
        ),
    ]
