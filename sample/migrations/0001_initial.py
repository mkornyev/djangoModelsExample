# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-13 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('andrew_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=8)),
                ('lname', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='sample.Student'),
        ),
    ]
