from django import forms
from django.forms import ModelForm, Textarea,FileInput
from .models import Estudiante,Aspirantes
from django.contrib import admin
admin.autodiscover()

from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django import forms


class NuevoAlumno2(ModelForm): 
	Aspirante = forms.ModelChoiceField(
        Aspirantes.objects.all(),
        widget=ForeignKeyRawIdWidget(Estudiante._meta.get_field("Aspirante").rel,admin.site)
    )
	class Meta:
		model = Estudiante

		fields = '__all__'
		#labels = {
		#'fechaCreacionRegistro': ('Fecha de registro'),
		#'plantelRegistro': ('Plantel de informes'),
		#'aspirante': ('Aspirante'),
		#'numerocontrol': ('Numero de Control interno'),
		#}
		readonly_fields = ['numeroControl']

class NuevoAlumno(ModelForm): 
	Aspirante = forms.ModelChoiceField(queryset  =None)
	class Meta:
		model = Estudiante

		fields = '__all__'
		labels = {
		'fechaCreacionRegistro': ('Fecha de registro'),
		'plantelRegistro': ('Plantel de informes'),
		'aspirante': ('Aspirante'),
		'numerocontrol': ('Numero de Control interno'),
		}
		readonly_fields = ['numeroControl']

