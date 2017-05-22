# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siad', '0007_auto_20170421_0933'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactoempresarial',
            options={'verbose_name_plural': 'Contactos empresariales'},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelOptions(
            name='plantel',
            options={'verbose_name_plural': 'Planteles'},
        ),
        migrations.AlterModelOptions(
            name='proovedor',
            options={'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterModelOptions(
            name='servicio',
            options={'verbose_name_plural': 'Servicios'},
        ),
        migrations.AlterField(
            model_name='aspirante',
            name='formaContacto',
            field=models.CharField(max_length=20, default='Personal', choices=[('Personal', 'Personal'), ('Telefono', 'Telefono'), ('Correo elctronico', 'Correo electronico'), ('Otro', 'Otro')]),
        ),
        migrations.AlterField(
            model_name='aspirante',
            name='medioContacto',
            field=models.CharField(max_length=20, default='Recomendacion', choices=[('Recomendacion', 'Recomendacion'), ('Instalaciones', 'Instalaciones'), ('Internet', 'Internet'), ('Lona publicitaria', 'Lona publiciataria'), ('Volante', 'volante'), ('Radio', 'Radio'), ('Otro', 'Otro')]),
        ),
        migrations.AlterField(
            model_name='curso',
            name='clasificacion',
            field=models.CharField(max_length=10, default='Global', choices=[('Global', 'Global'), ('Area', 'Area'), ('Otro', 'Otro')]),
        ),
        migrations.AlterField(
            model_name='curso',
            name='duracion',
            field=models.CharField(max_length=15, default='Dos meses', choices=[('Dos meses', 'Dos meses'), ('Cuatro meses', 'Cuatro meses'), ('Ocho meses', 'Ocho meses'), ('Otro', 'Otro')]),
        ),
        migrations.AlterField(
            model_name='curso',
            name='servicio',
            field=models.CharField(max_length=25, default='Colbach', choices=[('Colbach', 'Colbach'), ('Secundaria', 'Secundaria'), ('Ceneval', 'Ceneval'), ('Prepa abierta', 'Prepa abierta'), ('Propedeutico prepa', 'Propedeutico prepa'), ('Propedeutico Uni', 'Propedeutico Uni'), ('Otro', 'Otro')]),
        ),
        migrations.AlterField(
            model_name='egreso',
            name='concepto',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='materia',
            name='clasificacion',
            field=models.CharField(max_length=15, default='Regular', choices=[('Regular', 'Regular'), ('Recursamiento', 'Recursamiento'), ('Otro', 'Otro')]),
        ),
        migrations.AlterField(
            model_name='materia',
            name='diasClase',
            field=models.CharField(max_length=30, default='Lunes a viernes', choices=[('Lunes a viernes', 'Lunes a viernes'), ('Lunes miercoles y viernes', 'Lunes, miercoles y viernes'), ('Sabado y domingo', 'Sabado y domingo'), ('sabado', 'Sabado'), ('Domingo', 'Domingo'), ('Otro', 'Otro')]),
        ),
        migrations.AlterField(
            model_name='pago',
            name='esquema',
            field=models.CharField(max_length=10, default='Semanal', choices=[('Semanal', 'Semanal'), ('Quincenal', 'Quincenal'), ('Mensual', 'Mensual'), ('Un solo pago', 'Un solo pago'), ('Otro', 'otro')]),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechaInicio',
            field=models.DateTimeField(),
        ),
    ]
