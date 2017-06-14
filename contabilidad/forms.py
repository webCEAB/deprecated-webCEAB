from django import forms
from django.forms import ModelForm, Textarea
from .models import Egreso

class NuevoEgreso(ModelForm): 

	class Meta:
		model = Egreso
		fields = '__all__'
		labels = {
		'concepto': ('Concepto'),
		}