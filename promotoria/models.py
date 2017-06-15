from __future__ import unicode_literals
<<<<<<< HEAD

=======
>>>>>>> 89b6ba607cb306d585a2d3e5d39498dc16807940
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

<<<<<<< HEAD
class Estudiante(models.Model):
	fechaCreacionRegistro = models.DateField(default=timezone.now)
	plantelRegistro = models.ForeignKey(Plantel, null = True)
	Aspirante = models.ForeignKey(Aspirantes,null = True)
	#Nombre = models.CharField(max_length=20, null=True,blank=True,default=Aspirante.nombre)
	numeroControl = models.IntegerField(null = True)
	curp = models.CharField(max_length=20, null = True)
	calle = models.CharField(max_length=100, null = True)
	colonia = models.CharField(max_length=100, null = True)
	entreCalles = models.CharField(max_length=100, null = True)
	cp = models.CharField(max_length=5, null = True)
	edad = models.IntegerField(null = True)
	gradoEstudios = models.CharField(max_length = 50, null = True)
	estadoCivil = models.CharField(max_length = 30, null = True)
	email = models.CharField(max_length=50, null = True)
	numeroHijos = models.IntegerField(null = True)
	empresa = models.ForeignKey(Empresa, null = True)
	documentacionCompleta = models.BooleanField(default=False)
	def __str__(self):
		return self.curp ######################################################3
=======
>>>>>>> 89b6ba607cb306d585a2d3e5d39498dc16807940
