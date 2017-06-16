from django.shortcuts import render, get_object_or_404, render_to_response, redirect # is used to looks for the object that is related the call
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.core.mail import send_mail
from .models import Aspirantes
from .forms import NuevoProspecto
from django.contrib.auth.decorators import permission_required

@permission_required('polls.can_vote')
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
