# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0019_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]