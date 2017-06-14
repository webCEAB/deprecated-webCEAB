# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('numeroRegistro', models.IntegerField()),
                ('concepto', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('monto', models.DecimalField(max_digits=7, decimal_places=2)),
                ('fecha', models.DateField()),
                ('factura', models.BooleanField()),
                ('montoCubierto', models.DecimalField(max_digits=7, decimal_places=2)),
                ('destino', models.ForeignKey(to='contabilidad.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('esquema', models.CharField(default='Semanal', max_length=10, choices=[('Semanal', 'Semanal'), ('Quincenal', 'Quincenal'), ('Mensual', 'Mensual'), ('Un solo pago', 'Un solo pago'), ('Otro', 'otro')])),
                ('fechaInicio', models.DateTimeField()),
                ('monto', models.DecimalField(max_digits=7, decimal_places=2)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
