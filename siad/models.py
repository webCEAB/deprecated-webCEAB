from django.db import models
from django.utils import timezone
from contabilidad.models import Proveedor

class Plantel(models.Model):
	nombre = models.CharField(max_length = 50)
	rfc = models.CharField(max_length = 20)
	calle = models.CharField(max_length=100)
	colonia = models.CharField(max_length=100)
	ciudadEstado = models.CharField(max_length = 50)
	cp = models.CharField(max_length=5)
	email = models.CharField(max_length=50)
	telefono = models.CharField(max_length = 10)
	def __str__(self):
		return self.nombre
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Planteles" 

class Empleado(models.Model):
	nombre = models.CharField(max_length=30)
	plantel = models.ForeignKey(Plantel)
	nombre = models.CharField(max_length=30)
	apellidoPaterno = models.CharField(max_length=20)
	apellidoMaterno = models.CharField(max_length=20)
	telefono = models.CharField(max_length = 10)
	puesto = models.CharField(max_length = 50)
	sueldo = models.DecimalField(max_digits = 7, decimal_places = 2)
	def __str__(self):
		return "%s: %s %s "%(self.puesto,self.nombre,self.apellidoPaterno)
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Empleados" 

class ContactoEmpresarial(models.Model):
	nombre = models.CharField(max_length=100)
	puesto = models.CharField(max_length=50)
	horario = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Contactos empresariales" 

class Empresa(models.Model):
	nombre = models.CharField(max_length=100)
	rfc = models.CharField(max_length = 20)
	calle = models.CharField(max_length=100)
	colonia = models.CharField(max_length=100)
	ciudadEstado = models.CharField(max_length = 100)
	cp = models.CharField(max_length=5)
	email = models.CharField(max_length=50)
	telefonoExtension = models.CharField(max_length=50)
	contactoEmpresarial = models.ForeignKey(ContactoEmpresarial)
	def __str__(self):
		return self.nombre