# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_apps', '0005_auto_20171024_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewappbuild',
            name='ci',
            field=models.CharField(choices=[('appveyor', 'appveyor'), ('travis', 'travis'), ('teamcity', 'teamcity'), ('jenkins', 'jenkins'), ('local', 'local'), ('N/A', 'N/A')], max_length=50),
        ),
    ]
