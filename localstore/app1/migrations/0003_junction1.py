# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='junction1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=255)),
                ('sname', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]
