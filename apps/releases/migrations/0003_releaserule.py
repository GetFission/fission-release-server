# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-17 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0002_auto_20180517_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReleaseRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_darwin', models.BooleanField(default=False)),
                ('is_windows', models.BooleanField(default=False)),
                ('is_linux', models.BooleanField(default=False)),
                ('channel', models.CharField(blank=True, max_length=255, null=True)),
                ('darwin_percent', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('windows_percent', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('linux_percent', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True)),
                ('release', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='releases.Release')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
