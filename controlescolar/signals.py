from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Estudiante, Boleta, Documentacion



@receiver(post_save, sender=Estudiante)
def my_handler(sender, instance,created,**kwargs):
	print "A INSTANCE OF Boleta AND Documentacion HAS BEEEN CREATED",created
	Boleta.objects.create(alumno=instance)
	Documentacion.objects.create(alumno=instance)