# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0018_auto_20160218_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]