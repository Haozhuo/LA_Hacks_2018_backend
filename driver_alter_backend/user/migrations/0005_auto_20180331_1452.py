# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-31 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20180331_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='createdAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]