# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_auto_20160207_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
