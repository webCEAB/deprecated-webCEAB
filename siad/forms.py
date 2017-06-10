from django import forms
from django.forms import ModelForm, Textarea
from promotoria.models import Aspirantes

class FormularioContactos(forms.Form): 
	asunto = forms.CharField()
	email = forms.EmailField(required=False) 
	mensaje = forms.CharField()