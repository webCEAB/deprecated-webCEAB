#from django.core.signals import post_save
#from django.dispatch import receiver
#from contrololescolar.models import Estudiante
#from django.contrib.auth.models import Estudiante
#	post_save.connect(estudiante_creado, dispatch_uid="identificador_unico_de_estudiante_creado")

#@receiver(post_save,sender = Estudiante)
#def estudiante_creado(sender, instance, created, **kwargs):
#	if created:
#		print("SE HA CREADO UN ALUMNO")
#	else:	
#		print("NO SE HA CREADO UN ALUMNO")
#
#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()

#from django.contrib.auth.models import Estudiante



from controlescolar.models import Boleta, Estudiante
from promotoria.models import Aspirantes, Caracteristica
@receiver(post_save, sender=Estudiante)
def my_handler(sender, instance,created,**kwargs):
	print "Se intenta crear una instancia de caracteristicas",created
	Boleta.objects.create(aspirante=instance)
