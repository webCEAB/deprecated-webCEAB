from django import forms
from django.forms import ModelForm, Textarea
from .models import Aspirante

class FormularioContactos(forms.Form): 
	asunto = forms.CharField()
	email = forms.EmailField(required=False) 
	mensaje = forms.CharField()

class NuevoProspecto(ModelForm): 

	class Meta:
		model = Aspirante

		fields = '__all__'
		labels = {
		'nombre': ('Nombre'),
		'apellidoPaterno': ('Apellido Paterno'),
		'apellidoMaterno': ('Apellido Materno'),
		'fechaCreacionRegistro': ('Fecha de registro'),
		'promotor': ('Promotor'),
		'formaContacto': ('Forma de Contacto'),
		'telefono': ('Teléfono'),
		'celular': ('Celular'),
		'medioContacto': ('Medio de Contacto'),
		'servicioInteres': ('Servicio que le interesa'),
		}