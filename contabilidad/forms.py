from django import forms
from django.forms import ModelForm, Textarea
from .models import Egreso
from siad.models import Plantel
import datetime 
import dateutil.relativedelta
from django.forms.extras.widgets import SelectDateWidget

class NuevoEgreso(ModelForm): 

	class Meta:
		model = Egreso
		fields = '__all__'
		labels = {
		'concepto': ('Concepto'),
		}
class adeudo_alumno_form(forms.Form):
	lista_planteles = [
	('Todos','todos'),
	('Ninguno','Ninguno')
	]
	#lista_planteles = []
	#for item in planteles:
#		lista_planteles.append((item,item))


	#fecha= forms.DateField(
	#	widget=SelectDateWidget,
	#	label = 'Adeudos a partir de:',
	#	)
	cantidad = forms.DecimalField(max_digits = 7,decimal_places=2)
	plantel = forms.ModelChoiceField(
	#	widget=forms.RadioSelect(),
		queryset = Plantel.objects.all()
		)
	
	