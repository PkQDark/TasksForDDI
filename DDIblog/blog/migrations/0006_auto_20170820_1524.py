# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-20 12:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-path']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='article_id',
            new_name='post_id',
        ),
    ]
