# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-10 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='contact_number',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('0', 'Female')], default='1', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
