# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-28 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parascopish', '0005_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
