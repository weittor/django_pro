# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 08:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_auto_20160330_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmanage',
            name='cmds',
        ),
    ]
