# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('emailid', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'registered_users',
            },
        ),
    ]
