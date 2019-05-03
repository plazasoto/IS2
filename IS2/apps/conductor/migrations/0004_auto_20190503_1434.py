# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-03 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conductor', '0003_auto_20190503_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductor',
            name='viaje',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='viajes', to='viaje.Viaje'),
        ),
    ]