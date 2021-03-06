# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-14 02:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0004_auto_20180813_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=10)),
                ('r_p', models.ManyToManyField(to='backweb.Permission')),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='role',
            name='r_u',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backweb.User'),
        ),
    ]
