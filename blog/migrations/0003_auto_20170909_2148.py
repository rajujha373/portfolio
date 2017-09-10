# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 16:18
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_title',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='like',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]