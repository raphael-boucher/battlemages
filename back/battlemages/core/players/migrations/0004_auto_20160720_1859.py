# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20160630_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_activity',
            field=models.DateField(auto_now=True),
        ),
    ]