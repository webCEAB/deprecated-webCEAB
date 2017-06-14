from django.db import models
from django.utils import timezone

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

class Pago(models.Model):
	#alumno = models.ForeignKey(Alumno)
	opcionesEsquema = (
			('Semanal','Semanal'),
			('Quincenal','Quincenal'),
			('Mensual','Mensual'),
			('Un solo pago','Un solo pago'),
			('Otro', 'otro'),
	)
	esquema = models.CharField(max_length = 10,choices = opcionesEsquema,default = 'Semanal')
	fechaInicio = models.DateTimeField()
	monto = models.DecimalField(max_digits = 7,decimal_places=2)
	descripcion = models.CharField(max_length=100)
	def __str__(self):
		return self.descripcion

class Materia(models.Model):
	nombre = models.CharField(max_length = 50)
	fechaInicio = models.DateField()
	fechaFin = models.DateField()
	horarioBaseInicio = models.TimeField()
	horarioBaseFin = models.TimeField()
	rolHorarioInicio = models.TimeField()
	rolHorarioFin = models.TimeField()
	opcionesDias = (
			('Lunes a viernes','Lunes a viernes'),
			('Lunes miercoles y viernes','Lunes, miercoles y viernes'),
			('Sabado y domingo','Sabado y domingo'),
			('sabado','Sabado'),
			('Domingo','Domingo'),
			('Otro','Otro'),
	)
	diasClase = models.CharField(max_length = 30,choices = opcionesDias,default = 'Lunes a viernes')
	opcionesClasificacion = (
			('Regular','Regular'),
			('Recursamiento','Recursamiento'),
			('Otro','Otro'),
	)
	clasificacion = models.CharField(max_length = 15,choices = opcionesClasificacion,default = 'Regular')
	def __str__(self):
		return "%s %s" % (self.nombre , self.clasificacion)

class Proovedor(models.Model):
	nombre = models.CharField(max_length=100)
	rfc = models.CharField(max_length = 20)
	calle = models.CharField(max_length=100)
	colonia = models.CharField(max_length=100)
	ciudadEstado = models.CharField(max_length = 100)
	cp = models.CharField(max_length=5)
	email = models.CharField(max_length=50)
	telefonoExtension = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre
	class Meta: 
		#ordering = ["nombre"] 
		verbose_name_plural = "Proveedores" 

class Egreso(models.Model):
	opcionesConcepto = (
			('Nomina','Nomina'),
			('Servicios generales','Servicios generales (cfe,internet,etc)'),
			('Gastos corrientes','Gastos corrientes (copias, papeleria, ferreteria)'),
			('Otros','Otros')
	)
	numeroRegistro = models.IntegerField()
	concepto = models.CharField(max_length = 20)
	descripcion = models.CharField(max_length = 100)
	monto = models.DecimalField(max_digits = 7, decimal_places = 2)
	fecha = models.DateField()
	destino = models.ForeignKey(Proovedor)
	factura = models.BooleanField()
	montoCubierto = models.DecimalField(max_digits = 7, decimal_places = 2)
	def __str__(self):
		return self.concepto