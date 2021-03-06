# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0014_auto_20160213_0708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='byline',
            options={'ordering': ['all_views']},
        ),
        migrations.AddField(
            model_name='byline',
            name='all_views',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='byline',
            name='most_viewed_all_time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='all_time_most_viewed', to='www.Article'),
        ),
        migrations.AddField(
            model_name='byline',
            name='most_viewed_weekly',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weekly_most_viewed', to='www.Article'),
        ),
        migrations.AddField(
            model_name='byline',
            name='weekly_views',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]
