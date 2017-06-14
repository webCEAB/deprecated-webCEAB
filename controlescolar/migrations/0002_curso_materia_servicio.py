# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlescolar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('servicio', models.CharField(default='Colbach', max_length=25, choices=[('Colbach', 'Colbach'), ('Secundaria', 'Secundaria'), ('Ceneval', 'Ceneval'), ('Prepa abierta', 'Prepa abierta'), ('Propedeutico prepa', 'Propedeutico prepa'), ('Propedeutico Uni', 'Propedeutico Uni'), ('Otro', 'Otro')])),
                ('duracion', models.CharField(default='Dos meses', max_length=15, choices=[('Dos meses', 'Dos meses'), ('Cuatro meses', 'Cuatro meses'), ('Ocho meses', 'Ocho meses'), ('Otro', 'Otro')])),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('clasificacion', models.CharField(default='Global', max_length=10, choices=[('Global', 'Global'), ('Area', 'Area'), ('Otro', 'Otro')])),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('horarioBaseInicio', models.TimeField()),
                ('horarioBaseFin', models.TimeField()),
                ('rolHorarioInicio', models.TimeField()),
                ('rolHorarioFin', models.TimeField()),
                ('diasClase', models.CharField(default='Lunes a viernes', max_length=30, choices=[('Lunes a viernes', 'Lunes a viernes'), ('Lunes miercoles y viernes', 'Lunes, miercoles y viernes'), ('Sabado y domingo', 'Sabado y domingo'), ('sabado', 'Sabado'), ('Domingo', 'Domingo'), ('Otro', 'Otro')])),
                ('clasificacion', models.CharField(default='Regular', max_length=15, choices=[('Regular', 'Regular'), ('Recursamiento', 'Recursamiento'), ('Otro', 'Otro')])),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('costo', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
