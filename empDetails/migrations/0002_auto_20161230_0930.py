# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-30 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empDetails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdetailsmodel',
            name='file',
            field=models.FileField(upload_to=b''),
        ),
    ]
