# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-20 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0007_auto_20180519_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasemember',
            name='is_rolled_back',
            field=models.BooleanField(default=False),
        ),
    ]
