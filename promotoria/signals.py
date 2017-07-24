from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Aspirantes, Caracteristica



@receiver(post_save, sender=Aspirantes)
def my_handler(sender, instance,created,**kwargs):
	print "Se intenta crear una instancia de caracteristicas",created
	Caracteristica.objects.create(aspirante=instance)