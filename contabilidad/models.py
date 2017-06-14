from django.db import models

# Create your models here.
class Proveedor(models.Model):
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
	destino = models.ForeignKey(Proveedor)
	factura = models.BooleanField()
	montoCubierto = models.DecimalField(max_digits = 7, decimal_places = 2)
	def __str__(self):
		return self.concepto
