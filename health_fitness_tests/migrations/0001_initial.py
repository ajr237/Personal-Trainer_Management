# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-22 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0003_auto_20180410_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyMassIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField()),
                ('mass', models.FloatField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
            ],
        ),
    ]
