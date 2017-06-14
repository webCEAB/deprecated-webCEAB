# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siad', '0010_auto_20170614_0038'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.RemoveField(
            model_name='egreso',
            name='destino',
        ),
        migrations.DeleteModel(
            name='Materia',
        ),
        migrations.DeleteModel(
            name='Pago',
        ),
        migrations.DeleteModel(
            name='Servicio',
        ),
        migrations.DeleteModel(
            name='Egreso',
        ),
        migrations.DeleteModel(
            name='Proovedor',
        ),
    ]
