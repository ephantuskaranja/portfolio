# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-15 06:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20180719_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='github_link',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='live_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
