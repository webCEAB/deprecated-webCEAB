from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from siad.models import Plantel, Empleado, Curso

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
	servicioInteres = models.ForeignKey(Curso)

	class Meta:
		ordering=["apellidoPaterno"]

	def __str__(self):
		return "%s %s %s" % (self.nombre,self.apellidoPaterno,self.apellidoMaterno)

# Create your models here.
