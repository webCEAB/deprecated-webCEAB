# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0002_egreso_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='esquema',
            field=models.CharField(max_length=10, default='Semanal', choices=[('Semanal', 'Semanal'), ('Quincenal', 'Quincenal'), ('Mensual', 'Mensual'), ('Un solo pago', 'Un solo pago'), ('Otro', 'otro')]),
        ),
    ]
