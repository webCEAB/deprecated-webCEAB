from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from siad.models import Plantel, Empleado,Empresa,Documento,Estatus
from promotoria.models import Aspirantes
from decimal import Decimal


class Materia(models.Model):
	nombre = models.CharField(max_length = 50)
	fecha_inicio = models.DateField()
	fecha_termino = models.DateField()
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
	horario_inicio = models.TimeField()#choices = opcionesHorarios,default = '7:00:00')
	horario_fin = models.TimeField()#choices = opcionesHorarios,default = '9:00:00')
	#opcionesDias = (
	#		('Lunes a viernes','Lunes a viernes'),
	#		('Sabado y domingo','Sabado y domingo'),
	#		('Solo sabado','Solo sabado'),
	#		('Solo domingo','Solo domingo'),
	#		('Otro','Otro'),
	#)
	#diasClase = models.CharField(max_length = 30,choices = opcionesDias,default = 'Lunes a viernes')
	def __str__(self):
		return "%s;\t inicia %s\t termina %s\t, de %s\t a %s" % (self.nombre , self.fecha_inicio, self.fecha_termino, self.horario_inicio, self.horario_fin)

class Estudiante(models.Model):
	fecha_de_registro = models.DateField(default=timezone.now)
	plantel = models.ForeignKey(Plantel, null = True)
	Aspirante = models.OneToOneField(Aspirantes,null = True)
	#Nombre = models.CharField(max_length=20, null=True,blank=True,default=Aspirante.nombre)
	numero_de_control = models.IntegerField(null = True)
	curp = models.CharField(max_length=20, null = True)
	calle = models.CharField(max_length=100, null = True)
	colonia = models.CharField(max_length=100, null = True)
	entre_calles = models.CharField(max_length=100, null = True)
	cp = models.CharField(max_length=5, null = True)
	edad = models.IntegerField(null = True)
	grad_estudios = models.CharField(max_length = 50, null = True)
	estado_civil = models.CharField(max_length = 30, null = True)
	email = models.CharField(max_length=50, null = True)
	numero_de_hijos = models.IntegerField(null = True)
	empresa = models.ForeignKey(Empresa, null = True)
	opciones_servicio = (
			('Secundaria','Secundaria'),
			('Preparatoria Abierta','Preparatoria Abierta'),
			('Colbach','Colbach'),
			('Ceneval','Ceneval'),
			('Propedeutico','Propedeutico'),
			('Otro','Otro'),
	)
	servicio_interes = models.CharField(max_length = 20,choices = opciones_servicio,default = 'Colbach')
	adeudo = models.DecimalField(max_digits = 7,decimal_places=2)
	materias = models.ManyToManyField(Materia)
	estatus = models.ForeignKey(Estatus)
	
	def __str__(self):
		#return self.Aspirante.nombre ######################################################
		return "%d %s %s %s %s" % (self.id,self.Aspirante.nombre,self.Aspirante.apellido_paterno,self.Aspirante.apellido_materno,self.curp)


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
	fecha_inicio = models.DateField()
	fecha_termino= models.DateField()
	opcionesClasificacion = (
			('Global','Global'),
			('Area','Area'),
			('Otro','Otro'),
	)
	clasificacion =  models.CharField(max_length = 10,choices = opcionesClasificacion,default = 'Global')
	def __str__(self):
		return self.servicio

class Boleta(models.Model):
	alumno = models.OneToOneField(Estudiante)
	calificacion_materia_1 = models.DecimalField(max_digits = 4, decimal_places=2,default=Decimal('-1.0'))
	calificacion_materia_2 = models.DecimalField(max_digits = 4, decimal_places=2,default=Decimal('-1.0'))
	calificacion_materia_3 = models.DecimalField(max_digits = 4, decimal_places=2,default=Decimal('-1.0'))
	calificacion_materia_4 = models.DecimalField(max_digits = 4, decimal_places=2,default=Decimal('-1.0'))
	calificacion_materia_5 = models.DecimalField(max_digits = 4, decimal_places=2,default=Decimal('-1.0'))
	calificacion_materia_6 = models.DecimalField(max_digits = 4, decimal_places=2,default=Decimal('-1.0'))
	calificacion_materia_7 = models.DecimalField(max_digits = 4, decimal_places=2,default=Decimal('-1.0'))
	calificacion_materia_8 = models.DecimalField(max_digits = 4, decimal_places=2,default=Decimal('-1.0'))
	calificacion_materia_9 = models.DecimalField(max_digits= 4, decimal_places=2,default=Decimal('-1.0'))
	calificacion_materia_10 = models.DecimalField(max_digits = 4, decimal_places=2,default=Decimal('-1.0'))
	def __str__(self):
		return str(self.alumno)

class Documentacion(models.Model):
	alumno = models.OneToOneField(Estudiante)
	documentacion_completa = models.BooleanField(default=False)
	documentacion_entregada = models.ManyToManyField(Documento)
	
	def __str__(self):
		return str(self.alumno)
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Documentacion" 

#from django.contrib.auth.models import Estudiante

#from django.db.models.signals import post_save
#from django.dispatch import receiver

#@receiver(post_save, sender=Estudiante)
#def create_estudiante(sender, instance, created, **kwargs):
#	if created:
#		print "Se creo un alumno"
#		Boleta.objects.create(user = instance)
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from django.contrib.auth.models import Estudiante

#@receiver(post_save, sender=Estudiante)
#def create_estudiante(sender, instance, created, **kwargs):
#	if created:
#		print "SE CREO UN ALUMNO"
#		Boleta.objects.create(Estudiante = instance)
#	else:
#		print("NO SE HA CREADO UN ALUMNO")