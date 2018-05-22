# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-22 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0009_auto_20180520_2021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='release',
            old_name='windows_artifact',
            new_name='nsis_exe',
        ),
        migrations.AddField(
            model_name='release',
            name='nsis_exe_sha512',
            field=models.TextField(blank=True, null=True),
        ),
    ]
