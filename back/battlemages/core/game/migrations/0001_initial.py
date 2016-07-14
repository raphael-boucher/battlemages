# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 20:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mages', '0001_initial'),
        ('spells', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MageState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.PositiveSmallIntegerField(choices=[(1, 'team 1'), (2, 'team 2')])),
                ('location_x', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(20)])),
                ('location_y', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(20)])),
                ('hp', models.SmallIntegerField()),
                ('mana', models.SmallIntegerField(default=0)),
                ('dead', models.BooleanField(default=False)),
                ('can_move', models.BooleanField(default=True)),
                ('can_cast', models.BooleanField(default=True)),
                ('discarded_spells', models.ManyToManyField(related_name='discarded_by', to='spells.Spell')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mages', to='game.Game')),
                ('mage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mages.Mage')),
                ('spells_in_hand', models.ManyToManyField(related_name='in_hand_of', to='spells.Spell')),
            ],
        ),
    ]
