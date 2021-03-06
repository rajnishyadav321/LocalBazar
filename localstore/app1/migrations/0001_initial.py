# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='junction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('pic_link', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('typeofstuff', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('lattitude', models.FloatField(blank=True, default=None, null=True)),
                ('longitude', models.FloatField(blank=True, default=None, null=True)),
                ('ishomedelivery', models.BooleanField(default=True)),
                ('isopen', models.BooleanField(default=True)),
                ('openingtime', models.TimeField(blank=True, default=None, null=True)),
                ('closingtime', models.TimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='junction',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product'),
        ),
        migrations.AddField(
            model_name='junction',
            name='sid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.shop'),
        ),
    ]
