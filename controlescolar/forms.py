from django import forms
from django.forms import ModelForm, Textarea
from .models import Estudiante

class NuevoAlumno(ModelForm): 

	class Meta:
		model = Estudiante

		fields = '__all__'
		labels = {
		'fechaCreacionRegistro': ('Fecha de registro'),
		'plantelRegistro': ('Plantel de informes'),
		'aspirante': ('Aspirante'),
		'numerocontrol': ('Numero de Control interno'),
		}