# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
                ('rfc', models.CharField(max_length=20)),
                ('calle', models.CharField(max_length=100)),
                ('colonia', models.CharField(max_length=100)),
                ('ciudadEstado', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=5)),
                ('email', models.CharField(max_length=50)),
                ('telefonoExtension', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
