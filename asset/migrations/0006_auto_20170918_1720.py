# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_auto_20170918_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='%Y%m%d46649'),
        ),
    ]
