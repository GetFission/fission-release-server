# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20171027_2216'),
        ('review_apps', '0001_squashed_0006_auto_20171025_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='projects.Project')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('commit_hash', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='review_apps.Branch')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='reviewappbuild',
            name='commit_hash',
        ),
        migrations.RemoveField(
            model_name='reviewappbuild',
            name='project',
        ),
        migrations.AlterField(
            model_name='reviewappbuild',
            name='build_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='reviewappbuild',
            name='commit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='builds', to='review_apps.Commit'),
        ),
    ]
