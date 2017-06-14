# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siad', '0009_auto_20170525_1040'),
        ('promotoria', '0004_auto_20170613_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fechaCreacionRegistro', models.DateField(default=django.utils.timezone.now)),
                ('numeroControl', models.IntegerField(null=True)),
                ('curp', models.CharField(max_length=20, null=True)),
                ('calle', models.CharField(max_length=100, null=True)),
                ('colonia', models.CharField(max_length=100, null=True)),
                ('entreCalles', models.CharField(max_length=100, null=True)),
                ('cp', models.CharField(max_length=5, null=True)),
                ('edad', models.IntegerField(null=True)),
                ('gradoEstudios', models.CharField(max_length=50, null=True)),
                ('estadoCivil', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('numeroHijos', models.IntegerField(null=True)),
                ('documentacionCompleta', models.BooleanField(default=False)),
                ('Aspirante', models.ForeignKey(null=True, to='promotoria.Aspirantes')),
                ('empresa', models.ForeignKey(null=True, to='siad.Empresa')),
                ('plantelRegistro', models.ForeignKey(null=True, to='siad.Plantel')),
            ],
        ),
    ]
