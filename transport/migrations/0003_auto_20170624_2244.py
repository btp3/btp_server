# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-24 17:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0002_transportlocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transportlocation',
            name='location',
        ),
        migrations.RemoveField(
            model_name='transportlocation',
            name='transport',
        ),
        migrations.DeleteModel(
            name='TransportLocation',
        ),
    ]
