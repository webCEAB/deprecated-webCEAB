from django.shortcuts import render, get_object_or_404, render_to_response, redirect # is used to looks for the object that is related the call
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
import dateutil.relativedelta
from django.core.mail import send_mail
from .models import Egreso
from controlescolar.models import Estudiante
from promotoria.models import Aspirantes
#from promotoria.models import Aspirantes
from .forms import NuevoEgreso, adeudo_alumno_form
from django.contrib.auth.decorators import permission_required

# Create your views here.
def contabilidad(request):
    return render(request,'contabilidad/contabilidad.html')

def nuevo_egreso(request):
	if request.method == 'POST':
		form = NuevoEgreso(request.POST) 
		if form.is_valid():
			form.save()
		return redirect('contabilidad')
	else:
		form = NuevoEgreso()
	return render(request, 'contabilidad/nuevo_egreso.html', {'form': form})
def consulta_adeudo_alumnos(request):
	if request.method == 'POST':
		form = adeudo_alumno_form(request.POST)
		if form.is_valid():
			cantidad = form.cleaned_data['cantidad']
			plantel = form.cleaned_data['plantel']
			# De la tabla aspirantes elegimos todos los que cumplan con el filtro
			# de plantel
			queryset = Aspirantes.objects.filter(plantel = plantel)
			# Ahora Hacemos una consulta de la consulta anterior, filtrando los 
			# datos anteriores usando otro criterio 
			queryset2 = Estudiante.objects.filter(Aspirante__in = queryset)

			lista = []
			for item in queryset2:
				lista.append([item.Aspirante.nombre + " " +item.Aspirante.apellidoPaterno +" " + item.Aspirante.apellidoMaterno,item.adeudo])
			encabezados = ["Nombre","Adeudo"]
			context={
			"lista":lista,
			"encabezados": encabezados,
			}
			print "NOSE PORQUE NO FUNCIONA"
			#lista1 = [[1,2,3],[1,2,3],4]
			#HttpResponse("Hola" + str(lista1))
			return render(request, "siad/resultado_consulta.html", context)
	else:
		fecha_default = datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=1)
		form = adeudo_alumno_form(initial = {
			'fecha':fecha_default,
			'cantidad':0.0
			})

	context = {
		"form":form,
	}
	return render(request, "siad/adeudo_alumnos.html", context)

