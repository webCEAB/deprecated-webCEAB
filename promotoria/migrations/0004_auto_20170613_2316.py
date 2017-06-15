# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotoria', '0003_auto_20170610_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='Aspirante',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='plantelRegistro',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]
