
from django.shortcuts import render, get_object_or_404, render_to_response, redirect # is used to looks for the object that is related the call
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.core.mail import send_mail
from .models import Aspirante, Alumno
from .forms import FormularioContactos, NuevoProspecto
import csv


# Create your views here.
def index(request):
	return render(request, 'siad/index.html', {})

def atributos_meta(request): 
	valor = request.META.items() 
	valor.sort() 
	html = [] 
	for k, v in valor: 
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v)) 
	return HttpResponse('<table>%s</table>' % '\n'.join(html)) 


def formulario_buscar(request):
	return render(request, 'siad/formulario_buscar.html')

def formulario_buscar_alumno(request):
	return render(request, 'siad/formulario_buscar_alumno.html')

def buscar(request): 
	error = False 
	if 'q' in request.GET: 
		q = request.GET['q'] 
		if not q: 
			error = True 
		else: 
			libros = Aspirante.objects.filter(nombre__icontains=q) 
			return render(request, 'siad/resultados.html', {'aspirantes': libros, 'query': q}) 
 
	return render(request, 'siad/formulario_buscar.html', {'error': error}) 

def buscar_alumno(request): 
	error = False 
	if 's' in request.GET: 
		s = request.GET['s'] 
		if not s: 
			error = True 
		else: 
			alumnos = Alumno.objects.filter(id__icontains=s) 
			return render(request, 'siad/resultados_alumno.html', {'alumnos': alumnos, 'query': s}) 
 
	return render(request, 'siad/formulario_buscar_alumno.html', {'error': error}) 


def contactos(request): 
    if request.method == 'POST': 
        form = FormularioContactos(request.POST) 
        if form.is_valid(): 
            cd = form.cleaned_data 
            send_mail( 
                cd['asunto'], 
                cd['mensaje'], 
                cd.get('email', 'indira.fraga@gmail.com'), 
                    ['indira.fraga@gmail.com'], 
             ) 
            return HttpResponseRedirect('/contactos/gracias/') 
    else: 
        form = FormularioContactos() 
    return render(request, 'formulario_contactos.html', {'form': form})

def control_escolar(request):
	lista_alumnos_total = Alumno.objects.order_by("id")
	return render_to_response('siad/formulario_buscar_alumno.html', {'lista_alumnos_total':lista_alumnos_total})

def contabilidad(request):
    return render(request,'siad/contabilidad.html')

def promotoria(request):
	lista_prospectos_total = Aspirante.objects.order_by("id")
	return render_to_response('siad/formulario_buscar.html', {'lista_prospectos_total':lista_prospectos_total})

def nuevo_prospecto(request):
	if request.method == 'Post':
		form = NuevoProspecto(request.Post) 
		if form.is_valid():
			form.save()
		return redirect('promotoria')
	else:
		form = NuevoProspecto()
	return render(request, 'siad/nuevo_prospecto.html', {'form': form})

