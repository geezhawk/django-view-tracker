# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_auto_20160207_1424'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Byline',
        ),
        migrations.AddField(
            model_name='article',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.IntegerField(max_length=250, null=True),
        ),
    ]
