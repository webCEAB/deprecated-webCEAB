# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('numeroControl', models.IntegerField()),
                ('nombre', models.TextField(max_length=100)),
                ('direccion', models.TextField(max_length=200)),
                ('fechaNacimiento', models.DateTimeField()),
                ('fechaCreacionRegistro', models.DateTimeField(default=django.utils.timezone.now)),
                ('centroInscripcion', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('colegiatura', models.DecimalField(max_digits=6, decimal_places=2)),
                ('perteneceEmpresa', models.BooleanField()),
            ],
        ),
    ]
