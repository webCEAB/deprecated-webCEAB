from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from siad.models import Plantel, Empleado, Curso, Empresa
from promotoria.models import Aspirantes

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
