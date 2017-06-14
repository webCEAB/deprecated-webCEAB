from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from siad.models import Plantel, Empleado, Empresa

class Aspirantes(models.Model):
	plantel = models.ForeignKey(Plantel)
	nombre = models.CharField(max_length=30)
	apellidoPaterno = models.CharField(max_length=20)
	apellidoMaterno = models.CharField(max_length=20)
	fechaCreacionRegistro = models.DateField(default=timezone.now)
	promotor = models.ForeignKey(Empleado)
	opcionesContacto = (
			('Personal','Personal'),
			('Telefono','Telefono'),
			('Correo elctronico','Correo electronico'),
			('Otro','Otro'),
	)
	formaContacto = models.CharField(max_length = 20, choices = opcionesContacto,default = 'Personal')
	telefono = models.CharField(max_length = 10)
	celular = models.CharField(max_length = 13)
	opcionesMedio = (
			('Recomendacion','Recomendacion'),
			('Instalaciones','Instalaciones'),
			('Internet','Internet'),
			('Lona publicitaria','Lona publiciataria'),
			('Volante','volante'),
			('Radio','Radio'),
			('Otro','Otro'),
	)
	medioContacto = models.CharField(max_length = 20,choices = opcionesMedio,default = 'Recomendacion')
	opcionesServicio = (
			('Secundaria','Secundaria'),
			('Preparatoria Abierta','Preparatoria Abierta'),
			('Colbach','Colbach'),
			('Ceneval','Ceneval'),
			('Propedeutico','Propedeutico'),
			('Otro','Otro'),
	)
	servicioInteres = models.CharField(max_length = 20,choices = opcionesServicio,default = 'Colbach')

	class Meta:
		verbose_name_plural = "Prospectos" 
		ordering=["apellidoPaterno"]

	def __str__(self):
		return "%s %s %s" % (self.nombre,self.apellidoPaterno,self.apellidoMaterno)

