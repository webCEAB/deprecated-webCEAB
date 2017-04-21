# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('siad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='apellidoMaterno',
            field=models.TextField(max_length=100, default=datetime.datetime(2017, 4, 10, 15, 33, 7, 465382, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='apellidoPaterno',
            field=models.TextField(max_length=100, default=datetime.datetime(2017, 4, 10, 15, 33, 18, 445173, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='fechaNacimiento',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
