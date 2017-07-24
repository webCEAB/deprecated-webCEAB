
from django.shortcuts import render, get_object_or_404, render_to_response, redirect # is used to looks for the object that is related the call
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.core.mail import send_mail
from .forms import FormularioContactos
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

def agregar_campo(request):
    return render(request,'siad/agrega_campo.html')