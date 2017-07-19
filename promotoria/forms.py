from django import forms
from django.forms import ModelForm, Textarea
from .models import Aspirantes

class FormularioContactos(forms.Form): 
	asunto = forms.CharField()
	email = forms.EmailField(required=False) 
	mensaje = forms.CharField()

class NuevoProspecto(ModelForm): 

	class Meta:
		model = Aspirantes

		fields = '__all__'
		labels = {
		'nombre': ('Nombre'),
		'apellidoPaterno': ('Apellido Paterno'),
		'apellidoMaterno': ('Apellido Materno'),
		'fechaCreacionRegistro': ('Fecha de registro'),
		'promotor': ('Promotor'),
		'formaContacto': ('Forma de Contacto'),
		'telefono': ('Telefono'),
		'celular': ('Celular'),
		'medioContacto': ('Medio de Contacto'),
		'servicioInteres': ('Servicio que le interesa'),
		}


class ConsultaAspiranteForm(ModelForm): 
	name = forms.CharField()
	url = forms.URLField()
	class Meta:
		model = Aspirantes

		fields = '__all__'
		