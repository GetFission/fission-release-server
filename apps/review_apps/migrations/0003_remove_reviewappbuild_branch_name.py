# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review_apps', '0002_auto_20171102_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewappbuild',
            name='branch_name',
        ),
    ]