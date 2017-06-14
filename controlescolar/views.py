from django.shortcuts import render, get_object_or_404, render_to_response, redirect # is used to looks for the object that is related the call
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.core.mail import send_mail
from .models import Estudiante
from .forms import NuevoAlumno

def control_escolares(request):
	lista_alumnos_total = Estudiante.objects.order_by("id")
	return render_to_response('siad/formulario_buscar_alumno.html', {'lista_alumnos_total':lista_alumnos_total})

def buscar_alumnos(request): 
	error = False 
	if 's' in request.GET: 
		s = request.GET['s'] 
		if not s: 
			error = True 
		else: 
			alumnos = Estudiante.objects.filter(id__icontains=s) 
			return render(request, 'siad/resultados_alumno.html', {'alumnos': alumnos, 'query': s}) 
 
	return render(request, 'siad/formulario_buscar_alumno.html', {'error': error}) 

def nuevo_alumno(request):
	if request.method == 'POST':
		form = NuevoAlumno(request.POST) 
		if form.is_valid():
			form.save()
		return redirect('control_escolares')
	else:
		form = NuevoAlumno()
	return render(request, 'siad/nuevo_alumno.html', {'form': form})