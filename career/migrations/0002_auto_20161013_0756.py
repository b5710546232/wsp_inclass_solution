# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='dateofB',
            new_name='dateOfBirth',
        ),
    ]