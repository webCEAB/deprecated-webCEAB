from django.shortcuts import render, get_object_or_404, render_to_response, redirect, HttpResponseRedirect # is used to looks for the object that is related the call
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.core.mail import send_mail
from .models import Aspirantes
from .forms import NuevoProspecto, ConsultaAspiranteForm
from django.contrib.auth.decorators import permission_required


def detalleAspirante(request,id = None):
	instance = get_object_or_404(Aspirantes, id=id)
	context = {
		"instance": instance,
	}
	return render(request, "promotoria/detalleAspirante.html", context)
def editaProspecto(request,id = None):
	instance = get_object_or_404(Aspirantes, id=id)
	form = ConsultaAspiranteForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print instance.get_absolute_url()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form":form,
	}
	return render(request, "promotoria/editaProspecto.html", context)
def promotorianva(request):
	if not request.user.is_authenticated:
		return redirect('index')
	else:
		lista_prospectos_total = Aspirantes.objects.order_by("id")
		return render_to_response('promotoria/formulario_buscar.html', {'lista_prospectos_total':lista_prospectos_total})

def nuevo_prospecto(request):
	if request.method == 'POST':
		form = NuevoProspecto(request.POST) 
		if form.is_valid():
			form.save()
		return redirect('promotorianva')
	else:
		form = NuevoProspecto()
	return render(request, 'promotoria/nuevo_prospecto.html', {'form': form})

def formulario_buscar(request):
	return render(request, 'promotoria/formulario_buscar.html')

def buscar_aspirante(request): 
	error = False 
	if 'q' in request.GET: 
		q = request.GET['q'] 
		if not q: 
			error = True 
		else: 
			libros = Aspirantes.objects.filter(nombre__icontains=q) 
			return render(request, 'promotoria/resultados.html', {'aspirantes': libros, 'query': q}) 
 
	return render(request, 'promotoria/formulario_buscar.html', {'error': error}) 

# Create your views here.
