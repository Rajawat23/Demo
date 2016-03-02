# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_browsing_pattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('timestamp', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User_intent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=255)),
                ('intent', models.TextField()),
                ('timestamp', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User_interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=255)),
                ('interest', models.TextField()),
                ('timestamp', models.CharField(max_length=20)),
            ],
        ),
    ]
