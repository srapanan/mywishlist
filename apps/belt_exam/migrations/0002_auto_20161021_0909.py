# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 16:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
