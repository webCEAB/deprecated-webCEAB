# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siad', '0009_auto_20170525_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='Aspirante',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='plantelRegistro',
        ),
        migrations.RemoveField(
            model_name='aspirante',
            name='plantel',
        ),
        migrations.RemoveField(
            model_name='aspirante',
            name='promotor',
        ),
        migrations.RemoveField(
            model_name='aspirante',
            name='servicioInteres',
        ),
        migrations.RemoveField(
            model_name='pago',
            name='alumno',
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Aspirante',
        ),
    ]
