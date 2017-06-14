from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from siad.models import Plantel, Empleado,Empresa
from promotoria.models import Aspirantes

class Estudiante(models.Model):
	fechaCreacionRegistro = models.DateField(default=timezone.now)
	plantelRegistro = models.ForeignKey(Plantel, null = True)
	Aspirante = models.ForeignKey(Aspirantes,null = True)
	#Nombre = models.CharField(max_length=20, null=True,blank=True,default=Aspirantes.nombre)
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

class Materia(models.Model):
	nombre = models.CharField(max_length = 50)
	fechaInicio = models.DateField()
	fechaFin = models.DateField()
	opcionesHorarios = (
			('7:00:00','7:00:00'),
			('8:00:00','8:00:00'),
			('9:00:00','9:00:00'),
			('13:00:00','13:00:00'),
			('16:00:00','16:00:00'),
			('19:30:00','19:30:00'),
			('21:00:00','21:00:00'),
			('21:15:00','21:15:00'),
	)
	horarioInicio = models.TimeField()#choices = opcionesHorarios,default = '7:00:00')
	horarioFin = models.TimeField()#choices = opcionesHorarios,default = '9:00:00')
	#opcionesDias = (
	#		('Lunes a viernes','Lunes a viernes'),
	#		('Sabado y domingo','Sabado y domingo'),
	#		('Solo sabado','Solo sabado'),
	#		('Solo domingo','Solo domingo'),
	#		('Otro','Otro'),
	#)
	#diasClase = models.CharField(max_length = 30,choices = opcionesDias,default = 'Lunes a viernes')
	def __str__(self):
		return "%s; inicia %s termina %s, de %s a %s" % (self.nombre , self.fechaInicio, self.fechaFin, self.horarioInicio, self.horarioFin)

class Servicio(models.Model):
	nombre = models.CharField(max_length = 50)
	costo = models.DecimalField(max_digits= 7,decimal_places=2)
	def __str__(self):
		return self.nombre
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Servicios" 

class Curso(models.Model):
	opcionesServicio = (
			('Colbach','Colbach'),
			('Secundaria','Secundaria'),
			('Ceneval','Ceneval'),
			('Prepa abierta','Prepa abierta'),
			('Propedeutico prepa','Propedeutico prepa'),
			('Propedeutico Uni','Propedeutico Uni'),
			('Otro','Otro'),
	)
	servicio = models.CharField(max_length = 25,choices = opcionesServicio,default = 'Colbach')
	opcionesDuracion = (
			('Dos meses','Dos meses'),
			('Cuatro meses','Cuatro meses'),
			('Ocho meses','Ocho meses'),
			('Otro','Otro'),
	)
	duracion = models.CharField(max_length = 15,choices = opcionesDuracion,default = 'Dos meses')
	fechaInicio = models.DateField()
	fechaFin = models.DateField()
	opcionesClasificacion = (
			('Global','Global'),
			('Area','Area'),
			('Otro','Otro'),
	)
	clasificacion =  models.CharField(max_length = 10,choices = opcionesClasificacion,default = 'Global')
	def __str__(self):
		return self.servicio
