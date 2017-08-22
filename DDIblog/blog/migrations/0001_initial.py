# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-19 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('perex', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
