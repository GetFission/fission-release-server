# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-17 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_projectclient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectclient',
            name='uid',
            field=models.CharField(max_length=255),
        ),
    ]
