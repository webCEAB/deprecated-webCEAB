from django.db import models
from django.utils import timezone
class Alumno(models.Model):
	#nombre = models.ForeignKey('auth.User')
	id = models.IntegerField(primary_key=True)
	numeroControl = models.IntegerField()
	nombre = models.TextField(max_length=100)
	direccion = models.TextField(max_length=200)
	fechaNacimiento = models.DateTimeField()
	fechaCreacionRegistro = models.DateTimeField(default=timezone.now)
	centroInscripcion = models.CharField(max_length=100)
	status = models.CharField(max_length = 100)
	colegiatura = models.DecimalField(max_digits=6, decimal_places=2)
	perteneceEmpresa = models.BooleanField()

	def __str__(self):
		return self.nombre
