# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170822_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='level',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]