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
class Servicio(models.Model):
	nombre = models.CharField(max_length = 50)
	costo = models.DecimalField(max_digits= 7,decimal_places=2)
	def __str__(self):
		return self.nombre
class Curso(models.Model):
	opcionesServicio = (
			('col','Colbach'),
			('sec','Secundaria'),
			('cen','Ceneval'),
			('pre','Prepa abierta'),
			('prp','Propedeutico prepa'),
			('pru','Propedeutico Uni'),
			('otr','Otro'),
	)
	servicio = models.CharField(max_length = 3,choices = opcionesServicio,default = 'col')
	opcionesDuracion = (
			('dos','Dos meses'),
			('cua','Cuatro meses'),
			('och','Ocho meses'),
			('otr','Otro'),
	)
	duracion = models.CharField(max_length = 3,choices = opcionesDuracion,default = 'col')
	fechaInicio = models.DateField()
	fechaFin = models.DateField()
	opcionesClasificacion = (
			('glo','Global'),
			('are','Area'),
			('otr','Otro'),
	)
	clasificacion =  models.CharField(max_length = 3,choices = opcionesClasificacion,default = 'glo')
	def __str__(self):
		return self.servicio	
class Aspirante(models.Model):
	plantel = models.ForeignKey(Plantel)
	nombre = models.CharField(max_length=30)
	apellidoPaterno = models.CharField(max_length=20)
	apellidoMaterno = models.CharField(max_length=20)
	fechaCreacionRegistro = models.DateField(default=timezone.now)
	promotor = models.ForeignKey(Empleado)
	opcionesContacto = (
			('per','Personal'),
			('tel','Telefono'),
			('ema','Correo electronico'),
			('otr','Otro'),
	)
	formaContacto = models.CharField(max_length = 3, choices = opcionesContacto,default = 'rec')
	telefono = models.CharField(max_length = 10)
	celular = models.CharField(max_length = 13)
	opcionesMedio = (
			('rec','Recomendacion'),
			('ins','Instalaciones'),
			('int','Internet'),
			('lon','Lona publiciataria'),
			('vol','volante'),
			('rad','Radio'),
			('otr','Otro'),
	)
	medioContacto = models.CharField(max_length = 3,choices = opcionesMedio,default = 'rec')
	servicioInteres = models.ForeignKey(Curso)
	def __str__(self):
		return self.nombre
class ContactoEmpresarial(models.Model):
	nombre = models.CharField(max_length=100)
	puesto = models.CharField(max_length=50)
	horario = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre
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
class Alumno(models.Model):
	fechaCreacionRegistro = models.DateField(default=timezone.now)
	plantelRegistro = models.ForeignKey(Plantel, null = True)
	Aspirante = models.ForeignKey(Aspirante,null = True)
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

class Pago(models.Model):
	alumno = models.ForeignKey(Alumno)
	opcionesEsquema = (
			('col','Semanal'),
			('sec','Quincenal'),
			('cen','Mensual'),
			('pre','Un solo pago'),
			('otr', 'otro'),
	)
	esquema = models.CharField(max_length = 3,choices = opcionesEsquema,default = 'sem')
	fechaInicio = models.DateField()
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
			('lav','Lunes a viernes'),
			('lmv','Lunes, miercoles y viernes'),
			('syd','Sabado y domingo'),
			('sab','Sabado'),
			('dom','Domingo'),
			('otr','Otro'),
	)
	diasClase = models.CharField(max_length = 3,choices = opcionesDias,default = 'lav')
	opcionesClasificacion = (
			('reg','Regular'),
			('rec','Recursamiento'),
			('otr','Otro'),
	)
	clasificacion = models.CharField(max_length = 3,choices = opcionesClasificacion,default = 'glo')
	def __str__(self):
		return self.nombre
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
class Egreso(models.Model):
	opcionesConcepto = (
			('nom','nomina'),
			('ser','Servicios generales (cfe,internet,etc)'),
			('gac','Gastos corrientes (copias, papeleria, ferreteria)'),
			('otr','Otros')
	)
	numeroRegistro = models.IntegerField()
	concepto = models.CharField(max_length = 50)
	descripcion = models.CharField(max_length = 100)
	monto = models.DecimalField(max_digits = 7, decimal_places = 2)
	fecha = models.DateField()
	destino = models.ForeignKey(Proovedor)
	factura = models.BooleanField()
	montoCubierto = models.DecimalField(max_digits = 7, decimal_places = 2)
	def __str__(self):
		return self.concepto

	
	
	
	
	
